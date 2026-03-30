import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class FakeLaserPublisher(Node):
    def __init__(self):
        super().__init__('fake_laser_publisher')

        self.publisher_ = self.create_publisher(LaserScan, '/scan', 10)
        self.timer = self.create_timer(0.5, self.publish_scan)

        self.step = 0
        self.get_logger().info('fake_laser_publisher started, publishing /scan')

    def publish_scan(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'laser_frame'

        msg.angle_min = -1.57
        msg.angle_max = 1.57
        msg.angle_increment = 3.14 / 9.0
        msg.time_increment = 0.0
        msg.scan_time = 0.5
        msg.range_min = 0.1
        msg.range_max = 10.0

        ranges = [2.0] * 10

        # 每隔几次模拟前方有障碍
        if self.step % 8 in [3, 4]:
            ranges[4] = 0.3
            ranges[5] = 0.35

        msg.ranges = ranges
        self.publisher_.publish(msg)

        self.get_logger().info(f'Published fake scan: {ranges}')
        self.step += 1


def main(args=None):
    rclpy.init(args=args)
    node = FakeLaserPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()