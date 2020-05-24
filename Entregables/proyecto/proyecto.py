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







"""

-------------------------------------------------------------------------------------------------
					PUES SE ACERCA
-------------------------------------------------------------------------------------------------
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped	#geometry_msgs --> Twist||String


def callback(data):
    print "I heard ", str(data.data)
    len = str(data.data)
    print len

    if len == 'ROBOT GO TO THE KITCHEN':
    	#print("ahiuevo")
	#from geometry_msgs.msg import PoseStamped	#geometry_msgs --> Twist||String
	def pos_robot():
		pub=rospy.Publisher('/move_base_simple/goal',PoseStamped, queue_size=20)
		print "nodo creado con exito"
		obj=PoseStamped()
		while not rospy.is_shutdown():
			obj.header.frame_id = "map"
			obj.header.stamp = rospy.Time.now()
			obj.pose.position.x=7.95961523056
			obj.pose.position.y=0.785449028015
			obj.pose.orientation.w=1
			pub.publish(obj)
			time.sleep(2)
	
    else:
    	print("ahuevo puto marcos")
   


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/recognized", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()




	

if __name__ == '__main__':
    listener()







------------------------------------------------------------------------------------------------------
					PUTA MADRE QUE TE PARIO
------------------------------------------------------------------------------------------------------


from geometry_msgs.msg import PoseStamped

VERBOSE=False

class image_feature:

 def __init__(self):
        '''Initialize ros publisher, ros subscriber'''
        # topic where we publish
        self.image_pub = rospy.Publisher("/move_base_simple/goal",PoseStamped, queue_size = 10)
        # self.bridge = CvBridge()
from std_msgs.msg import String
        # subscribed Topic
        self.subscriber = rospy.Subscriber("/recognized",String, self.callback, queue_size = 1)
        if VERBOSE :
            print "subscribed to /recognized"


def callback(self, ros_data):
        obj = PoseStamped()
        obj.header.stamp = rospy.Time.now()
        # Publish new image
        self.image_pub.publish(obj)
	while not rospy.is_shutdown():
		obj.header.frame_id = "map"
		obj.header.stamp = rospy.Time.now()
		obj.pose.position.x=7.95961523056
		obj.pose.position.y=0.785449028015
		obj.pose.orientation.w=1
		pub.publish(obj)
		time.sleep(2)

def main(args):
    '''Initializes and cleanup ros node'''
    ic = image_feature()
    rospy.init_node('image_feature', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Image feature detector module"


if __name__ == '__main__':
    main(sys)
---------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------
#				PUBLICA DONDE VA EL ROBOT 
#-------------------------------------------------------------------------------------------
from geometry_msgs.msg import PoseStamped	#geometry_msgs --> Twist||String
def pos_robot():
	pub=rospy.Publisher('/move_base_simple/goal',PoseStamped, queue_size=20)
	rospy.init_node('where_to', anonymous=True)
	print "nodo creado con exito"
	obj=PoseStamped()
	while not rospy.is_shutdown():
		obj.header.frame_id = "map"
		obj.header.stamp = rospy.Time.now()
		obj.pose.position.x=7.95961523056
		obj.pose.position.y=0.785449028015
		obj.pose.orientation.w=1
		pub.publish(obj)
		time.sleep(2)


if __name__ =='__main__':
	try:
		pos_robot()
	except rospy.ROSInterruptException:
		pass

#--------------------------------------------------------------------------------------------



"""


