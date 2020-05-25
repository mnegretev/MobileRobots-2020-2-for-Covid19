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
  if command == 'GO TO THE KITCHEN':
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = 4.0
    goal.pose.position.y = 1.0
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    pub_goal.publish(goal)
  elif command == 'GO TO THE LIVING ROOM':
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = 3.0
    goal.pose.position.y = 0.0
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    pub_goal.publish(goal)
  elif command == 'STOP':
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = goal.pose.position.x
    goal.pose.position.y = goal.pose.position.y
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = goal.pose.orientation.x
    goal.pose.orientation.y = goal.pose.orientation.y
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    pub_goal.publish(goal)
  else:
    pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
    loop = rospy.Rate(2)
    msg_speech = SoundRequest()
    msg_speech.sound   = -3
    msg_speech.command = 1
    msg_speech.volume  = 3.0
    msg_speech.arg2    = "voice_kal_diphone"
    if command == 'HOW ARE YOU':
      msg_speech.arg = "GOOD"
    loop.sleep()
    pub_speech.publish(msg_speech)
 
def listener():

  rospy.init_node('command', anonymous=True)

  rospy.Subscriber("recognized", String, callback)

  rospy.spin()

if __name__ == '__main__':
  listener()
