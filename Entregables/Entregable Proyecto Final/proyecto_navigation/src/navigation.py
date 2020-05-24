#!/usr/bin/env python
import actionlib
import sys
import rospy
import os
from sound_play.msg import SoundRequest
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from pocketsphinx import LiveSpeech, get_model_path

def main():
     mover = False
     comenzar= False
     hablar("Bienvenido  Cargando servicio")
     print("Bienvenido! Cargando servicio...")

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

     hablar("Listo!")
     print("Listo! Para iniciar el servicio, diga: comenzar")
     for phrase in speech:
      frase = str(phrase)
      #print ("Se escucho: "+ frase)
      if comenzar == True:
	if frase=="al patio":
		hablar("Moviendo al patio")
    		print("Moviendo al patio")
		avanzar(-3.0,0.0)
	elif frase=="al pasillo":
		hablar("Moviendo al pasillo")
    		print("Moviendo al pasillo")
		avanzar(3.0,5.0)
	elif frase=="al cuarto uno":
		hablar("Moviendo al cuarto uno")
    		print("Moviendo al cuarto uno")
		avanzar(4.0,1.0)
	elif frase=="al cuarto dos":
		hablar("Moviendo al cuarto dos")
    		print("Moviendo al cuarto dos")
		avanzar(5.5,2.0)
	elif frase=="al cuarto tres":
		hablar("Moviendo al cuarto tres")
    		print("Moviendo al cuarto tres")
		avanzar(3.5,-1.0)
	elif frase=="al cuarto cuatro":
		hablar("Moviendo al cuarto cuatro")
    		print("Moviendo al cuarto cuatro")
		avanzar(5.5,-1.5)
	elif frase== "pausa":
		hablar("Pausando servicio")
		print("Pausando servicio, para reanudarlo diga: comenzar")
		comenzar = False
	elif frase == "parar":
		hablar("Terminando  vuelva pronto")
		print("Terminando, vuelva pronto!")
		break
	#else:
		#print("Comando no reconocido")
      else:
	if frase == "comenzar":
		print("Escuchando instrucciones...")
		hablar("Escuchando instrucciones")
		comenzar = True
	elif frase == "parar":
		hablar("Terminando  vuelva pronto")
		print("Terminando, vuelva pronto!")
		break
	#else:
		#print("Comando no reconocido")

def avanzar(x,y):
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
	hablar("Se llego al destino")
    	print("Se llego al destino")
        return client.get_result()
	

def hablar(texto):
    rospy.init_node("speech_syn")
    pub_speech = rospy.Publisher("robotsound", SoundRequest, queue_size=10)
    loop = rospy.Rate(2)

    msg_speech = SoundRequest()
    msg_speech.sound   = -3
    msg_speech.command = 1
    msg_speech.volume  = 1.0
    msg_speech.arg2    = "voice_el_diphone"
    msg_speech.arg = texto

    loop.sleep()
    pub_speech.publish(msg_speech)




if __name__ == "__main__":
    main()



