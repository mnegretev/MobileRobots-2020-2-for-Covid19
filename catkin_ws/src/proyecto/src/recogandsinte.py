#!/usr/bin/env python

import sys
import rospy
from sound_play.msg import SoundRequest
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseActionResult

place = ""

def callback_function(msg):
	global place 
	x = msg.data.split(" ")
	place = x[4]
	print(place)

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