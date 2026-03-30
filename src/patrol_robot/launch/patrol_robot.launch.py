from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='patrol_robot',
            executable='fake_laser_publisher',
            name='fake_laser_publisher',
            output='screen'
        ),
        Node(
            package='patrol_robot',
            executable='patrol_controller',
            name='patrol_controller',
            output='screen'
        ),
        Node(
            package='patrol_robot',
            executable='obstacle_avoidance',
            name='obstacle_avoidance',
            output='screen'
        ),
        Node(
            package='patrol_robot',
            executable='base_driver_sim',
            name='base_driver_sim',
            output='screen'
        ),
    ])
