cmake_minimum_required(VERSION 2.8.3)

project(example_topic)

find_package(catkin REQUIRED COMPONENTS
  rospy
  message_generation
)
add_message_files(
  FILES
  Message.msg
)
generate_messages()
catkin_package()
