#!/usr/bin/env python

import sys
import rospy
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped
from sound_play.msg import SoundRequest
from std_msgs.msg import String
from actionlib_msgs.msg import GoalID



goal_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)
calcel_pub = rospy.Publisher("/move_base/cancel", GoalID, queue_size=1)
speech_pub = rospy.Publisher("/robotsound", SoundRequest, queue_size=1)
final_goal = ""

msg_speech = SoundRequest()
msg_speech.sound   = -3
msg_speech.command = 1
msg_speech.volume  = 1.0
msg_speech.arg2    = "voice_kal_diphone"

def move(msg):
    global final_goal
    global goal_pub
    loop = rospy.Rate(2)
    goal_aux =PoseStamped()
    cancel = GoalID()
    goal_aux.pose.orientation.w=0.5
    goal_aux.header.frame_id="map"
    vocab_String = msg.data.split()

    
    voice = vocab_String[1]
    if(voice =='STOP'):
	final_goal=vocab_String[1]
    else:
	final_goal=vocab_String[3]
    
    

    if(final_goal=='GARDEN'):
        goal_aux.pose.position.x=7.00
        goal_aux.pose.position.y=0.50
 	goal_pub.publish(goal_aux)
    elif(final_goal=='WINDOW'):
	goal_aux.pose.position.x=8.00
	goal_aux.pose.position.y=3.00
	goal_pub.publish(goal_aux)
    elif(final_goal=='DOOR'):
	goal_aux.pose.position.x=0.00
	goal_aux.pose.position.y=0.00
	goal_pub.publish(goal_aux)
    elif(final_goal=='BATHROOM'):
	goal_aux.pose.position.x=3.00
	goal_aux.pose.position.y=5.00
	goal_pub.publish(goal_aux)
    elif(final_goal=='STOP'):
	cancel.stamp.secs=0
	cancel.stamp.nsecs=0
	cancel.id=''
	calcel_pub.publish(cancel)		
    else:
		loop.sleep()
  

def speech(msg):
    global speech_pub
    if(msg.status.text=="Goal reached."):
		print("The robot has arrived")
		loop = rospy.Rate(2)
		msg_speech.arg = "I am here"
		loop.sleep()
		speech_pub.publish(msg_speech)
    else:
		print(msg.status.text)
        
        
def main():
	print "INITIALIZING SPEECH SYNTHESIS NODE..."
	rospy.init_node("speech_synthesize")
	rospy.Subscriber("/recognized",String, move)
	rospy.Subscriber("/move_base/result" , MoveBaseActionResult , speech)
	rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
