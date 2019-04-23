 cmake_minimum_required(VERSION 2.8.3)
 project(robotic_arm_control)
 
 find_package(catkin REQUIRED COMPONENTS
  controller_manager 
  joint_state_controller 
  robot_state_publisher 
 )
 
 find_package(gazebo REQUIRED)
 
 include_directories(include ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS} ${SDFormat_INCLUDE_DIRS})
 
 catkin_package(
     DEPENDS
     CATKIN_DEPENDS
     INCLUDE_DIRS
     LIBRARIES ${PROJECT_NAME}
 ) 
 
install(DIRECTORY launch config
DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

