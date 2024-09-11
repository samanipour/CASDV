from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    vehilce_controller_node = Node(
        package='vehicle',
        executable='vehicle_controller'
    )
    ld.add_action(vehilce_controller_node)
    return ld