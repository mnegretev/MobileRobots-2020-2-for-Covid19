#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import tf

global listener
global posX
global posY
global latestXGoal
global latestYGoal
global prevX
global prevY




def talker(x, y, z, saveAsLatestGoal):

    gs = rospy.Publisher("goalSet", String, queue_size=5)
    gs.publish(str(x) + "-" + str(y))

    if(saveAsLatestGoal):
        global prevX, prevY
        global latestXGoal, latestYGoal
        latestXGoal = x
        latestYGoal = y 
        prevX.append(x)
        prevX.append(y)


    goal_publisher = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=5)
    rate = rospy.Rate(10) # 10hz
    # while not rospy.is_shutdown():

    goal = PoseStamped()

    goal.header.seq = 1
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"

    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.position.z = z

    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0

    goal_publisher.publish(goal)

def continueToGoal():
    global latestXGoal, latestYGoal

    if(not latestXGoal == 0 and not latestYGoal == 0 ):
        talker(latestXGoal,latestYGoal,0, True)

def stop():
    global listener, posX, posY

    (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
    posX=trans[0]
    posY=trans[0]

    talker(posX,posY,0, False)

def switch(case):
   sw = {
      "GO TO KITCHEN": lambda : talker(8.84, 5.0, 0, True),
      "GO TO ENTRANCE": lambda :  talker(1, 0, 0, True),
      "GO TO ROOM": lambda :  talker(2.54, 4.46, 0, True),
      "GO TO SPACE": lambda :  talker(8.83, 0.964, 0, True),
      "RETURN": lambda :  talker(0, 0, 0, True),
      "CONTINUE": lambda :  continueToGoal(),
      "STOP": lambda :  stop()
   }
   sw.get(case, lambda : "ERROR: no action taken")()


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    string = data.data.replace('ROBOT ', '')
    switch(string)

def listener():

    global listener

    global prevX, prevY

    rospy.init_node('new_goal', anonymous=True)

    listener = tf.TransformListener()

    prevX = prevY = []

    rospy.Subscriber("recognized", String, callback)

    # spin() simply keeps python from exiting until this node is stopped



    rospy.spin()

if __name__ == '__main__':
    listener()



