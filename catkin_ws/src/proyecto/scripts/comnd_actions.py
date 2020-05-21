#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from geometry_msgs.msg import PoseStamped

def callback(data):
  command = data.data
  print command
  pub_goal = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=5)
  goal = PoseStamped()
  goal.header.frame_id = "map"
  if command == 'ROBOT GO TO POINT A':
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = -5.0
    goal.pose.position.y = 2.0
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    pub_goal.publish(goal)
  elif command == 'ROBOT GO TO POINT C':
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = 3.0
    goal.pose.position.y = 2.0
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    pub_goal.publish(goal)
  else:
    pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
    loop = rospy.Rate(2)
    msg_speech = SoundRequest()
    msg_speech.sound   = -3
    msg_speech.command = 1
    msg_speech.volume  = 1.0
    msg_speech.arg2    = "voice_us3_mbrola"
    if command == 'ROBOT SAY POTATO':
      msg_speech.arg = "POTATO POTATO"
    elif command == 'ROBOT SAY HELLO':
      msg_speech.arg = "HELLO"
    else:
      msg_speech.arg = ""
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
