#!/usr/bin/python

import os

import rospy

from std_msgs.msg import String
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *




from geometry_msgs.msg import PoseStamped
from sound_play.msg import SoundRequest
from move_base_msgs.msg import MoveBaseActionResult


my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
class ASRTest(object):
    """Class to add jsgf grammar functionality."""
    def __init__(self):

        # Initializing publisher with buffer size of 10 messages
        self.pub_ = rospy.Publisher("recognized", String, queue_size=1)
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
                if os.path.isdir("/usr/local/lib/python3.6/dist-packages/pocketsphinx/model/"):
                    rospy.loginfo("Loading the default acoustic model")
                    self.hmm = "/usr/local/lib/python3.6/dist-packages/pocketsphinx/model/en-us/"
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



                    
                    pub_goal = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size = 1)
                    goal_msg = PoseStamped()
                    goal_msg.header.frame_id = 'map'
                    goal_msg.pose.orientation.w = 1.0

                    if recognized == "JUSTINA KITCHEN":
                        print("I am going to the kitchen")

                        goal_msg.pose.position.x = 2
                        goal_msg.pose.position.y = 4
                        pub_goal.publish(goal_msg)

                        del my_list1[:]
                        my_list1.append(True)

                        if len(my_list2) == 0:
                            pass
                        else:
                            my_list2[0] = False


                        if len(my_list3) == 0:
                            pass
                        else:
                            my_list3[0] = False


                        if len(my_list4) == 0:
                            pass
                        else:
                            my_list4[0] = False


                    else:
                        if recognized == "JUSTINA LIVINGROOM":
                            print("I am going to the livingroon")

                            goal_msg.pose.position.x = 2
                            goal_msg.pose.position.y = 1
                            pub_goal.publish(goal_msg)

                            del my_list2[:]
                            my_list2.append(True)

                            if len(my_list1) == 0:
                                pass
                            else:
                                my_list1[0] = False


                            if len(my_list3) == 0:
                                pass
                            else:
                                my_list3[0] = False


                            if len(my_list4) == 0:
                                pass
                            else:
                                my_list4[0] = False
                            


                        else:
                            if recognized == "JUSTINA GARDEN":
                                print("I am going to the garden")

                                goal_msg.pose.position.x = 6
                                goal_msg.pose.position.y = 4
                                pub_goal.publish(goal_msg)

                                del my_list3[:]
                                my_list3.append(True)

                                if len(my_list1) == 0:
                                    pass
                                else:
                                    my_list1[0] = False


                                if len(my_list2) == 0:
                                    pass
                                else:
                                    my_list2[0] = False


                                if len(my_list4) == 0:
                                    pass
                                else:
                                    my_list4[0] = False

                            else:
                                if recognized == "JUSTINA BATHROOM":
                                    print("I am going to the bathroom")    

                                    goal_msg.pose.position.x = 8
                                    goal_msg.pose.position.y = 1
                                    pub_goal.publish(goal_msg)

                                    del my_list4[:]
                                    my_list4.append(True)

                                    if len(my_list1) == 0:
                                        pass
                                    else:
                                        my_list1[0] = False


                                    if len(my_list2) == 0:
                                        pass
                                    else:
                                        my_list2[0] = False


                                    if len(my_list3) == 0:
                                        pass
                                    else:
                                        my_list3[0] = False



                    def arrive_goal_callback(arrived_msg):
                        #new_msg = MoveBaseActionResult()
                        
                        pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=1)
                        loop = rospy.Rate(10) ##original rospy.Rate(2), add more time to have a clear speech
                        msg_speech = SoundRequest()
                        msg_speech.sound   = -3
                        msg_speech.command = 1
                        msg_speech.volume  = 1.0
                        msg_speech.arg2    = "voice_en1_mbrola" #voice name

                        advise_msgs = arrived_msg.status.status




                        if len(my_list1) == 0:  #if lists is empty pass
                            pass
                        else:
                            if(my_list1[0] == True and advise_msgs == 3):
                                msg_speech.arg = "I have arrived to the kitchen"
                                loop.sleep()
                                pub_speech.publish(msg_speech)

                        if len(my_list2) == 0:  #if lists is empty pass
                            pass
                        else:
                            if(my_list2[0] == True and advise_msgs == 3):
                                
                                msg_speech.arg = "I have arrived to the living room"
                                loop.sleep()
                                pub_speech.publish(msg_speech)

                        if len(my_list3) == 0:  #if lists is empty pass
                            pass
                        else:
                            if(my_list3[0] == True and advise_msgs == 3):
                                
                                msg_speech.arg = "I have arrived to the garden"
                                loop.sleep()
                                pub_speech.publish(msg_speech)

                        if len(my_list4) == 0:  #if lists is empty pass
                            pass
                        else:
                            if(my_list4[0] == True and advise_msgs == 3):
                              
                                msg_speech.arg = "I have arrived to the bath room"
                                loop.sleep()
                                pub_speech.publish(msg_speech)




                        

                    rospy.Subscriber("/move_base/result", MoveBaseActionResult, arrive_goal_callback)





                self.decoder.start_utt()

    @staticmethod
    def shutdown():
        """This function is executed on node shutdown."""
        # command executed after Ctrl+C is pressed
        rospy.loginfo("Stop ASRControl")
        rospy.sleep(1)


if __name__ == "__main__":




    ASRTest()
