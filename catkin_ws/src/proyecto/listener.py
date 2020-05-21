#!/usr/bin/env python

import rospy
from std_msgs.msg import MoveBaseActionResult
from sound_play.msg import SoundRequest

def callback(data):

	pub_speech = rospy.Publisher("robotsound",SoundRequest,queue_size=10)
	loop=rospy.Rate(2)

	msg_speech = SoundRequest()
	msg_speech.sound = -3
	msg_speech.command = 1
	msg_speech.volume = 1.0
	msg_speech.arg2 = "voice_rab_diphone"

	if data.status.status == 3:
		msg_speech.arg = "Goal Reached"

	elif data.status.status == 4:
		msg_speech.arg = "I can not do it"

	else:
		msg_speech.arg = "Something is wrong"

	loop.sleep()

	print "Sending text to say: " + msg_speech.arg
	pub_speech.publish(msg_speech)

def listener():

	rospy.init_node('listener',anonymous=True)
	rospy.Suscriber("move_base/result",MoveBaseActionResult,callback)

	rospy.spin()


if __name__ == '__main__':
	listener()
