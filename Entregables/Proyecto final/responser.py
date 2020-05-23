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
  pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
  loop = rospy.Rate(2)
  msg_speech = SoundRequest()
  msg_speech.sound   = -3
  msg_speech.command = 1
  msg_speech.volume  = 1.0
  msg_speech.arg2    = "voice_kal_diphone"
    
  if command == 'ROBOT GO TO KITCHEN' or command == 'ROBOT GO TO THE KITCHEN' or command == 'GO TO THE KITCHEN' or command == 'GO TO THE KITCHEN':
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = 2.0
    goal.pose.position.y = 2.0
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    pub_goal.publish(goal)
  elif command == 'ROBOT GO TO YARD' or command == 'ROBOT GO TO THE YARD' or command == 'GO TO THE YARD' or command == 'GO TO THE YARD':
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = 1.0
    goal.pose.position.y = 1.0
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    pub_goal.publish(goal)
  elif command == 'ROBOT GO TO BEDROOM' or command == 'ROBOT GO TO THE BEDROOM':
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = 1.0
    goal.pose.position.y = 4.0
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    pub_goal.publish(goal)
  else:
    if command == 'ROBOT SAY YES' or command == 'SAY YES':
      msg_speech.arg = "YES"
    if command == 'ROBOT SAY NO' or command == 'SAY NO':
      msg_speech.arg = "NO"
    elif command == 'ROBOT SCREAM' or command == 'SCREAM':
      msg_speech.arg = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    elif command == 'ROBOT LAUGH' or command == 'LAUGH':
      msg_speech.arg = "HAHAHAHAH"
    elif command == 'ROBOT STOP' or command == 'STOP':
      msg_speech.arg = "STOPING"
    elif command == 'ROBOT START' or command == 'START':
      msg_speech.arg = "STARTING"
    elif command == 'ROBOT SAY HELLO' or command == 'SAY HELLO':
      msg_speech.arg = "HELLO WORLD HAPPY FACE"
    elif command == 'ROBOT SAY GOODBYE' or command == 'SAY GOODBYE':
      msg_speech.arg = "GOODBYE WORLD SAD FACE"
    elif command == 'ROBOT TELL A JOKE' or command == 'TELL A JOKE':
      msg_speech.arg = "I DO NOT KNOW ANY JOKES"
    elif command == 'ROBOT GO TO KITCHEN' or command == 'ROBOT GO TO THE KITCHEN' or command == 'GO TO THE KITCHEN' or command == 'GO TO THE KITCHEN':
      msg_speech.arg = "GOING"
      goal.header.stamp = rospy.Time.now()
      goal.pose.position.x = 1.5
      goal.pose.position.y = 1.5
      goal.pose.position.z = 0.0
      goal.pose.orientation.x = 0.0
      goal.pose.orientation.y = 0.0
      goal.pose.orientation.z = 0.0
      goal.pose.orientation.w = 1.0
      pub_goal.publish(goal)
    elif command == 'ROBOT GO TO YARD' or command == 'ROBOT GO TO THE YARD' or command == 'GO TO THE YARD' or command == 'GO TO THE YARD':
      msg_speech.arg = "GOING"
      goal.header.stamp = rospy.Time.now()
      goal.pose.position.x = 1.0
      goal.pose.position.y = 1.0
      goal.pose.position.z = 0.0
      goal.pose.orientation.x = 0.0
      goal.pose.orientation.y = 0.0
      goal.pose.orientation.z = 0.0
      goal.pose.orientation.w = 1.0
      pub_goal.publish(goal)
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
