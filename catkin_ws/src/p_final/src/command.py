#!/usr/bin/env python
import rospy

from std_msgs.msg import String
from sound_play.msg import SoundRequest
from geometry_msgs.msg import PoseStamped

goal = PoseStamped()

def callback(data):
  global goal
  command = str(data.data)
  
  pub_goal = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=5)
  
  goal.header.frame_id = "map"
  
  if command.find('GO TO') != -1:
    
    if command.find('KITCHEN') != -1:
        goal.header.stamp = rospy.Time.now()
        goal.pose.position.x = 2.0
        goal.pose.position.y = 4.0
        goal.pose.position.z = 0.0
        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0  
        pub_goal.publish(goal)
    if command.find('BEDROOM') != -1:
        goal.header.stamp = rospy.Time.now()
        goal.pose.position.x = 8.2
        goal.pose.position.y = 5.0
        goal.pose.position.z = 0.0
        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0  
        pub_goal.publish(goal)
    if command.find('LIVING ROOM') != -1:
        goal.header.stamp = rospy.Time.now()
        goal.pose.position.x = 5.0
        goal.pose.position.y = 1.0
        goal.pose.position.z = 0.0
        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0  
        pub_goal.publish(goal)
    
    
  elif command.find('SAY HELLO') != -1:
    pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
    loop = rospy.Rate(2)
    msg_speech = SoundRequest()
    msg_speech.sound   = -3
    msg_speech.command = 1
    msg_speech.volume  = 1.0
    msg_speech.arg2    = "voice_us3_mbrola"
    msg_speech.arg = "HELLO I AM ROBOT"
    loop.sleep()
    pub_speech.publish(msg_speech)
  elif command.find('WHAT TIME IS IT') != -1:
    pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
    loop = rospy.Rate(2)
    msg_speech = SoundRequest()
    msg_speech.sound   = -3
    msg_speech.command = 1
    msg_speech.volume  = 1.0
    msg_speech.arg2    = "voice_us3_mbrola"
    msg_speech.arg = "THE TIME IS TWO FIFTEEN PM"
    loop.sleep()
    pub_speech.publish(msg_speech)
  else:
    pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
    loop = rospy.Rate(2)
    msg_speech = SoundRequest()
    msg_speech.sound   = -3
    msg_speech.command = 1
    msg_speech.volume  = 1.0
    msg_speech.arg2    = "voice_us3_mbrola"
    msg_speech.arg = "SAY A COMMAND"
    loop.sleep()
    pub_speech.publish(msg_speech)
 
def listener():
  # In ROS, nodes are uniquely named. If two nodes with the same
  # name are launched, the previous one is kicked off. The
  # anonymous=True flag means that rospy will choose a unique
  # name for our 'listener' node so that multiple listeners can
  # run simultaneously.
  rospy.init_node('command', anonymous=True)

  rospy.Subscriber("recognized", String, callback)

  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()

if __name__ == '__main__':
  listener()
