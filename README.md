# patrol_robot

A low-resource ROS2 patrol robot project developed in WSL Ubuntu with VS Code.

## Features

- Automatic patrol controller
- Fake laser scan publisher
- Obstacle avoidance node
- Safe velocity command output
- Base driver simulation
- ROS2 launch integration

## Environment

- Windows + WSL2
- Ubuntu 22.04
- ROS2 Humble
- VS Code

## Build

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash