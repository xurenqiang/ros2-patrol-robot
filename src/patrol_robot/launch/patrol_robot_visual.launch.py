import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description():
    package_share = get_package_share_directory('patrol_robot')
    xacro_file = os.path.join(package_share, 'urdf', 'patrol_robot.urdf.xacro')
    rviz_config = os.path.join(package_share, 'rviz', 'patrol_robot.rviz')
    params_file = os.path.join(package_share, 'config', 'params.yaml')

    robot_description = {
        'robot_description': Command(['xacro ', xacro_file])
    }

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
            output='screen',
            parameters=[params_file]
        ),
        Node(
            package='patrol_robot',
            executable='obstacle_avoidance',
            name='obstacle_avoidance',
            output='screen',
            parameters=[params_file]
        ),
        Node(
            package='patrol_robot',
            executable='base_driver_sim',
            name='base_driver_sim',
            output='screen'
        ),
        Node(
            package='patrol_robot',
            executable='cmd_vel_monitor',
            name='cmd_vel_monitor',
            output='screen'
        ),
        Node(
            package='patrol_robot',
            executable='diff_drive_sim',
            name='diff_drive_sim',
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[robot_description]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config]
        ),
    ])
