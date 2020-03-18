#!/usr/bin/env python

import rospy
import cv2
import rospkg
import numpy
import json

def to_json(kp, des, file_name):
    data = []
    for i in range(len(kp)):
        d = {"pt":kp[i].pt}
        d["size"]       = kp[i].size
        d["angle"]      = kp[i].angle
        d["response"]   = kp[i].response
        d["octave"]     = kp[i].octave
        d["class_id"]   = kp[i].class_id
        d["descriptor"] = des[i].tolist()
        data.append(d)
    f = open(file_name, 'w')
    f.write(json.dumps(data, indent=4))
    f.close()
    
def main():
    print "INITIALIZING SIFT TRAINING NODE..."
    rospy.init_node("sift_detection")

    obj_name = rospy.get_param("~object_name")
    pkg_path = rospkg.RosPack().get_path('vision')
    obj_file = pkg_path + "/training/" + obj_name + ".png"
    print "Extracting features from image file: " + obj_file
    img_bgr  = cv2.imread(obj_file)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    sift = cv2.xfeatures2d.SIFT_create()
    kp, des = sift.detectAndCompute(img_gray,None)
    print [type(des), des.shape]
    cv2.drawKeypoints(img_gray,kp,img_bgr)
    kp_file = pkg_path + "/training/" + obj_name + ".json"
    to_json(kp, des, kp_file)
    print "Features stored in file: " + kp_file
    
    loop = rospy.Rate(30)
    while not rospy.is_shutdown():
        cv2.imshow("Training image", img_bgr)
        cv2.waitKey(10)
        loop.sleep()
        
if __name__ == "__main__":
    main()
