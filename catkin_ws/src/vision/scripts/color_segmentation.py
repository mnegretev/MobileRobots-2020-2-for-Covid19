#!/usr/bin/env python

import rospy
import cv2
import cv_bridge
import numpy
from sensor_msgs.msg import Image

def callback_rgb(msg):
    bridge = cv_bridge.CvBridge()
    img_bgr = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    img_bin = cv2.inRange(img_hsv, numpy.array([45,134,84]), numpy.array([80, 255, 255]))
    idx = cv2.findNonZero(img_bin)
    [centroid_x, centroid_y, a, b] = cv2.mean(idx)
    cv2.circle(img_bgr, (int(centroid_x), int(centroid_y)), 20, [0, 255, 0], thickness=3)
    cv2.imshow("Image BGR", img_bgr)
    cv2.imshow("Image HSV", img_hsv)
    cv2.imshow("Image Binary", img_bin)
    cv2.waitKey(1)
    
def main():
    print "INITIALIZING COLOR SEGMENTATION NODE..."
    rospy.init_node("color_segmentation")
    rospy.Subscriber("/camera/color/image_raw"   , Image,       callback_rgb )
    loop = rospy.Rate(30)
    while not rospy.is_shutdown():
        loop.sleep()

if __name__ == "__main__":
    main()
