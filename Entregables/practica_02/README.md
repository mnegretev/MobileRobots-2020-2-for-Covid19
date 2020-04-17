# Práctica 02

**Alumno:** Paul Sebastian Aguilar Enriquez <br>
**Número de cuenta:** 415028130

## Nota al lector

Este documento fue escrito originalmente en `Markdown` y posteriormente exportado a un PDF, por lo cual, para una mejor lectura, revisar el documento original en [https://github.com/mnegretev/MobileRobots-2020-2-for-Covid19/blob/aguilar_enriquez/Entregables/practica_02/README.md](https://github.com/mnegretev/MobileRobots-2020-2-for-Covid19/blob/aguilar_enriquez/Entregables/practica_02/README.md).

## Objetivo

- Uso de archivos urdf y árbol de transformaciones con el paquete tf.
- Realizar los ejercicios de las diapositivas 10 y 11.

## Entregables

- Capturas de pantalla donde se observe que se cambió el urdf
- Capturas de pantalla donde se observe que se cambió el mapa
- Capturas de pantalla con la etiqueta ‘origin’ cambiada
- Capturas de pantalla con alguna de las etiquetas ‘joint’ eliminada
- Comentarios sobre lo que sucedió en cada uno de los casos anteriores
- Copia de los archivos urdf y launch con las modificaciones hechas

### Capturas de pantalla donde se observe que se cambió el urdf

El archivo venia configurado originalmente con `robotino.urdf` y se modifico por
`justina_simple.urdf`.

<div align="center">

![urdf_original](./img/practica_02_01.png)

Original

![urdf_modificado](./img/practica_02_02.png)

Modificado

</div>

Lo anterior modifico el robot cargado en escena.

<div align="center">

![robot_original](./img/practica_02_03.png)

Original, Robotino.

![robot_modificado](./img/practica_02_04.png)

Modificado, Justina.

</div>

### Capturas de pantalla donde se observe que se cambió el mapa

El archivo venia configurado originalmente con `Universum.yaml` y se modifico por
`Biorobotica.yaml`.

<div align="center">

![mapa_original](./img/practica_02_05.png)

Original

![mapa_modificado](./img/practica_02_06.png)

Modificado

</div>

Lo anterior modifico el mapa cargado en escena.

<div align="center">

![mapa_original](./img/practica_02_07.png)

Original, mapa de Universum.

![mapa_modificado](./img/practica_02_08.png)

Modificado, mapa de Biorobotica.

</div>


### Capturas de pantalla con la etiqueta ‘origin’ cambiada

El archivo venia configurado originalmente con `0 0 0.25` y se modifico por
`0 0 0`.

<div align="center">

![origin_original](./img/practica_02_09.png)

Original

![origin_modificado](./img/practica_02_10.png)

Modificado

</div>

Lo anterior modifico el alcance del angulo de visión en Z, esto debido a que
ese es el componente al que se le modifico la coordenada de origen con respecto
a su padre.

<div align="center">

![origin_original](./img/practica_02_11.png)

Original, con 0.25 en Z

![origin_modificado](./img/practica_02_12.png)

Modificado, con 0 en Z.

</div>

### Capturas de pantalla con alguna de las etiquetas ‘joint’ eliminada

Se procedio a eliminar el joint de `camera_depth_optical_frame`.

<div align="center">

![joint_original](./img/practica_02_13.png)

Original

![joint_eliminado](./img/practica_02_14.png)

Eliminado

</div>

Al eliminar ese joint la definición del robot era incorrecta por lo cual se marco un error y este no se cargo en escena.

<div align="center">

![joint_error](./img/practica_02_15.png)

Error

![joint_robot_sin_cargar](./img/practica_02_16.png)

Robot sin cargar en escena

</div>

Lo que se hizo para corregir este error fue borrar el joint con su elemento padre. Esto permitio cargar el robot ya que su definición era correcta, pero con la ausencia de ese elemento se alteraron sus componentes y funcionamiento como podemos ver.

<div align="center">

![joint_sin_padre](./img/practica_02_17.png)

Aqui se elimino completamente el `link` y su `joint`, solamente se pone la imagen para que se vean los numeros de linea correspondientes y confirmar la eliminación de esas lineas.

![joint_robot_sin_cargar](./img/practica_02_18.png)

Robot en escena pero sin el deep_view de la camara RGB.

![joint_robot_sin_cargar](./img/practica_02_19.png)

`link` y `joint` comentados en el archivo

</div>

### Comentarios sobre lo que sucedió en cada uno de los casos anteriores

Los comentarios se incluyeron en cada sección anterior.

### Copia de los archivos urdf y launch con las modificaciones hechas

- [Salida del comando tf info](./info.txt)
- [Copia de robotino_simul.launch](./robotino_simul.launch)
- [Copia de robotino.urdf](./robotino.urdf)
