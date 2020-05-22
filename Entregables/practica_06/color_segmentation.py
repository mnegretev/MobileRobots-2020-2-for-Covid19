#!/usr/bin/env python

import rospy
import cv2
import cv_bridge
import numpy
from sensor_msgs.msg import Image

# HSV min del Dinosaurio    60, 200, 60
# HSV max del Dinosaurio    80, 255, 255

# HSV min de la Taza        94, 59, 69
# HSV max de la Taza        98, 57, 51

my_min_H = (92 * 180) / 360
my_min_S = (55 * 255) / 100
my_min_V = (55 * 255) / 100

my_max_H = (100 * 180) / 360
my_max_S = (75 * 255) / 100
my_max_V = (75 * 255) / 100

def callback_rgb(msg):
    bridge = cv_bridge.CvBridge()
    img_bgr = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    # frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    img_bin = cv2.inRange(img_hsv, numpy.array([my_min_H, my_min_S, my_min_V]), numpy.array([my_max_H, my_max_S, my_max_V]))
    idx = cv2.findNonZero(img_bin)
    [centroid_x, centroid_y, a, b] = cv2.mean(idx)
    cv2.circle(img_bgr, (int(centroid_x), int(centroid_y)), 20, [0, 255, 0], thickness=3)
    cv2.imshow("Image BGR", img_bgr)
    cv2.imshow("Image HSV", img_hsv)
    cv2.imshow("Image Binary", img_bin)
    cv2.waitKey(1)

def main():
    print "INITIALIZING COLOR SEGMENTATION NODE..."

    print "Min HSV: ", my_min_H, ", ", my_min_S, ", ", my_min_V
    print "Max HSV: ", my_max_H, ", ", my_max_S, ", ", my_max_V

    rospy.init_node("color_segmentation")
    rospy.Subscriber("/camera/color/image_raw"   , Image,       callback_rgb )
    loop = rospy.Rate(30)
    while not rospy.is_shutdown():
        loop.sleep()

if __name__ == "__main__":
    main()
