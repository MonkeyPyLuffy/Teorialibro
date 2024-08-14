#TIPOS DE DATOS

#"""Cada «trozo» de memoria contiene realmente un objeto, de ahí que se diga que en Python
#todo son objetos. Y cada objeto tiene, al menos, los siguientes campos:
#• Un tipo del dato almacenado.
#• Un identificador único para distinguirlo de otros objetos.
#• Un valor consistente con su tipo.

#ejemplo de booleano

aprobado = True

#ejemplos de las funciones int,float y bool


is_raininng = False #bool

sound_level = 0     #int

temperature = 25.5  #float

#ejemplos de la funcion round().

pi = 3.1416

round(pi)
#3
round(pi, 1)
#3.1
round(pi, 2)
#3.14
round(pi, 3)
#3.141
round(3,  4)
#3.1416

#NOTA: round es para acercarse al numero escrito en una variable, y int siempre obtiene el numero entero
#round suele ser utilizado para problemas de matematicas que no den el resultado exacto o correcto.



#El tema de las cadenas es muy interesante ya que permite escribir texto de manera mas comoda
#aqui unos ejemplos


"Una cadena simple"

"Mmmm eh escuchado de la funcion str"

"¡Oye tengo una idea!"

"Pasemos a ese tema ¿esta bien?"


#tambien se pueden crear cadenas a partir de la funcion str
#ejemplos:

str(True)
#True
str(10)
#10
str(26.1)
#26.1

#aqui una breve explicacion de como funcionan cada una de estas funciones:



#bool es una funcion para determinar si una cosa es verdadera o falsa.

#int esta funcion permite convertir un numero en entero.

#float esta funcion pasa los numeros a flotantes(decimales) con exactitud.

#la funcion round() permite hacer que un numero flotante se acerque con exactitud a un numero entero.

#la funcion cadena son textos que se imprimen y que pueden ayudar a manejar texto en tus programas o otros.

#la funcion str sirve para comvertir otros datos a cadenas como simbolos o numeros.