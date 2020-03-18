#!/usr/bin/env python

import rospy
import rosbag
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import Image

def main():
    print "INITIALIZING RGBD_SIMUL NODE..."
    rospy.init_node("rgbd_simul")
    loop = rospy.Rate(30)
    pub_rgbd = rospy.Publisher("/camera/depth_registered/points", PointCloud2, queue_size=1)
    pub_rgb  = rospy.Publisher("/camera/color/image_raw",    Image      , queue_size=1)
    bag_file = ""
    if rospy.has_param("~bag_file"):
        bag_file = rospy.get_param("~bag_file")

    bag = rosbag.Bag(bag_file)
    while not rospy.is_shutdown():
        for topic, msg, t in bag.read_messages(topics=["/camera/depth_registered/points", "/camera/color/image_raw"]):
            msg.header.stamp = rospy.Time.now()
            if topic == "/camera/color/image_raw":
                pub_rgb.publish(msg)
            if topic == "/camera/depth_registered/points":
                pub_rgbd.publish(msg)
            loop.sleep()
    bag.close()
    
if __name__ == "__main__":
    main()
