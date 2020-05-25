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
  msg_speech.volume  = 3.0
  msg_speech.arg2    = "voice_kal_diphone"

  if data.status.status == 3:
    msg_speech.arg = "task completed"
  elif data.status.status == 4:
    msg_speech.arg = "I can't do it"
  else:
    msg_speech.arg = "trying to do it"
  loop.sleep()
  print "Sending text to say: " + msg_speech.arg
  pub_speech.publish(msg_speech)
 
def listener():

  rospy.init_node('listener', anonymous=True)

  rospy.Subscriber("move_base/result", MoveBaseActionResult, callback)

  rospy.spin()

if __name__ == '__main__':
  listener()
