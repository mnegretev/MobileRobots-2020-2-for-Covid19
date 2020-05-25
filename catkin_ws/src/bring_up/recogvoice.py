#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String

recv = ''
pub = rospy.Publisher('heardString', String, queue_size = 10)

def callback(data):
	global recv
	rospy.loginfo(rospy.get_caller_id()+"I heard %s", data.data)
	if data.data == 'VE A LA SALA':
		pub.publish('sala')
	elif data.data == 'VE A LA COCINA':
		pub.publish('cocina')
	elif data.data == 'VE A LA BODEGA':
		pub.publish('bodega')
	elif data.data == 'VE A LA PUERTA':
		pub.publish('puerta')

def controller():
	rospy.init_node('recogvoice', anonymous = True)

	rospy.Subscriber("recognized", String, callback)

	rospy.spin()


if __name__ == '__main__':
	controller()