#!/usr/bin/python

import os

import rospy

# Move
# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Voice recognition
from std_msgs.msg import String
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

# Voice synthesis
from sound_play.msg import SoundRequest

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
        print "ROBOT SAY: " + text_to_say
        pub_speech.publish(msg_speech)

class MoveToPoint(object):

    def __init__(self, point):
        # Creamos el cliente
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        client.wait_for_server()
        imDone = ""

        # Definimos los puntos
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        if point == 0:  # OUTSIDE
            goal.target_pose.pose.position.x = 0.0
            goal.target_pose.pose.position.y = 0.0
            goal.target_pose.pose.orientation.w = 1.0
            imDone = "I'M OUTSIDE"
        elif point == 1: # Room 1
            goal.target_pose.pose.position.x = 1.5
            goal.target_pose.pose.position.y = 2.5
            goal.target_pose.pose.orientation.w = 1.0
            imDone = "I'M IN THE ROOM ONE"
        elif point == 2: # Room 2
            goal.target_pose.pose.position.x = 4.0
            goal.target_pose.pose.position.y = 3.5
            goal.target_pose.pose.orientation.w = 1.0
            imDone = "I'M IN THE ROOM TWO"
        elif point == 3: # Room 3
            goal.target_pose.pose.position.x = 7.0
            goal.target_pose.pose.position.y = 2.5
            goal.target_pose.pose.orientation.w = 1.0
            imDone = "I'M IN THE ROOM THREE"
        elif point == 4: # Room 4
            goal.target_pose.pose.position.x = 3.0
            goal.target_pose.pose.position.y = 1.0
            goal.target_pose.pose.orientation.w = 1.0
            imDone = "I'M IN THE ROOM FOUR"

        # Nos movemos
        client.send_goal(goal)

        wait = client.wait_for_result()

        if not wait:
            # Indicamos que algo ha pasado
            SaySomethingRobot("HELP ME PLEASE, I'M STUCK HERE")
            rospy.logerr("ACTION SERVER IS NOT AVAILABLE")
            rospy.signal_shutdown("ACTION SERVER IS NOT AVAILABLE")
        else:
            # Indicamos que hemos llegado al punto
            rospy.loginfo(imDone)
            SaySomethingRobot(imDone)

class GetCommand(object):
    def __init__(self, command):

        #Mostramos el texto recibido
        print "DETECTED COMMAND: " + command

        # Verificamos si es un movimiento de robot
        if "MOVE" in command:
            # Determinamos a donde movernos
            if "ONE" in command:
                # Hacemos que el robot indique se va a mover
                SaySomethingRobot("MOVING TO ROOM ONE")
                # Nos movemos a un punto
                MoveToPoint(1)
            elif "TWO" in command:
                # Hacemos que el robot indique se va a mover
                SaySomethingRobot("MOVING TO ROOM TWO")
                # Nos movemos a un punto
                MoveToPoint(2)
            elif "THREE" in command:
                # Hacemos que el robot indique se va a mover
                SaySomethingRobot("MOVING TO ROOM THREE")
                # Nos movemos a un punto
                MoveToPoint(3)
            elif "FOUR" in command:
                # Hacemos que el robot indique se va a mover
                SaySomethingRobot("MOVING TO ROOM FOUR")
                # Nos movemos a un punto
                MoveToPoint(4)
            elif "OUTSIDE" in command:
                SaySomethingRobot("MOVING OUTSIDE")
                # Nos movemos a un punto
                MoveToPoint(0)
        # Verificamos otras instruccions
        elif "STOP" in command:
            SaySomethingRobot("NO, NOTHING CAN'T STOP ME")
        elif "DANCE" in command:
            SaySomethingRobot("SORRY BUT I DON'T KNOW HOW TO DANCE YET")


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
                    # Vamos a reconocer el comando
                    GetCommand(recognized)
                else :
                    # Indiquemos que no sabemos que dice el usuario
                    notRecognized = "SORRY BUT I DON'T UNDERSTAND YOU"
                    rospy.loginfo('OUTPUT: \"' + notRecognized + '\"')
                    SaySomethingRobot(notRecognized)
                self.decoder.start_utt()

    @staticmethod
    def shutdown():
        """This function is executed on node shutdown."""
        # command executed after Ctrl+C is pressed
        rospy.loginfo("Stop ASRControl")
        rospy.sleep(1)


if __name__ == "__main__":
    ASRTest()
