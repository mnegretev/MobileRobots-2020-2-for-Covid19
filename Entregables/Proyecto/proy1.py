#!/usr/bin/env python

import sys
import rospy
from sound_play.msg import SoundRequest
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseActionResult


movsig = " "
pub_goal= rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=10)
pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
msg_speech = SoundRequest()
msg_speech.sound   = -3
msg_speech.command = 1
msg_speech.volume  = 1.0
msg_speech.arg2    = "voice_kal_diphone"

def callback_move_sig(msg):
	global movsig, pub_goal

	loop = rospy.Rate(2)
	goal=PoseStamped()

	goal.pose.orientation.w=0.5
	goal.header.frame_id="map"

	argg = msg.data.split(" ")
	movsig = argg[2]

	print('Destino: {}'.format(movsig))

	if(movsig=='EXIT'):
		goal.pose.position.x=8.50
		goal.pose.position.y=0.80
	elif(movsig=='BACK'):
		goal.pose.position.x=2.0
		goal.pose.position.y=1.0
	elif(movsig=='RIGHT'):
		goal.pose.position.x=3.56
		goal.pose.position.y=4.42
	elif(movsig=='CENTER'):
		goal.pose.position.x=5.00
		goal.pose.position.y=0.75
	else:
		loop.sleep()
	pub_goal.publish(goal)

def callback_answer(msg):
	global pub_speech
	if(msg.status.text=="Goal reached."):
		print("{} Objetivo alcanzado {}".format(msg.status.text,movsig))
		loop = rospy.Rate(2)
		msg_speech.arg = "Robot has reached destination " + movsig
		loop.sleep()
		pub_speech.publish(msg_speech)
	else:
		print(msg.status.text)


def main():
	print "...INITIALIZING SPEECH SYNTHESIS NODE..."
	print "Options: Robot move; CENTER, BACK, EXIT, RIGHT"
	print "Rivera Esquivel Jennifer E."
	rospy.init_node("speech_synthesize")
	rospy.Subscriber("/recognized",String, callback_move_sig)
	rospy.Subscriber("/move_base/result" , MoveBaseActionResult , callback_answer)
	rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass
