cmake_minimum_required(VERSION 2.8.3)

project(example_action)
find_package(catkin REQUIRED COMPONENTS
  rospy
  genmsg
  actionlib_msgs
)
add_action_files(
  FILES DoCount.action
)
generate_messages(
  DEPENDENCIES
  actionlib_msgs
)
catkin_package()
