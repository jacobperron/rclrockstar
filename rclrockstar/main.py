import argparse
import time

import rclpy
from rclpy.executors import ExternalShutdownException
import rclpy.node

from std_msgs.msg import String

from .transpile import transpile


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', type=str, help='Rockstar source file')
    parser.add_argument(
        '--print-python',
        action='store_true',
        help='Print transpiled Python source before executing.'
    )
    return parser.parse_args()


def Node(name):
    node = rclpy.node.Node(name)
    return node


def Publisher(node, topic):
    return node.create_publisher(String, topic, 1)


def publish(publisher, data):
    msg = String(data=data)
    publisher.publish(msg)


def rest(seconds):
    time.sleep(seconds)


# Let everything alias to 'ROS'
def Ros(*args):
    if len(args) == 1:
        if isinstance(args[0], str):
            return Node(*args)
        return rest(*args)
    if isinstance(args[0], rclpy.node.Node):
        return Publisher(*args)
    return publish(*args)


def main():
    args = parse_arguments()

    rclpy.init()

    python_code = transpile(args.source_file)
    if args.print_python:
        for line in python_code:
            print(line)

    try:
        exec('\n'.join(python_code))
    except (KeyboardInterrupt, ExternalShutdownException):
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
