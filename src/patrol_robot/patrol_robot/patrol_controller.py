import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class PatrolController(Node):
    def __init__(self):
        super().__init__('patrol_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.publish_patrol_cmd)
        self.get_logger().info('patrol_controller started, publishing patrol commands')

    def publish_patrol_cmd(self):
        msg = Twist()
        msg.linear.x = 0.2
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info('Published patrol forward command')


def main(args=None):
    rclpy.init(args=args)
    node = PatrolController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()