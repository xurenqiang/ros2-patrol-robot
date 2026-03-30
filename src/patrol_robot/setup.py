from setuptools import setup
import os
from glob import glob

package_name = 'patrol_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xrq',
    maintainer_email='xrq@todo.todo',
    description='Low-resource ROS2 patrol robot project with RViz and URDF visualization',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cmd_vel_monitor = patrol_robot.cmd_vel_monitor:main',
            'fake_laser_publisher = patrol_robot.fake_laser_publisher:main',
            'obstacle_avoidance = patrol_robot.obstacle_avoidance:main',
            'base_driver_sim = patrol_robot.base_driver_sim:main',
            'patrol_controller = patrol_robot.patrol_controller:main',
            'diff_drive_sim = patrol_robot.diff_drive_sim:main',
        ],
    },
)