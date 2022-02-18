cmake_minimum_required(VERSION 3.5)
project(odrive_ros)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)  
find_package(std_msgs REQUIRED)  
find_package(geometry_msgs REQUIRED)  
find_package(diagnostic_msgs REQUIRED)  
find_package(diagnostic_updater REQUIRED)  


## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  #include
  )


#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
install(PROGRAMS
  nodes/odrive_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()


