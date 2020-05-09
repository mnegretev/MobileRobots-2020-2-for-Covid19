#!/usr/bin/env python

import sys
import rospy
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped
from sound_play.msg import SoundRequest
from std_msgs.msg import String
from actionlib_msgs.msg import GoalID


location = ""
pub_goal = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)
pub_cancel = rospy.Publisher("/move_base/cancel", GoalID, queue_size=10)
pub_speech = rospy.Publisher("/robotsound", SoundRequest, queue_size=10)

#Using speech script
msg_speech = SoundRequest()
msg_speech.sound   = -3
msg_speech.command = 1
msg_speech.volume  = 1.0
msg_speech.arg2    = "voice_en1_mbrola"

def move_callback(msg):
    global location
    global pub_goal
    global pub_vel
    loop = rospy.Rate(2)
    goal =PoseStamped()
    cancel_msg = GoalID()
    goal.pose.orientation.w=0.5
    goal.header.frame_id="map"
    vocab_String = msg.data.split()

    try:
	voice_raw = vocab_String[1]
	if(voice_raw =='STOP'):
		location=vocab_String[1]
	else:
		location=vocab_String[2]
    except:
	print("The phrase is not valid")
    

    if(location=='KITCHEN'):
        goal.pose.position.x=8.50
        goal.pose.position.y=0.00
 	pub_goal.publish(goal)
    elif(location=='BEDROOM'):
	goal.pose.position.x=3.00
	goal.pose.position.y=4.00
	pub_goal.publish(goal)
    elif(location=='OUTSIDE'):
	goal.pose.position.x=-0.50
	goal.pose.position.y=0.00
	pub_goal.publish(goal)
    elif(location=='GARDEN'):
	goal.pose.position.x=8.00
	goal.pose.position.y=6.00
	pub_goal.publish(goal)
    elif(location=='STOP'):
	cancel_msg.stamp.secs=0
	cancel_msg.stamp.nsecs=0
	cancel_msg.id=''
	pub_cancel.publish(cancel_msg)		
    else:
		loop.sleep()
  

def speech_callback(msg):
    global pub_speech
    if(msg.status.text=="Goal reached."):
		print("{} I am in the {}".format(msg.status.text,location))
		loop = rospy.Rate(2)
		msg_speech.arg = "I am in the " + location + " Rocova"
		loop.sleep()
		pub_speech.publish(msg_speech)
    else:
		print(msg.status.text)
        
        
def main():
	print "INITIALIZING SPEECH SYNTHESIS NODE..."
	rospy.init_node("speech_synthesize")
	rospy.Subscriber("/recognized",String, move_callback)
	rospy.Subscriber("/move_base/result" , MoveBaseActionResult , speech_callback)
	rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
