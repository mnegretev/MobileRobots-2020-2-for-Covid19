#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseActionResult

def callback(msg):
	print('{}'.format(msg.status.text))

def main():
	rospy.init_node('prueba')
	rospy.Subscriber("/move_base/result" , MoveBaseActionResult , callback)
	rospy.spin()

if __name__ == '__main__':
	main()