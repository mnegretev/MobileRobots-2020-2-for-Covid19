#!/usr/bin/env python
#yolo
import rospy
import tf
import time 
import roslib
import sys
import os

from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped	#geometry_msgs --> Twist||String


class image_feature:

    def __init__(self):
        '''Initialize ros publisher, ros subscriber'''
        # topic where we publish
        self.image_pub = rospy.Publisher("/move_base_simple/goal",PoseStamped, queue_size=10)
        # self.bridge = CvBridge()

        # subscribed Topic
        self.subscriber = rospy.Subscriber("/recognized",String, self.callback)
     
    def callback(self, ros_data):
	print 'Escuche ', str (ros_data)
	len = str(ros_data.data)
	print len

	if len == 'ROBOT GO TO THE KITCHEN':
			
		msg = PoseStamped()
        	msg.header.stamp = rospy.Time.now()
		msg.header.frame_id = "map"
		msg.pose.position.x=-10.4599180222
		msg.pose.position.y=5.55513000488
		msg.pose.orientation.w=1

        	self.image_pub.publish(msg)
	
	elif len == 'ROBOT GO TO THE ENTRY':

		
		msg = PoseStamped()
        	msg.header.stamp = rospy.Time.now()
		msg.header.frame_id = "map"
		msg.pose.position.x=-7.49327802658
		msg.pose.position.y=-2.61084508896
		msg.pose.orientation.w=1

        	self.image_pub.publish(msg)
		

	elif len == 'ROBOT GO TO THE LIVINGROOM':

		
		msg = PoseStamped()
        	msg.header.stamp = rospy.Time.now()
		msg.header.frame_id = "map"
		msg.pose.position.x=-3.56561517715
		msg.pose.position.y=-0.613797664642
		msg.pose.orientation.w=1

        	self.image_pub.publish(msg)

	elif len == 'ROBOT GO TO THE BEDROOM':

		
		msg = PoseStamped()
        	msg.header.stamp = rospy.Time.now()
		msg.header.frame_id = "map"
		msg.pose.position.x=3.34376144409
		msg.pose.position.y=-0.892126083374
		msg.pose.orientation.w=1

        	self.image_pub.publish(msg)

	else: 

		
		msg = PoseStamped()
        	msg.header.stamp = rospy.Time.now()
		msg.header.frame_id = "map"
		msg.pose.position.x=20.4228782654		#jardin
		msg.pose.position.y=5.56792259216
		msg.pose.orientation.w=1

        	self.image_pub.publish(msg)




def main(args):
    '''Initializes and cleanup ros node'''
    ic = image_feature()
    rospy.init_node('image_feature', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Image feature detector module"


if __name__ == '__main__':
    main(sys.argv)








