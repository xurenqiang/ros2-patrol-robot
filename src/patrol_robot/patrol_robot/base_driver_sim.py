import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class BaseDriverSim(Node):
    def __init__(self):
        super().__init__('base_driver_sim')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel_safe',
            self.cmd_callback,
            10
        )
        self.get_logger().info('base_driver_sim started, listening on /cmd_vel_safe')

    def cmd_callback(self, msg: Twist):
        if msg.linear.x > 0.0 and abs(msg.angular.z) < 0.1:
            action = 'Moving forward'
        elif msg.angular.z > 0.1:
            action = 'Turning left'
        elif msg.angular.z < -0.1:
            action = 'Turning right'
        else:
            action = 'Stopped'

        self.get_logger().info(
            f'Base action: {action}, linear.x={msg.linear.x:.2f}, angular.z={msg.angular.z:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = BaseDriverSim()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()