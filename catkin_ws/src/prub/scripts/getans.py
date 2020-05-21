#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseActionResult
from sound_play.msg import SoundRequest

def callback(data):
  pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)

  loop = rospy.Rate(1)

  msg_speech = SoundRequest()
  msg_speech.sound   = -3
  msg_speech.command = 1
  msg_speech.volume  = 1.0
  msg_speech.arg2    = "voice_us2_mbrola"

  if data.status.status == 2:
    msg_speech.arg = ""
  if data.status.status == 3:
    msg_speech.arg = "Goal reached"
  elif data.status.status == 4:
    msg_speech.arg = "I can't do it"
    
  loop.sleep()
  
  pub_speech.publish(msg_speech)
 
def main():

  rospy.init_node('getans')

  rospy.Subscriber("move_base/result", MoveBaseActionResult, callback)

  rospy.spin()

if __name__ == '__main__':
  main()
  
