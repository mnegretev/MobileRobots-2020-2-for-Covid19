#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String
import tf
from sound_play.msg import SoundRequest

global listener
global flag




def callback(data):
    global flag

    pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)

    loop = rospy.Rate(2)

    msg_speech = SoundRequest()
    msg_speech.sound   = -3
    msg_speech.command = 1
    msg_speech.volume  = 1.0
    msg_speech.arg2    = "voice_don_diphone"
    msg_speech.arg = "Ok, I'll go"

    loop.sleep()

    pub_speech.publish(msg_speech)

    flag = False

    rospy.loginfo(rospy.get_caller_id() + " New GOAL I heard %s", data.data)
    [x, y] = str(data.data).split('-')

    loop = rospy.Rate(2)

    loop.sleep()

    flag = True
    while flag:
        loop.sleep()
        (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
        posX=trans[0]
        posY=trans[1]
        print "Current POS = " +str(posX) + ", " +str(posY)
        print float(x)-posX
        print float(y)-posY
        if((-0.5 < (float(x)-posX) < 0.5)):
            if(-0.5 < (float(y)-posY) < 0.5):
                print "DONE!"
                flag = False
        
        

    

    loop = rospy.Rate(2)

    msg_speech = SoundRequest()
    msg_speech.sound   = -3
    msg_speech.command = 1
    msg_speech.volume  = 1.0
    msg_speech.arg2    = "voice_don_diphone"
    msg_speech.arg = "GOAL, REACHED"

    loop.sleep()

    pub_speech.publish(msg_speech)

def listener():

    global listener

    global prevX, prevY

    rospy.init_node('goal_reached', anonymous=True)

    listener = tf.TransformListener()

    rospy.Subscriber("goalSet", String, callback)



    rospy.spin()

if __name__ == '__main__':
    listener()
