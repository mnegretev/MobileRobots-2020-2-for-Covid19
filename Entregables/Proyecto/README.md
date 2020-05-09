Contreras Vargas Rolando 

En el video se muestra el funcionamiento del robt a parir del reconocimiento de voz y el robot avisa cuando ha llegado a destino

Para la ejecución:

	1. Ejecutar el comando: roscore 
(Inicializa el nodo master)

	2. Ejecutar el comando: roslaunch robot_project robot_simul.launch 
(Este lauch contiene los nodos para simular al robot, moverlo, así como el reconocimiento y la sintesis de voz)

	3. Ejecutar el comando rosrun rosrun robot_project run_project.py
(EJecuta el programa principal realizado en python)


FRASES DISPONIBLES

	- GO TO KITCHEN
	- GO TO BEDROOM
	- GO TO GARDEN
	- GO TO OUTSIDE
	- ROBOT STOP

SUSCRIPTORES
	-/recognized importamos (String) ->Se utiliza para extraer la cadena procesada por el comando de voz

	-/move_base/result importamos (MoveBaseActionResult) ->Se utiliza para saber si el robot a llegado a destino

PUBLICADORES
	- /move_base_simple/goal importamos (PoseStamped) ->Se utiliza para publicar la meta

	- /move_base/cancel importamos (GoalID) ->Se utiliza para detener al robot

	- /robotsound importamos (SoundRequest) ->Se utiliza para publicar la cadena en la sitesis de voz

COMENTARIOS

 -El audio de la computadora suele viciar el reconocimiento de voz del robot, es decir que cuando menciona que llego a la posición deseada el microfono puede reconcoer la misma orden. (Se recomienda uso de audifonos)

 -El robot puede atorarse, en este caso se puede utilizar la herramienta de Rviz para colocar el robot en un punto fuera de obstaculos

