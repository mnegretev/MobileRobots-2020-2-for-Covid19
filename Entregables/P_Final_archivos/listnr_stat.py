#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseActionResult
from sound_play.msg import SoundRequest

def callback(data):
  pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)

  loop = rospy.Rate(2)

  msg_speech = SoundRequest()
  msg_speech.sound   = -3
  msg_speech.command = 1
  msg_speech.volume  = 1.0
  msg_speech.arg2    = "voice_us3_mbrola"

  if data.status.status == 3:
    msg_speech.arg = "Goal reached"
  elif data.status.status == 4:
    msg_speech.arg = "unable to complete"
  else:
    msg_speech.arg = "Something is wrong"
  loop.sleep()
 
def listener():
  # In ROS, nodes are uniquely named. If two nodes with the same
  # name are launched, the previous one is kicked off. The
  # anonymous=True flag means that rospy will choose a unique
  # name for our 'listener' node so that multiple listeners can
  # run simultaneously.
  rospy.init_node('listener', anonymous=True)

  rospy.Subscriber("move_base/result", MoveBaseActionResult, callback)

  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()

if __name__ == '__main__':
  listener()
