Buenos días, el juego funciona de la siguiente forma, se ejecuta el codigo y este nos abre una pestaña donde podremos escoger la opciones que queramos, y se comparara con la opcion escogia por la computadora posterior a esto se dara un ganador. 
Para entender el juego mas a profundida, podemos observar el codigo donde aplicamos el bucle while ya que tenemos una condicion que es verdadera la cual son las opciones a escoger entre piedra, papel, tijera, spoke y lizard. Esto para que el usuario escoja su opción, posterior a eso asignamos le asignamos a la computadora la eleccion aleatoria con el comando random.choice, este comando nos da un elemendo random que este dentro de una cadena, un rango, una lista, una tupla o cualquier tipo de secuencia 
Posterior a esto usamos condicionales para definir el ganador, empezamos planteando un empate entre el usuario y la computadora con el if, como segunda condicional planteamos todas las posibles victorias por parte del usuario con el elif y como tercera condicionante si no se llega a cumplir ninguna de las tres perderiamos, esto con el else.
Luego de esto proponemos el el juego, donde se obtienen las opciones del usuario y de la computadora, se dan a conocer la eleccion de cada uno y se realiza una comparacion para si dar al ganador.
En la gran parte del codigo podemos observar la declaracion return, la cual nos ayuda para dar el resultado de una función.
Y eso seria la explicacion de nuestro código, en el cual predominan las condicionales y las elegimos porque se nos hizo la mejor forma de hacerlo ya que podiamos plantear todas las posibles victorias del usuario y compararlas con las de la maquina y en caso de que fueran distintas, plantear con el else que perdimos por esa parte se nos hizo mas facil y rapido de hacer con las condicionales.
Respecto a nuestra interfaz gráfica, estamos usando Pygame. Utilizando documentación que encontramos sobre la interfaz y de cómo aplicarla, fuimos desarrollando el proyecto. Para aplicar los diferentes colores, se usan combinaciones de valores RGB para conseguir el color deseado. Por ejemplo, si queríamos usar el "white", debía ser WHITE = (255, 255, 255).EL numero maximo era 225,asi que segun el color y el brillo deseado se aumenta o disminuye estos valores, De esta manera, aplicamos colores en nuestra interfaz.Para poder acomodar todo el texto en el lugar que queriamos debiamos usar coordenadas (x,y,z) para de esta manera no se sobrepongan las palabras y tengan el orden deseado. asdasdasdas dasdasdad

Instrucion de Uso:
Para poder ejectuar la interfaz grafica del juego debemos tener previamente instalada la herramienta de pygame, que esta la instalamos mediante el cdm.
El siguiente paso a seguir sería ejecutar el archivo que se llama "Interfaz grafica". Hecho esto, visualizarán el juego y deberán elegir la opción que ustedes quieran. Estas opciones están representadas con números y deberán presionar del número 1 al 5 según la opción que ustedes deseen.
