# Práctica 05

**Alumno:** Paul Sebastian Aguilar Enriquez <br>
**Número de cuenta:** 415028130

## Nota al lector

Este documento fue escrito originalmente en `Markdown` y posteriormente exportado a un PDF, por lo cual, para una mejor lectura, revisar el documento original en [https://github.com/mnegretev/MobileRobots-2020-2-for-Covid19/blob/aguilar_enriquez/Entregables/practica_05/README.md](https://github.com/mnegretev/MobileRobots-2020-2-for-Covid19/blob/aguilar_enriquez/Entregables/practica_05/README.md).

## Objetivo

- Síntesis de voz con *festival*.
- Realizar los ejercicios de las diapositivas 21, 22 y 23

## Entregables

- Archivos de audio donde se escuchen frase sintetizadas. Las frases a sintetizar se dejan a elección del estudiante.
- Al menos dos archivos de audio, es decir, sintetizar con al menos dos voces diferentes.

### Desarrollo

#### Instalación de las voces

Se instalaron las voces:

- `festvox-en1`
- `festvox-us1`

<div align="center">

![voces_instaladas_1](./img/practica_05_01.png)

Voces instaladas

![voces_instaladas_2](./img/practica_05_02.png)

Voces instaladas

</div>

#### Configuración y uso de voces utilizadas

Se sintetizaron textos con tres voces diferentes:

- `en1_mbrola`
- `us1_mbrola`
- `kal_diphone`

Estas se indicaron en el script `catkin_ws/src/speech_syn/scripts/speech_test.py`.

<div align="center">

![voces_seleccionadas](./img/practica_05_03.png)

Asignación de voces para sintetizar

![voces_en1_mbrola](./img/practica_05_04.png)

Voz en1_mbrola

![voces_us1_mbrola](./img/practica_05_05.png)

Voz us1_mbrola

![voces_kal_diphone](./img/practica_05_06.png)

Voz kal_diphone

</div>

#### Audios sintetizados

- [en1_mbrola](./audio/voice_01_en1_mbrola.m4a)
- [us1_mbrola](./audio/voice_02_us1_mbrola.m4a)
- [kal_diphone](./audio/voice_03_kal_diphone.m4a)
