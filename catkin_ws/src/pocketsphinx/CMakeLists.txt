cmake_minimum_required(VERSION 2.8.3)
project(pocketsphinx)

find_package(catkin REQUIRED COMPONENTS
    geometry_msgs
    std_msgs
    rospy
)

catkin_package(DEPENDS)

# catkin_package()


install(DIRECTORY demo
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
