#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32
from std_msgs.msg import Bool
from geometry_msgs.msg import TransformStamped
from sensor_msgs.msg import JointState
import tf

def callbackPos(msg):
    global goalAngles
    goalAngles = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(msg.data)):
        goalAngles[i] = msg.data[i]
    
def callbackGripper(msg):
    global goalGripper
    goalGripper = msg.data


def main():
    print "INITIALIZING LEFT ARM NODE ..."
    rospy.init_node("left_arm")
    subPos     = rospy.Subscriber("/la_goal_pose",    Float32MultiArray, callbackPos)
    subGripper = rospy.Subscriber("/la_goal_gripper", Float32,           callbackGripper)
    
    br = tf.TransformBroadcaster()
    jointStates = JointState()
    jointStates.name = ["la_1_joint", "la_2_joint", "la_3_joint", "la_4_joint", "la_5_joint", "la_6_joint", "la_7_joint", "la_grip_left", "la_grip_right"]
    jointStates.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    pubJointStates = rospy.Publisher("/joint_states", JointState, queue_size = 1)

    loop = rospy.Rate(10)

    global goalAngles;
    global goalGripper
    goalAngles = [0, 0, 0, 0, 0, 0, 0]
    angles = [0, 0, 0, 0, 0, 0, 0]
    speeds = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    goalGripper = 0
    gripper = 0
    gripperSpeed = 0.1
    deltaAngles = [0, 0, 0, 0, 0, 0, 0]
    deltaGripper = 0
    while not rospy.is_shutdown():
        for i in range(len(deltaAngles)):
            deltaAngles[i] = goalAngles[i] - angles[i]
            if deltaAngles[i] > speeds[i]:
                deltaAngles[i] = speeds[i]
            if deltaAngles[i] < -speeds[i]:
                deltaAngles[i] = -speeds[i]
            angles[i] += deltaAngles[i]
            jointStates.position[i] = angles[i]
            

        deltaGripper = goalGripper - gripper
        if deltaGripper > gripperSpeed:
            deltaGripper = gripperSpeed
        if deltaGripper < -gripperSpeed:
            deltaGripper = -gripperSpeed
        gripper += deltaGripper
        jointStates.position[7] = gripper
        jointStates.position[8] = gripper
        
        jointStates.header.stamp = rospy.Time.now()
        pubJointStates.publish(jointStates)
        loop.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
