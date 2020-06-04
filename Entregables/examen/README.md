# Examen Parcial

**Alumno:** Paul Sebastian Aguilar Enriquez <br>
**Número de cuenta:** 415028130

## Nota al lector

Este documento fue escrito originalmente en `Markdown` y posteriormente exportado a un PDF, por lo cual, para una mejor lectura, revisar el documento original en [https://github.com/mnegretev/MobileRobots-2020-2-for-Covid19/blob/aguilar_enriquez/Entregables/examen/README.md](https://github.com/mnegretev/MobileRobots-2020-2-for-Covid19/blob/aguilar_enriquez/Entregables/examen/README.md).

### 1. Explique qué es la configuración, espacio de configuraciones y grados de libertad de un robot móvil.

### 2. Investigue dos métodos basados en grafos para planeación de rutas.

Los **_métodos geométricos_** o también llamados **_métodos roadmap (RM)_** se
caracterizan  por  construir primero una descripción del espacio libre con la
forma de una red o grafo para posteriormente unir los puntos inicial y final del
robot al grafo, para por último escoger aquél camino dentro del _roadmap_
(grafo) que minimice el coste (distancia o tiempo). Estos métodos son válidos
para problemas de planificación sencillos.

#### Grafos de visibilidad

Dado un conjunto de obstáculos con forma poligonal en el plano euclidiano se
dice que el grafo de visibilidad es aquel grafo en el cual cada nodo representa
un vértice de los polígonos y las aristas son las conexiones visibles entre
tales vértices. Esto quiere decir que para cada arista en el grafo de
visibilidad definida por $v_{1}$ y $v_{2}$, el segmento de recta que conecta los
vértices correspondientes en el plano no se interseca con ningún polígono
(obstáculo).

<div align="center">

![Grafo_Visibilidad](./imgs/01_grafo_de_visibilidad.png)

Grafo de visibilidad, los nodos representan los vértices y las aristas unen
vértices visibles entre sí

</div>

#### Diagramas de Voronoi o Polígonos de Thiessen

Consiste en la descomposición de un espacio métrico en regiones asociadas a la
presencia de obstáculos, asignándole en dicha descomposición a cada uno de los
obstáculos una región en el espacio métrico la cual es formada por los puntos más
cercanos a él y a los demás obstáculo.

De esta forma se puede construir una configuración de aristas y vértices, para
la cual se pueden generar dos tipos de trayectorias, lineas rectas y parábolas.

Las lineas rectas surgen cuando se hayan a igual distancia dos aristas de dos
obstáculos diferentes, mientras que en el caso de tratarse de un vértice y una
arista resulta la parábola.

<div align="center">

![Voronoi](./imgs/02_Euclidean_Voronoi_diagram.png)

20 puntos en el plano y su partición del plano en regiones de Voronoi.

</div>


### 3. Investigue dos métodos basados en muestreo para planeación de rutas.

Los métodos basados en muestreo son los llamados **_métodos probabilísticos_**
que a diferencia de los clásicos por geometría, se basan en  la construcción de
un grafo mediante la creación de puntos aleatorios en el espacio de trabajo
(fase de muestreo o aprendizaje), intentando la unión con el grafo de los puntos
iniciales y finales y su posterior conexión dentro del mismo minimizando el
coste (fase de búsqueda).

El nombre de método probabilístico se debe a que se muestrea a ciegas el espacio
de trabajo, confiando en que cuantos más puntos se muestreen más probable será
encontrar un camino que una el punto inicial con el final.

En la fase de muestreo cada punto que se selecciona, aleatoriamente, debe
cumplir ser libre de obstáculos y poderse unir con el grafo mediante un camino
sin colisiones.

En la fase de búsqueda se busca dentro del grafo obtenido en la fase de muestreo
aquel que minimice el coste, definiendo como coste la distancia o el tiempo que
tarda en alcanzar el punto final desde el punto de inicio.

#### Mapas probabilísticos o PRM (Probabilistic Roadmap Method).

La idea básica del PRM es tomar muestras aleatorias del espacio de la
configuración del robot, probándolas para ver si están en el espacio libre, y
utilizar un planificador local para intentar conectar estas configuraciones con
otras configuraciones cercanas. Se añaden las configuraciones de inicio y de
fin, y se aplica un algoritmo de búsqueda al grafo resultante para determinar
una trayectoria entre las configuraciones de inicio y de fin.

El planificador probabilístico de la ruta consta de dos fases: una de
construcción y otra de consulta.

En la fase de construcción, se construye una hoja de ruta (grafo), que aproxima
los movimientos que se pueden realizar en el entorno. Primero, se crea una
configuración aleatoria. Luego, se conecta con los k vecinos más cercanos.
Las configuraciones y conexiones se añaden al grafo hasta que el mapa de ruta es
lo suficientemente denso.

En la fase de consulta, las configuraciones de inicio y fin se conectan al
grafo, y el camino se obtiene mediante un algoritmo de búsqueda de caminos como
Dijkstra.

<div align="center">

![PRM](./imgs/03_PRM_with_Ob-maps.gif)

Ejemplo de PRM que explora caminos factibles alrededor de una serie de
obstáculos poligonales.

</div>

#### Exploración  rápida  de  árboles  aleatorios  o  RRT  (Rapidly  Exploring  Random Tree).

Rapidly-exploring Random Tree (RTT) es un algoritmo diseñado para buscar
eficientemente espacios no convexos de alta dimensión mediante la construcción
aleatoria de un árbol de relleno de espacio. El árbol se construye  de  forma  
incremental  a  partir  de  muestras  extraídas  al  azar  del  espacio  de
búsqueda  y  está intrínsicamente sesgada para crecer hacia grandes áreas no
buscadas del problema

A medida que se dibuja cada muestra, se intenta una conexión entre
ella y el estado (desplazamiento) más cercano en el árbol. Si la conexión es
factible esto resulta en la adición del nuevo estado al árbol. Con un muestreo
uniforme del espacio de búsqueda, la probabilidad de expandir un estado
existente es proporcional al tamaño de su polígono de Voronoi, estos polígonos se
van generando conforme se construye el árbol y se mapean obstáculos.

<div align="center">

![PRM](./imgs/04_Rapidly-exploring_Random_Tree_RRT.gif)

Animación de un RTT de 1000 iteraciones.

</div>

### 4. Explique en qué consiste el proceso de SLAM (Simultaneous Localization and Mapping).

La localización y modelado simultáneos, mapeo y localización simultáneos​ o SLAM,
es una técnica usada por robots y vehículos autónomos para construir un mapa de
un entorno desconocido en el que se encuentra, a la vez que estima su
trayectoria al desplazarse dentro de este entorno.

Given a series of controls u t {\displaystyle u_{t}} u_{t} and sensor observations o t {\displaystyle o_{t}} o_{t} over discrete time steps t {\displaystyle t} t, the SLAM problem is to compute an estimate of the agent's state x t {\displaystyle x_{t}} x_{t} and a map of the environment m t {\displaystyle m_{t}} m_{t}. All quantities are usually probabilistic, so the objective is to compute:

    P ( m t + 1 , x t + 1 | o 1 : t + 1 , u 1 : t ) {\displaystyle P(m_{t+1},x_{t+1}|o_{1:t+1},u_{1:t})} {\displaystyle P(m_{t+1},x_{t+1}|o_{1:t+1},u_{1:t})}

Applying Bayes' rule gives a framework for sequentially updating the location posteriors, given a map and a transition function P ( x t | x t − 1 ) {\displaystyle P(x_{t}|x_{t-1})} P(x_{t}|x_{t-1}),

    P ( x t | o 1 : t , u 1 : t , m t ) = ∑ m t − 1 P ( o t | x t , m t , u 1 : t ) ∑ x t − 1 P ( x t | x t − 1 ) P ( x t − 1 | m t , o 1 : t − 1 , u 1 : t ) / Z {\displaystyle P(x_{t}|o_{1:t},u_{1:t},m_{t})=\sum _{m_{t-1}}P(o_{t}|x_{t},m_{t},u_{1:t})\sum _{x_{t-1}}P(x_{t}|x_{t-1})P(x_{t-1}|m_{t},o_{1:t-1},u_{1:t})/Z} {\displaystyle P(x_{t}|o_{1:t},u_{1:t},m_{t})=\sum _{m_{t-1}}P(o_{t}|x_{t},m_{t},u_{1:t})\sum _{x_{t-1}}P(x_{t}|x_{t-1})P(x_{t-1}|m_{t},o_{1:t-1},u_{1:t})/Z}

Similarly the map can be updated sequentially by

    P ( m t | x t , o 1 : t , u 1 : t ) = ∑ x t ∑ m t P ( m t | x t , m t − 1 , o t , u 1 : t ) P ( m t − 1 , x t | o 1 : t − 1 , m t − 1 , u 1 : t ) {\displaystyle P(m_{t}|x_{t},o_{1:t},u_{1:t})=\sum _{x_{t}}\sum _{m_{t}}P(m_{t}|x_{t},m_{t-1},o_{t},u_{1:t})P(m_{t-1},x_{t}|o_{1:t-1},m_{t-1},u_{1:t})} {\displaystyle P(m_{t}|x_{t},o_{1:t},u_{1:t})=\sum _{x_{t}}\sum _{m_{t}}P(m_{t}|x_{t},m_{t-1},o_{t},u_{1:t})P(m_{t-1},x_{t}|o_{1:t-1},m_{t-1},u_{1:t})}

Like many inference problems, the solutions to inferring the two variables together can be found, to a local optimum solution, by alternating updates of the two beliefs in a form of EM algorithm.

### 5. Explique en qué consiste la localización mediante filtros de partı́culas, sus ventajas sobre el Filtro de Kalman y los paquetes de ROS que lo implementan.

### 6. Investigue qué son los campos potenciales y explique los pasos generales para implementarlos.

### 7. Explique qué es una transformación homogénea y para qué se utiliza en robots móviles.
### 8. Investigue qué es un robot con restricciones no holonómicas de movimiento.

### Referencias

- [https://bibing.us.es/proyectos/abreproy/71064/fichero/1064-MONTES.pdf](https://bibing.us.es/proyectos/abreproy/71064/fichero/1064-MONTES.pdf)
- [https://porprofesionalmic.files.wordpress.com/2015/09/investigacion-documental-navegacion-planificacion-rutas.pdf](https://porprofesionalmic.files.wordpress.com/2015/09/investigacion-documental-navegacion-planificacion-rutas.pdf)
- [https://es.wikipedia.org/wiki/Grafo_de_visibilidad](https://es.wikipedia.org/wiki/Grafo_de_visibilidad)
- [https://es.wikipedia.org/wiki/Pol%C3%ADgonos_de_Thiessen](https://es.wikipedia.org/wiki/Pol%C3%ADgonos_de_Thiessen)
- [https://en.wikipedia.org/wiki/Probabilistic_roadmap](https://en.wikipedia.org/wiki/Probabilistic_roadmap)
- [https://en.wikipedia.org/wiki/Rapidly-exploring_random_tree](https://en.wikipedia.org/wiki/Rapidly-exploring_random_tree)
- [https://es.wikipedia.org/wiki/Localizaci%C3%B3n_y_modelado_simult%C3%A1neos](https://es.wikipedia.org/wiki/Localizaci%C3%B3n_y_modelado_simult%C3%A1neos)
