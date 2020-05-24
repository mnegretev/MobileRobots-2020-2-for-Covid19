#!/usr/bin/python

import os

import sys

import rospy
import rospy
import tf


import actionlib



from std_msgs.msg import String
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from sound_play.msg import SoundRequest
from std_msgs.msg import Float32MultiArray 
import time 
NAME = "gutierrez_martinez"
#---

class SaySomethingRobot(object):

    def __init__(self, text_to_say):
        # rospy.init_node("speech_syn")
        pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
        loop = rospy.Rate(2)

        msg_speech = SoundRequest()
        # Indicamos que se va a reproducir un texto una sola vez
        msg_speech.sound   = -3
        msg_speech.command = 1
        msg_speech.volume  = 1.0
        # Indicamos la voz
        msg_speech.arg2    = "voice_kal_diphone"
        #self.msg_speech.arg2    = "voice_en1_mbrola"
        #self.msg_speech.arg2    = "voice_us1_mbrola"

        # Indicamos el mensaje
        msg_speech.arg = text_to_say

        loop.sleep()
        print "ROBOT: " + text_to_say
        pub_speech.publish(msg_speech)
#---

def get_robot_pose(listener):
    try:
        (trans, rot) = listener.lookupTransform('odom', 'base_link', rospy.Time(0))
        robot_x = trans[0]
        robot_y = trans[1]
        robot_a = 2*math.atan2(rot[2], rot[3])
        if robot_a > math.pi:
            robot_a -= 2*math.pi
        return robot_x, robot_y, robot_a
    except:
        pass
    return None

class Mover(object):
    def __init__(self, point):
      print "PROYECTO FINAL - " + NAME
      rospy.init_node("")
      pub_speeds = rospy.Publisher("/rotombot/hardware/motor_speeds", Float32MultiArray, queue_size=10)
      loop = rospy.Rate(20)
      listener = tf.TransformListener()
      client.wait_for_server()
      imDone = ""
      while not rospy.is_shutdown():
      
      		if point == 0:  
                      time.sleep(1)
                      msg= Float32MultiArray()
           	      msg.data=[0.6, 0.6]
            	      pub_speeds.publish(msg)
            	      time.sleep(3)
            	      imDone = "Advance"
            	      loop.sleep()
      		if point == 1: 
        #vuelta a la derecha
	    	      msg.data=[0.8, -0.8]
            	      pub_speeds.publish(msg)
	              time.sleep(.50)
                      imDone = "turn right"
                      loop.sleep()
      		if point == 2: 
        #vuelta a la izquierda
		     msg.data=[-0.8, 0.8]
       		     pub_speeds.publish(msg)
		     time.sleep(.50)
         	     imDone = "turn left"
         	     loop.sleep()
       		if point == 3:
        #detener
	             msg.data=[0.0, 0.0]
        	     pub_speeds.publish(msg)
		     time.sleep(.5)
         	     imDone = "Advance"
         	     loop.sleep()
        
        

#---
class GetCommand(object):
    def __init__(self, command):

     
        print "COMANDO: " + command

      
        if "ADVANCED" in command:
                 SaySomethingRobot("ADVANCED")
                 Mover(0)
           
        if "RIGHT" in command:
               
                SaySomethingRobot("TURN RIGHT")
       
                MoverPoint(1)
        if "LEFT" in command:
           
                SaySomethingRobot("TURN LEFT")
             
                Mover(2)
                
        if "STOP" in command:
                SaySomethingRobot("STOP PLEASE")
                Mover(3)
          


class ASRTest(object):
    """Class to add jsgf grammar functionality."""

    def __init__(self):

        # Initializing publisher with buffer size of 10 messages
        self.pub_ = rospy.Publisher("recognized", String, queue_size=10)
        # initialize node
        rospy.init_node("asr_control")
        # Call custom function on node shutdown
        rospy.on_shutdown(self.shutdown)

        # Params

        # File containing language model
        _lm_param = "~lm"
        # Dictionary
        _dict_param = "~dict"
        # Hidden markov model. Default has been provided below
        _hmm_param = "~hmm"
        # Gram file contains the rules and grammar
        _gram = "~gram"
        # Name of rule within the grammar
        _rule = "~rule"

        _grammar = "~grammar"

        # check if lm or grammar mode. Default = grammar
        self._use_lm = 0

        self.in_speech_bf = False

        # Setting param values
        if rospy.has_param(_hmm_param):
            self.hmm = rospy.get_param(_hmm_param)
            if rospy.get_param(_hmm_param) == ":default":
                if os.path.isdir("/usr/local/lib/python2.7/dist-packages/pocketsphinx/model/"):
                    rospy.loginfo("Loading the default acoustic model")
                    self.hmm = "/usr/local/lib/python2.7/dist-packages/pocketsphinx/model/en-us/"
                    rospy.loginfo("Done loading the default acoustic model")
                else:
                    rospy.logerr(
                        "No language model specified. Couldn't find default model.")
                    return
        else:
            rospy.logerr(
                "No language model specified. Couldn't find default model.")
            return

        if rospy.has_param(_dict_param) and rospy.get_param(_dict_param) != ":default":
            self.dict = rospy.get_param(_dict_param)
        else:
            rospy.logerr(
                "No dictionary found. Please add an appropriate dictionary argument.")
            return

        if rospy.has_param(_grammar) and rospy.get_param(_grammar) != ":default":
            pass
        else:
            rospy.logerr(
                "No grammar found. Please add an appropriate grammar along with gram file.")
            return

        if rospy.has_param(_lm_param) and rospy.get_param(_lm_param) != ':default':
            self._use_lm = 1
            self.class_lm = rospy.get_param(_lm_param)
        elif rospy.has_param(_gram) and rospy.has_param(_rule):
            self._use_lm = 0
            self.gram = rospy.get_param(_gram)
            self.rule = rospy.get_param(_rule)
        else:
            rospy.logerr(
                "Couldn't find suitable parameters. Please take a look at the documentation")
            return

        # All params satisfied. Starting recognizer
        self.start_recognizer()

    def start_recognizer(self):
        """Function to handle lm or grammar processing of audio."""
        config = Decoder.default_config()
        rospy.loginfo("Done initializing pocketsphinx")

        # Setting configuration of decoder using provided params
        config.set_string('-hmm', self.hmm)
        config.set_string('-dict', self.dict)

        # Check if language model to be used or grammar mode
        if self._use_lm:
            rospy.loginfo('Language Model Found.')
            config.set_string('-lm', self.class_lm)
            self.decoder = Decoder(config)
        else:
            rospy.loginfo(
                'language model not found. Using JSGF grammar instead.')
            self.decoder = Decoder(config)

            # Switch to JSGF grammar
            jsgf = Jsgf(self.gram + '.gram')
            rule = jsgf.get_rule(rospy.get_param('~grammar') + '.' + self.rule)
            # Using finite state grammar as mentioned in the rule
            rospy.loginfo(rospy.get_param('~grammar') + '.' + self.rule)
            fsg = jsgf.build_fsg(rule, self.decoder.get_logmath(), 7.5)
            rospy.loginfo("Writing fsg to " +
                          self.gram + '.fsg')
            fsg.writefile(self.gram + '.fsg')

            self.decoder.set_fsg(self.gram, fsg)
            self.decoder.set_search(self.gram)

        # Start processing input audio
        self.decoder.start_utt()
        rospy.loginfo("Decoder started successfully")

        # Subscribe to audio topic
        rospy.Subscriber("jsgf_audio", String, self.process_audio)
        rospy.spin()

    def process_audio(self, data):
        """Audio processing based on decoder config."""
        # Check if input audio has ended
        self.decoder.process_raw(data.data, False, False)
        if self.decoder.get_in_speech() != self.in_speech_bf:
            self.in_speech_bf = self.decoder.get_in_speech()
            if not self.in_speech_bf:
                self.decoder.end_utt()
                if self.decoder.hyp() != None:
                    recognized = self.decoder.hyp().hypstr
                    rospy.loginfo('OUTPUT: \"' + recognized + '\"')
                    self.pub_.publish(recognized)
                    GetCommand(recognized)
                self.decoder.start_utt()
                 

    @staticmethod
    def shutdown():
        """This function is executed on node shutdown."""
        # command executed after Ctrl+C is pressed
        rospy.loginfo("Stop ASRControl")
        rospy.sleep(1)


if __name__ == "__main__":
    ASRTest()
