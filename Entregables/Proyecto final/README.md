-project.gram contiene la gramática para que el robot obedezca los comandos de voz, tiene que agregarse en la ruta catkin_ws/src/pocketsphinx/vocab

-project.dic contiene la fonética para la gramática, y debe agregarse en la ruta catkin_ws/src/pocketsphinx/vocab

-robotino_simul.launch contiene los nodos que se utilizaron en el proyecto, debe remplazarse por el archivo de mismo nombre ubicado en catkin_ws/src/bring_up/launch

-listener.py es el programa que se encarga de recibir el status del robot cuando se mueve, para sintetizar si alcanzó la meta. Se puede crear un paquete nuevo, en mi caso lo agregué al paquete de vision ubicado en catkin_ws/src

-responser.py se encarga de escuchar los comandos de voz, identificarlos y ordenarle al robot dicho comando. Se puede crear un paquete nuevo, en mi caso lo agregué al paquete de vision ubicado en catkin_ws/src

-Para correrlo se deben abrir 3 pestañas en la terminal, se ejecutarán los siguientes comandos: 
	Pestaña 1: roslaunch bring_up robotino_simul.launch 
	Pestaña 2: rosrun vision listener.py
	Pestaña 3: rosrun vision responser.py

Una vez hecho esto se abrirá el entorno rviz y el robot escuchará comandos de voz para después ejecutar acciones.