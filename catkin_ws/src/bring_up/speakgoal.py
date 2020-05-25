#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest

pub = rospy.Publisher('robotsound', SoundRequest, queue_size = 10)

def callback(data):

	if data.data == "goal reached":
		loop = rospy.Rate(2)
		msg_speech = SoundRequest()
		msg_speech.sound   = -3
		msg_speech.command = 1
		msg_speech.volume  = 1.0
		msg_speech.arg2    = "voice_el_diphone"
		msg_speech.arg = "llegue a mi destino exitosamente"

		loop.sleep()
		print "Sending text to say: " + "llegue a mi destino exitosamente"
		pub.publish(msg_speech)


def controller():
	rospy.init_node('speakgoal', anonymous = True)

	rospy.Subscriber("theReacher", String, callback)

	rospy.spin()


if __name__ == '__main__':
	print "INITIALIZING SPEECH SYNTHESIS TEST..."
	controller()