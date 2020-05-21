#!/usr/bin/env python

#Este codigo requiere tener instalado la voz voice_upc_ca_ona_hts, y pocketsphinx para python

from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
import sys
import rospy
from sound_play.msg import SoundRequest
import os
from pocketsphinx import LiveSpeech, get_model_path


def move(x,y,lugar):
    say("Moviendo a " + lugar)
    print("Moviendo a " + lugar)
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
	say("Llegue a " + lugar)
	print("Llegue a "+ lugar)
        return client.get_result()

def say(text_to_say):
    rospy.init_node("speech_syn")
    pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
    loop = rospy.Rate(2)

    msg_speech = SoundRequest()
    msg_speech.sound   = -3
    msg_speech.command = 1
    msg_speech.volume  = 1.0
    msg_speech.arg2    = "voice_upc_ca_ona_hts"
    msg_speech.arg = text_to_say

    loop.sleep()
    #print "Sending text to say: " + text_to_say
    pub_speech.publish(msg_speech)


def main():
     mover = False
     lugar = "la entrada"
     say("Iniciando Servicio")
     print("**** Iniciando Servicio ****")
     print("...Cargando...")
     #iniciador del LiveSpeech
     model_path = get_model_path()
     speech = LiveSpeech(
	verbose=False,
	sampling_rate=16000,
	buffer_size=2048,
	no_search=False,
	full_utt=False,
	hmm= os.path.join(model_path, 'es-es'),
	lm= os.path.join(model_path, 'es-20k.lm.bin'),
	dict= os.path.join(model_path, 'es.dict')
     )

     say("Diga su comando")
     print("...Diga su comando...")
     for phrase in speech:
      frase = str(phrase)
      #print frase
      if mover == True:
	if frase=="sala":
		lugar = "la sala"
		move(8.5,1.0,"la sala")
		print
		print("...Diga su comando...")
		mover = False
	elif frase=="cocina":
		lugar = "la cocina"
		move(9.0,4.0,"la cocina")
		print
		print("...Diga su comando...")
		mover = False
	elif frase=="cuarto":
		lugar = " cuarto"
		move(2.5,4.0,"el cuarto")
		print
		print("...Diga su comando...")
		mover = False
	elif frase=="entrada":
		lugar = "la entrada"
		move(2.0,1.0,"la entrada")
		print
		print("...Diga su comando...")
		mover = False
	#else:
		#print("No reconoci el lugar, intente de nuevo")
		#say("No reconoci el lugar, intente de nuevo")
      else:
	if frase == "mover":
		say("A donde quiere mover")
		mover = True
		print("...Diga el lugar...")
	elif frase == "opciones":
		say("Estas son las opciones")
		print("Estas son las opciones:")
		print("* Mover...")
		print(" - Sala")
		print(" - Entrada")
		print(" - Cocina")
		print(" - Cuarto")
		print("* Lugar - Para saber la ubicacion del robot")
		print("* Acabar - Para finalizar el programa")
		print
		print("...Diga su comando...")
	elif frase == "lugar":
		say("Se ubica en " + lugar)
		print("Se ubica en " + lugar)
		print
		print("...Diga su comando...")
	elif frase == "acabar":
		print("...Acabando Servicio...")
		break

if __name__ == "__main__":
    main()



