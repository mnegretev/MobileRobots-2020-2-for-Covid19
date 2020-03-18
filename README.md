# MobileRobots-2020-2-for-Covid19

Material para el curso alternativo sobre Construcción de Robots Móviles en tiempos del Covid19.

## Requerimientos

* Ubuntu 18.04 and ROS Melodic OR
* Ubuntu 16.04 and ROS Kinetic

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
