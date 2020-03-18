#!/usr/bin/env python

import rospy
import rospkg
import cv_bridge
import cv2
import json
import numpy
from sensor_msgs.msg import Image

sift = cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

def from_json(file_name):
    kp  = []
    des = []
    d = json.load(open(file_name, 'r'))
    for x in d:
        kp.append(cv2.KeyPoint(x["pt"][0], x["pt"][1], x["size"], x["angle"], x["response"], x["octave"], x["class_id"]))
        des.append(x["descriptor"])
    des = numpy.asarray(des, dtype=numpy.float32)
    return kp, des

def callback_rgb(msg):
    global img_bgr
    bridge = cv_bridge.CvBridge()
    img_bgr = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    kp_query, des_query = sift.detectAndCompute(img_gray,None)
    matches = flann.knnMatch(des_query, des_train, k=2)
        
    good_points = []
    for m,n in matches:
        if m.distance < 0.7*n.distance: #Two best matches are similar enough
            good_points.append([kp_query[m.queryIdx].pt[0], kp_query[m.queryIdx].pt[1]])
            
    if len(good_points) > 10:
        good_points = numpy.asarray(good_points)
        max_p = numpy.amax(good_points, axis=0)
        min_p = numpy.amin(good_points, axis=0)
        cv2.rectangle(img_bgr, (int(max_p[0]), int(max_p[1])), (int(min_p[0]), int(min_p[1])), (255,0,0), 2)
    cv2.imshow("Recognized objects", img_bgr)
    cv2.waitKey(1)

def main():
    print "INITIALIZING SIFT RECOGNITION NODE..."
    rospy.init_node("sift_recognition")
    rospy.Subscriber("/camera/color/image_raw"   , Image,       callback_rgb )
    loop = rospy.Rate(30)

    print "Loading trained keypoints..."
    global kp_train, des_train
    obj_name = rospy.get_param("~object_name")
    pkg_path = rospkg.RosPack().get_path('vision')
    obj_file = pkg_path + "/training/" + obj_name + ".json"
    kp_train, des_train = from_json(obj_file)    
    
    while not rospy.is_shutdown():
        loop.sleep()

if __name__ == "__main__":
    main()
