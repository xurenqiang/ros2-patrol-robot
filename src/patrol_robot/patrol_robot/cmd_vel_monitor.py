import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CmdVelMonitor(Node):
    def __init__(self):
        super().__init__('cmd_vel_monitor')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )
        self.get_logger().info('cmd_vel_monitor started, listening on /cmd_vel')

    def cmd_callback(self, msg: Twist):
        self.get_logger().info(
            f'Received /cmd_vel -> linear.x: {msg.linear.x:.2f}, angular.z: {msg.angular.z:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = CmdVelMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()