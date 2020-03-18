#!/usr/bin/env python

import rospy
import numpy

def inverse_kinematics(x, y, z, roll, pitch, yaw, elbow):
    articular = [0,0,0,0,0,0,0]
    return articular


def main():
    print "INITIALIZING INVERSE KINEMATICS NODE..."
    rospy.init_node("inverse_kinematics")
    loop = rospy.Rate(10)

    while not rospy.is_shutdown():
        loop.sleep()

if __name__ == "__main__":
    main()
