import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# 启动雷达建图的所有准备
# 发布lidar, imu, odom, tf
def generate_launch_description():

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(
                get_package_share_directory("tianracer_core"),
                'launch', 'tianracer_core.launch.py')),
            ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(
                get_package_share_directory("tianracer_description"),
                'launch', 'tianracer_tf.launch.py')),
            ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(
                get_package_share_directory("tianracer_bringup"),
                'launch', 'lidar.launch.py')),
            ),
    ])