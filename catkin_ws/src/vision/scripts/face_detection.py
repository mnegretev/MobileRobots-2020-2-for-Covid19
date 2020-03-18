#!/usr/bin/env python

import rospy
import cv2

def main():
    print "INITIALIZING FACE DETECTION NODE..."
    rospy.init_node("face_detection")
    loop = rospy.Rate(30)

    while not rospy.is_shutdown():
        loop.sleep()

if __name__ == "__main__":
    main()
