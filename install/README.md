# robotaxi
clone repository to home

rename the folder to catkin_ws

run catkin_make inside the folder

add bashrc lines 

source /opt/ros/noetic/setup.bash

source ~/catkin_ws/devel/setup.bash

export TURTLEBOT3_MODEL=waffle_pi

export GAZEBO_MODEL_PATH=~/catkin_ws/src/ros_autonomous_slam/worlds


change /home/yg to your username in /worlds/world.world

start gazebo with car and mesh file

roslaunch ros_autonomous_slam turtlebot3_world.launch 

start controller

rosrun teleop_twist_keyboard teleop_twist_keyboard.py

start camera view

rosrun teleop_twist_keyboard teleop_twist_keyboard.py


# In a CMake project
$ mkdir build
$ cd build
$ cmake ..
$ make
$ make install  # (optionally)
