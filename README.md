# rclrockstar

A ROS 2 client library for the [Rockstar](https://codewithrockstar.com) programming language.

## Why?

So we can all be rockstar robot developers 🧑‍🎤 🤖

## Features

- Create ROS nodes
- Create ROS publishers for type `std_msgs/msg/String`
- Publish string data

## Roadmap

- Create ROS subscriptions for type `std_msgs/msg/String`
- Create ROS timers

## Setup

1. Install [ROS 2](https://docs.ros.org/en/foxy/Installation.html) (Foxy or newer)

1. Clone this repository

    git clone https://github.com/jacobperron/rclrockstar.git

1. Install Python dependencies with [Poetry](https://python-poetry.org/)

    pip3 install poetry
    cd rclrockstar
    poetry install

## Usage

In the root of the repository,

    poetry run ros_rocks examples/example.rock

For more info,

    poetry run ros_rocks --help 

## Examples

You can find examples [here](https://github.com/jacobperron/rclrockstar/tree/main/examples)

## License

This project is licensed under the MIT License.
See the full license [here](https://github.com/jacobperron/rclrockstar/blob/main/LICENSE).

## Acknowledgments

- Thanks to [yyyyyyyan](https://github.com/yyyyyyyan) for [`rockstar -py`](https://github.com/yyyyyyyan/rockstar-py), which is where the transpilation code was copied from.
