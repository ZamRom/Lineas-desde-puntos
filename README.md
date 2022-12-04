# Líneas desde puntos
### Lines from points
**Autor:** Ariel Rodolfo Zamudio Romero
**Correo de contacto:** zamromxd@gmail.com
#### Metodo de ejecución e instalación 
Para ejecutar el programa solo es necesario tener instalado una versión de Python (de preferencia el 3) y descargar el archivo y hacer clic sobre el para que abra la terminal y poder interactuar con el programa
#### Introducción 
El objetivo de este proyecto es el graficar líneas/rectas dados los puntos que ingrese el usuario de 3 formas distintas:

* Unidos los puntos uno a uno como un polígono
* Unidos todos los puntos a un punto central como una estrella
* Unidos todos con todos como si fuera un grafo completo

#### Metodología
Se utilizan las librerías: _[**Matplotlib**](https://matplotlib.org/) y **[Numpy](https://numpy.org/)**_ para graficar las rectas utilizando el método _punto-pendiente_ de geometría, en otras palabras, utilizando la formula _y = m(x-x1)+y1_

#### Implementación
Con ayuda de numpy crearemos '_arrays_' para calcular la serie de puntos necesarios (estilo; x0 y0,x1 y1 dentro de la recta para su calculo) y con ayuda de matplotlib haremos el entorno y la graficación de las funciones

#### Pruebas
Haremos 4 pruebas básicas para probar los 3 formas disponibles y otra para observar la opción que permite revisar la grafica anterior ('T' sería la terminal y 'U' sería el usuario) (Revisaremos las imágenes en el siguiente apartado)
1. Caso 1.-
>- T: ¿Quiere volver a abrir la anterior grafica? [Si/No] 
>- U: n
>- T: ¿Cuál opción quiere usar?
A.- Forma Poligonal
B.- Forma Estrella
C.- Grafo completo
Opción: 
>- U: a
>- T: Si pone números demasiado grandes puede que el programa se vuelva lento o no funcione por completo
Le recomendamos que use numeros con 5 digitos maximo si quiere que se execute rapidamente
>- <<Favor de poner las coordenadas deseadas de modo: x1 y1, x2 y2>> 
>- U: 1 1, 1 -1, -1 -1, -1 1

2. Caso 2.-
>- T: ¿Quiere volver a abrir la anterior grafica? [Si/No] 
>- U: n
>- T: ¿Cuál opción quiere usar?
A.- Forma Poligonal
B.- Forma Estrella
C.- Grafo completo
Opción: 
>- U: estrella
>- T: Si pone números demasiado grandes puede que el programa se vuelva lento o no funcione por completo
Le recomendamos que use numeros con 5 digitos maximo si quiere que se execute rapidamente
>- <<Favor de poner las coordenadas deseadas de modo: x1 y1, x2 y2>> 
>- U: 1 1, 1 -1, -1 -1, -1 1

3. Caso 3.- 
>- T: ¿Quiere volver a abrir la anterior grafica? [Si/No] 
>- U: n
>- T: ¿Cuál opción quiere usar?
A.- Forma Poligonal
B.- Forma Estrella
C.- Grafo completo
Opción: 
>- U: 3
>- T: Si pone números demasiado grandes puede que el programa se vuelva lento o no funcione por completo
Le recomendamos que use numeros con 5 digitos maximo si quiere que se execute rapidamente
>- <<Favor de poner las coordenadas deseadas de modo: x1 y1, x2 y2>> 
>- U: 1 1, 1 -1, -1 -1, -1 1
4. Caso 4.-
> - T: ¿Quiere volver a abrir la anterior grafica? [Si/No] 
> - U: s

#### Resultados
![Caso 1](https://github.com/ZamRom/LinesFromPoint/blob/main/Caso1.jpg?raw=true "Caso 1")
>Este seria el resultado del caso 1

![Caso 2](https://github.com/ZamRom/LinesFromPoint/blob/main/Caso2.jpg?raw=true "Caso 2")
>Este seria el resultado del caso 2

![Caso 3](https://github.com/ZamRom/LinesFromPoint/blob/main/Caso3.jpg?raw=true "Caso 3")
>Este seria el resultado del caso 3

![Caso 4](https://github.com/ZamRom/LinesFromPoint/blob/main/Caso4.jpg?raw=true "Caso 4")
>Este seria el resultado del caso 4 (_Aunque es un tanto obvio porque solo volvió a graficar la anterior configuración_)

#### Conclusiones
Es un programa que usa un algoritmo bastante sencillo para graficar rectas dados 2 puntos, pero ayuda bastante para los casos sencillos donde uno ocupa ver la clase de "grafico" que crean los puntos que tenemos
#### Licencia
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
