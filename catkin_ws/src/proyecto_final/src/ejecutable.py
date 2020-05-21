#!/usr/bin/env python

import sys
import rospy
from sound_play.msg import SoundRequest
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalID

place = "goal"
pub_goal= rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=10)
pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
pub_cancel = rospy.Publisher("/move_base/cancel", GoalID, queue_size=10)
msg_speech = SoundRequest()
msg_speech.sound   = -3
msg_speech.command = 1
msg_speech.volume  = 1.0
msg_speech.arg2    = "voice_kal_diphone"

def callback_function(msg):
	global place
	global pub_goal
	global pub_vel
	loop = rospy.Rate(2)
	goal=PoseStamped()
	cancel_msg = GoalID()
	goal.pose.orientation.w=0.5
	goal.header.frame_id="map"
	x = msg.data.split(" ")

	try:
		voice=x[1]
		if(voice=='STOP'):
			place=x[1]
		else:
			place=x[2]
    	except:
		print("The phrase is not valid")

	print('goal: {}'.format(place))
	if(place=='EXIT'):
		goal.pose.position.x=8.10
		goal.pose.position.y=0.86
		pub_goal.publish(goal)
	elif(place=='KITCHEN'):
		goal.pose.position.x=2.0
		goal.pose.position.y=0.0
		pub_goal.publish(goal)
	elif(place=='LOUNGE'):
		goal.pose.position.x=5.04
		goal.pose.position.y=2.00
		pub_goal.publish(goal)
	elif(place=='STUDIO'):
		goal.pose.position.x=6.4	#	8.86
		goal.pose.position.y=6.42
		pub_goal.publish(goal)
	elif(place=='BATHROOM'):
		goal.pose.position.x=7.55
		goal.pose.position.y=3.9
		pub_goal.publish(goal)
	elif(place=='BEDROOM'):
		goal.pose.position.x=2.2	#	1.2
		goal.pose.position.y=4.8	#	6.86
		pub_goal.publish(goal)
	elif(place=='STOP'):
		cancel_msg.stamp.secs=0
		cancel_msg.stamp.nsecs=0
		cancel_msg.id=''
		pub_cancel.publish(cancel_msg)
	else:
		loop.sleep()

def callback(msg):
	global pub_speech
	if(msg.status.text=="Goal reached."):
		print("{} Now the robot is in the {}".format(msg.status.text,place))
		loop = rospy.Rate(2)
		msg_speech.arg = "Now I am in the " + place
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
