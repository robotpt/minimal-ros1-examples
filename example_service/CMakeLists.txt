cmake_minimum_required(VERSION 2.8.3)

project(example_service)

find_package(catkin REQUIRED COMPONENTS
  rospy
  message_generation
)
add_service_files(
  FILES
  Instructions.srv
)
generate_messages()
catkin_package()
