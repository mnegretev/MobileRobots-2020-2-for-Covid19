#!/usr/bin/env python

import sys
import rospy
from sound_play.msg import SoundRequest
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped

place = "goal"
pub_goal= rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=10)
pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
msg_speech = SoundRequest()
msg_speech.sound   = -3
msg_speech.command = 1
msg_speech.volume  = 1.0
msg_speech.arg2    = "voice_us3_mbrola"

def callback_function(msg):
	global place 
	global pub_goal
	loop = rospy.Rate(2)
	goal=PoseStamped()
	goal.pose.orientation.w=0.5
	goal.header.frame_id="map"
	x = msg.data.split(" ")
	place = x[2]
	print('goal: {}'.format(place))
	if(place=='EXIT'):
		goal.pose.position.x=8.10
		goal.pose.position.y=0.86
	elif(place=='ENTRY'):
		goal.pose.position.x=2.0
		goal.pose.position.y=0.0
	elif(place=='CENTER'):
		goal.pose.position.x=5.04
		goal.pose.position.y=2.00
	elif(place=='END'):
		goal.pose.position.x=8.86
		goal.pose.position.y=6.42
	elif(place=='NOOK'):
		goal.pose.position.x=1.20
		goal.pose.position.y=6.86
	else:
		loop.sleep()
	pub_goal.publish(goal)

def callback(msg):
	global pub_speech
	if(msg.status.text=="Goal reached."):
		print("{} The robot has arrived to the {}".format(msg.status.text,place))
		loop = rospy.Rate(2)
		msg_speech.arg = "I have arrived to the " + place
		loop.sleep()
		pub_speech.publish(msg_speech)
	else:
		print(msg.status.text)


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
