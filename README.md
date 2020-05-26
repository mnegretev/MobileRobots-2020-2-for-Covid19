# MobileRobots-2020-2-for-Covid19

Material para el curso alternativo sobre Construcción de Robots Móviles en tiempos del Covid19.

## Ejecutar proyecto final

Se deben de ejecutar los siguientes comandos:

* roslaunch bring_up robotino_simul.launch
* roslaunch bring_up navigation_move_base.launch
* roslaunch bring_up pocketsphinx_test.launch
* roslaunch bring_up speech_test.launch
* rosrun bring_up recogvoice.py
* rosrun bring_up sendgoal.py
* rosrun bring_up speakgoal.py

En el archivo pocketsphinx_test.launch se necesita editar la línea:
* param name="hmm" value="/home/lui/Downloads/CIEMPIESS_Spanish_Models_581h/Models/581HCDCONT10000SPA"/
reemplazando la ruta en value por la propia que corresponda a los modelos acústicos de [CIEMPIESS](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Mexican%20Spanish/) 

La voz utilizada es instalada por el comando:
* sudo apt-get install festvox-ellpc11k
y debe de ser movida bajo el directorio de voces en inglés para que sea reconocida.





## Instalación

Nota: se asume que ya se tiene instalado Ubuntu y ROS.

* $ git clone https://github.com/mnegretev/MobileRobots-2020-2-for-Covid19
* $ cd MobileRobots-2020-2-for-Covid19

Para ROS Melodic:
* $ ./SetupMelodic.sh
Y para ROS Kinetic
* $ ./SetupKinetic.sh

* $ cd catkin_ws
* $ catkin_make -j2 -l2
* $ sudo usermod -a -G audio <user_name>

La última instrucción agrega al usuario actual al grupo 'audio', por lo que es necesario hacer logout y login nuevamente. Para probar la instalación:

* $ cd 
* $ source MobileRobots-2020-2-for-Covid19/catkin_ws/devel/setup.bash
* $ roslaunch bring_up robotino_simul.launch

Si todo se instaló y compiló correctamente, se debería ver un rviz como el siguiente:

![RepoExample](https://github.com/mnegretev/MobileRobots-2020-2-for-Covid19/blob/master/Slides/Figures/RepoExample.png)

Para compilar las diapositivas del curso (se asume que se tiene instalado texlive):

* $ cd ~/EIR-2020-AtHomeEducation/Slides
* $ pdflatex EIR_2020_AtHomeEducation.tex

En la carpeta /Slides hay una versión compilada.

## Contacto
Dr. Marco Negrete<br>
Profesor Asociado C<br>
Departamento de Procesamiento de Señales<br>
Facultad de Ingeniería, UNAM <br>
[mnegretev.info](http://mnegretev.info)<br>
contact@mnegretev.info<br>
