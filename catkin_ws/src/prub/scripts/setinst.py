#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

goal = PoseStamped()

def callback(recog):
  global goal
  recog = str(recog.data)
  goal_pub = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=5)
   
  goal.header.seq = 1
  goal.header.frame_id = "map"
  goal.header.stamp = rospy.Time.now()
  goal.pose.position.z = 0.0
  goal.pose.orientation.x = 0.0
  goal.pose.orientation.y = 0.0
    
  if recog.find('KITCHEN') + 1:
    goal.pose.position.x = 7.42886325836
    goal.pose.position.y = 2.30235471725
    goal.pose.orientation.z = -0.0196151595322
    goal.pose.orientation.w = 0.99980760425
    
  elif recog.find('BEDROOM') + 1:
    goal.pose.position.x = 7.42886325836
    goal.pose.position.y = 4.00235471725
    goal.pose.orientation.z = 0.164005275233
    goal.pose.orientation.w = 0.98645946176
    
  elif recog.find('YARD') + 1:
    goal.pose.position.x = 3.37301754951
    goal.pose.position.y = 1.54060220718
    goal.pose.orientation.z = 0.0445461486044
    goal.pose.orientation.w = 0.99900732762
    
  elif recog.find('FORWARD') + 1:
    goal.pose.position.x = goal.pose.position.x + 0.1
    goal.pose.position.y = 0.0
    
  elif recog.find('BACK') + 1:
    goal.pose.position.x = goal.pose.position.x - 0.1
    goal.pose.position.y = 0.0
    
  elif recog.find('LEFT') + 1:
    goal.pose.position.x = 0.0
    goal.pose.position.y = goal.pose.position.x - 0.1
    
  elif recog.find('RIGHT') + 1:
    goal.pose.position.y = goal.pose.position.x + 0.1
  
  elif recog.find('START') + 1:
    goal_pub.publish(goal)
    
  elif recog.find('STOP') + 1:
    goal.pose.position.x = goal.pose.position.x - 0.01
    goal.pose.position.y = goal.pose.position.y - 0.01
    goal.pose.orientation.z = 0.0445461486044
    goal.pose.orientation.w = 0.99900732762
    goal_pub.publish(goal)

def main():

  rospy.init_node('setinst')
  
  rospy.Subscriber("recognized", String, callback)

  rospy.spin()

if __name__ == '__main__':
  main()
  
