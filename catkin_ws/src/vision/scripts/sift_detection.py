#!/usr/bin/env python

import rospy
import cv2
import cv_bridge
import numpy
from sensor_msgs.msg import Image

def callback_rgb(msg):
    bridge = cv_bridge.CvBridge()
    img_bgr  = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    img_ori  = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp, des = sift.detectAndCompute(img_gray,None)
    cv2.drawKeypoints(img_gray,kp,img_bgr)
    cv2.imshow("SIFT Keypoints", img_bgr)
    cv2.imshow("BGR Image", img_ori)
    cv2.waitKey(1)
    
def main():
    print "INITIALIZING SIFT DETECTION NODE..."
    rospy.init_node("sift_detection")
    rospy.Subscriber("/camera/color/image_raw"   , Image,       callback_rgb )
    loop = rospy.Rate(30)
    while not rospy.is_shutdown():
        loop.sleep()
        
if __name__ == "__main__":
    main()
