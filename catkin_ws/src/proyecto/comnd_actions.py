#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest

def rotate(x, y):
	x=double(x)
	y=double(y)
	goal = PoseStamped()
	goal.header.seq = 1
	goal.header.stamp = rospy.Time.now()
	goal.header.frame_id = "map"
	goal.pose.position.x = x
	goal.pose.position.y = y
	goal.pose.position.z = 0.0
	goal.pose.orientation.x = 0.0
	goal.pose.orientation.y = 0.0
	goal.pose.orientation.z = 0.0
	goal.pose.orientation.w = 1.0
	return goal


def callback(data):
	command =data.data
	if command == 'ROBOT GO TO POINT A':
		pub_goal = rospy.Publisher("move_base_simple/goal",PoseStamped,queue_size=5)
		goal = PoseStamped()
		goal.header.seq = 1
		goal.header.stamp = rospy.Time.now()
		goal.header.frame_id = "map"
		goal.pose.position.x = 6.6
		goal.pose.position.y = 2.9
		goal.pose.position.z = 0.0
		goal.pose.orientation.x = 0.0
		goal.pose.orientation.y = 0.0
		goal.pose.orientation.z = 0.0
		goal.pose.orientation.w = 1.0
		pub_goal.publish(goal)

	elif command == 'ROBOT SAY POTATO':

		pub_speech = rospy.Publisher("robotsound",SoundRequest,queue_size=10)
		loop = rospy.Rate(2)
		msg_speech = SoundRequest()
		msg_speech.sound = -3
		msg_speech.command = 1 
		msg_speech.volume = 1.0
		msg_speech.arg2 = "voice_us3_mbrola"
		msg_speech.arg = "potato"
		loop.sleep()
		pub_speech.publish(msg_speech)

	if command == 'ROBOT ROTATE':
		pub_goal = rospy.Publisher("move_base_simple/goal",PoseStamped,queue_size=5)

		goal=rotate(5.0,2.0)
		pub_goal.publish(goal)

		goal=rotate(5.0,5.0)
		pub_goal.publish(goal)

		goal=rotate(8.0,5.0)
		pub_goal.publish(goal)

		goal=rotate(8.0,2.0)
		pub_goal.publish(goal)

		goal=rotate(5.0,2.0)
		pub_goal.publish(goal)


	if command == 'GO FORWARD':
		pub_goal = rospy.Publisher("move_base_simple/goal",PoseStamped,queue_size=5)
		goal = PoseStamped()
		goal.header.seq = 1
		goal.header.stamp = rospy.Time.now()
		goal.header.frame_id = "map"
		goal.pose.position.x = 1.5
		goal.pose.position.y = 0.0
		goal.pose.position.z = 0.0
		goal.pose.orientation.x = 0.0
		goal.pose.orientation.y = 0.0
		goal.pose.orientation.z = 0.0
		goal.pose.orientation.w = 1.0
		pub_goal.publish(goal)

	else:
		pass


def listener():
	rospy.init_node('command',anonymous=True)
	rospy.Subscriber("recognized",String,callback)

	rospy.spin()


if __name__='__main__':
	listener()