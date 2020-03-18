#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32
from std_msgs.msg import Bool
from geometry_msgs.msg import TransformStamped
from sensor_msgs.msg import JointState
import tf

def callbackPosHead(msg):
    ### Set GoalPosition
    global goalPan
    global goalTilt
    goalPan = msg.data[0]
    goalTilt = msg.data[1]

def main():
    print "INITIALIZING HEAD NODE ..."
    rospy.init_node("head")
    subPosition = rospy.Subscriber("head/goal_pose", Float32MultiArray, callbackPosHead)
    
    br = tf.TransformBroadcaster()
    jointStates = JointState()
    jointStates.name = ["pan_connect", "tilt_connect"]
    jointStates.position = [0 ,0]
    pubJointStates = rospy.Publisher("/joint_states", JointState, queue_size = 1)

    loop = rospy.Rate(10)

    loop = rospy.Rate(30)

    global goalPan
    global goalTilt
    goalPan = 0
    goalTilt = 0
    pan = 0
    tilt = 0
    speedPan = 0.1 
    speedTilt = 0.1
    while not rospy.is_shutdown():
        deltaPan = goalPan - pan
        deltaTilt = goalTilt - tilt
        if deltaPan > speedPan:
            deltaPan = speedPan
        if deltaPan < -speedPan:
            deltaPan = -speedPan
        if deltaTilt > speedTilt:
            deltaTilt = speedTilt
        if deltaTilt < -speedTilt:
            deltaTilt = -speedTilt
        pan += deltaPan
        tilt += deltaTilt
        jointStates.header.stamp = rospy.Time.now()
        jointStates.position[0] = pan
        jointStates.position[1] = -tilt #A tilt > 0 goes upwards, but to keep a dextereous system, positive tilt should go downwards
        pubJointStates.publish(jointStates)
        loop.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
