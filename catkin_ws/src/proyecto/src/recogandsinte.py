#!/usr/bin/env python

import sys
import rospy
from sound_play.msg import SoundRequest
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped

place = "goal"

def callback_function(msg):
	global place 
	pub_goal= rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=10)
	loop = rospy.Rate(2)
	goal=PoseStamped()
	goal.pose.orientation.w=0.5
	goal.header.frame_id="map"
	x = msg.data.split(" ")
	place = x[4]
	print('goal: {}'.format(place))
	if(place=='EXIT'):
		goal.pose.position.x=9.57
		goal.pose.position.y=0.07
		print(goal)
		pub_goal.publish(goal)
	elif(place=='ENTRY'):
		goal.pose.position.x=0.0
		goal.pose.position.y=0.0
		print(goal)
		pub_goal.publish(goal)
	elif(place=='CENTER'):
		goal.pose.position.x=5.04
		goal.pose.position.y=3.45
		print(goal)
		pub_goal.publish(goal)
	elif(place=='CORNER'):
		goal.pose.position.x=9.40
		goal.pose.position.y=7.03
		print(goal)
		pub_goal.publish(goal)
	elif(place=='NOOK'):
		goal.pose.position.x=1.20
		goal.pose.position.y=6.86
		print(goal)
		pub_goal.publish(goal)
	else:
		loop.sleep()


def callback(msg):
	pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
	loop = rospy.Rate(2)
	msg_speech = SoundRequest()
	msg_speech.sound   = -3
	msg_speech.command = 1
	msg_speech.volume  = 1.0
	msg_speech.arg2    = "voice_us3_mbrola"
	msg_speech.arg = "the robot has arrive to the " + place
	loop.sleep()
	pub_speech.publish(msg_speech)
	print('{}'.format(msg.status.text))

def main():
	print "INITIALIZING SPEECH SYNTHESIS NODE..."
	rospy.init_node("speech_synthesize")
	rospy.Subscriber("/recognized",String, callback_function)
	rospy.Subscriber("/move_base/result" , MoveBaseActionResult , callback)
	rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass