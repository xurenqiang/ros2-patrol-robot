import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')

        self.cmd_sub = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )
        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )
        self.safe_cmd_pub = self.create_publisher(Twist, '/cmd_vel_safe', 10)

        self.latest_cmd = Twist()
        self.obstacle_detected = False

        self.get_logger().info('obstacle_avoidance started')

    def cmd_callback(self, msg: Twist):
        self.latest_cmd = msg
        self.publish_safe_cmd()

    def scan_callback(self, msg: LaserScan):
        front_ranges = msg.ranges[4:6]
        min_front = min(front_ranges)

        if min_front < 0.5:
            self.obstacle_detected = True
            self.get_logger().warn(f'Obstacle detected! front min distance = {min_front:.2f}')
        else:
            self.obstacle_detected = False

        self.publish_safe_cmd()

    def publish_safe_cmd(self):
        safe_cmd = Twist()

        if self.obstacle_detected and self.latest_cmd.linear.x > 0.0:
            safe_cmd.linear.x = 0.0
            safe_cmd.angular.z = 0.5
        else:
            safe_cmd = self.latest_cmd

        self.safe_cmd_pub.publish(safe_cmd)


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()