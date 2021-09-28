cmake_minimum_required(VERSION 3.5)
project(tianracer_core)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(
  include/tianboard
)

add_executable(${PROJECT_NAME}_node src/main.cpp)

add_library(tian_core SHARED src/tianboard.cpp)


ament_target_dependencies(${PROJECT_NAME}_node
  std_msgs
  rclcpp)

target_link_libraries(${PROJECT_NAME}_node tian_core)

install(
  DIRECTORY include
  DESTINATION share/${PROJECT_NAME}
)

install(
  TARGETS ${PROJECT_NAME}_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
