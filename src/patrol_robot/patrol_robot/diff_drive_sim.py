import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TransformStamped
from tf2_ros import TransformBroadcaster

class DiffDriveSim(Node):
    def __init__(self):
        super().__init__('diff_drive_sim')
        # 订阅安全速度
        self.subscription = self.create_subscription(Twist, '/cmd_vel_safe', self.cmd_callback, 10)
        self.tf_broadcaster = TransformBroadcaster(self)
        
        self.current_cmd = Twist()
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        
        self.dt = 0.1 # 增大一点步长方便观察
        self.timer = self.create_timer(self.dt, self.update_pose)
        self.get_logger().info('Simulation node started!')

    def cmd_callback(self, msg: Twist):
        self.current_cmd = msg

    def update_pose(self):
        vx = self.current_cmd.linear.x
        wz = self.current_cmd.angular.z
        
        # 计算位移
        self.x += vx * math.cos(self.yaw) * self.dt
        self.y += vx * math.sin(self.yaw) * self.dt
        self.yaw += wz * self.dt
        
        # 强制打印，看看数值到底变没变
        self.get_logger().info(f"Pose: x={self.x:.3f}, vx={vx:.2f}")
        
        self.publish_tf()

    def publish_tf(self):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.translation.z = 0.0
        
        qz = math.sin(self.yaw / 2.0)
        qw = math.cos(self.yaw / 2.0)
        t.transform.rotation.z = qz
        t.transform.rotation.w = qw
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = DiffDriveSim()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()