### le pedi a chat gpt un ejecicio que contenga los 5 puntos que aprendi Enunciado: ###
"""
-Pedí al usuario:
+nombre
+edad
+altura
-Creá una tupla llamada usuario con esos datos en este orden:
+(nombre, edad, altura)
-Guardá esa tupla dentro de una lista llamada usuarios.
-Mostrá por pantalla:
+la lista completa
+cuántos usuarios hay registrados
+el nombre del primer usuario
+el último dato del usuario (usando índice negativo)
-Usá operadores para:
+sumar 1 a la edad del usuario
+mostrar un mensaje indicando si es mayor de edad (>= 18)
"""

name = (input ("cual es tu nombre?: "))
age = (input ("cuantos años tienes?: "))
height = (input ("cuanto mides?: "))
user1_tuple = name, age, height
print (user1_tuple)
list_users = list()
list_users = [user1_tuple]
print (list_users)
print (len (list_users))
print (name)
print (user1_tuple [-1])
age = (int (age) + 1)
print (age)
if age >= 18:

    print ("eres mayor de edad, puedes pasar")

else:

    print ("eres menor de edad, no puedes pasar")

### segundo ejercicio###

"""
Ejercicio puente (muy corto)

Hacelo en 10–15 minutos, no más.

Enunciado

-Pedí nombres de usuarios en un loop

-Guardalos en una lista

-Permití salir escribiendo "salir"

-Mostrá la lista final

Nada de archivos. Nada de JSON. Simple.
"""
nombres_users = []

while True:
    name = input ("ingrese un nombre (o salir): ")

    if name == "salir":
        print ("los usuarios son:", nombres_users)
        break
    else:
        nombres_users.append (name) 
# este ejercicio no me salio, pero una vez resuelto por chat entendi el problema que tenia y su resolucion


