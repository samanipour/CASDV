#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class VehicleController(Node):
    def __init__(self):
        super().__init__("vehicle_controller")

def main(args=None):
    rclpy.init(args=args)
    node = VehicleController()
    node.get_logger().info("Vehicle Controller Started")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
