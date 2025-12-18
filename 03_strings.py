"""__name__, surname, age = "joaco", "aranda", 18

print ("mi nombre es", __name__, surname, "y mi edad es", age, "años") #anda pero es incorrecto

print ("mi nombre es %s %s y mi edad es %d" %(__name__, surname, age)) #forma optima de hacer, asi no se pueden poner str por int y es mas seguro

print (f"mi nombre es {__name__} {surname} y mi edad es {age} años") # esta es la mejor forma

language = "argentina"
language_part = language [1:6]
language_partes = language [-5]
reversed_language = language [::-1] #hay que ponerlo en -1 para quue se escriba del reves correctamente

print(reversed_language)

print (language_part)

print (language_partes)

print (language.capitalize()) #pone la primera letra mayuscula

print (language.casefold())

print (language.count("a")) #cuenta la cantidad de letras seleccionada que hay en la palabra

print (language.islower())
print (language.isdecimal())#los "IS" son preguntas booleanas

print (language.isupper())
print (language.upper()  .isupper())

print (language.startswith("b"))
print (language.startswith("ar"))# startwith, pregunta si la palabra arranco con "x" letra 
"""
name, surname, age, height = "joaquin", "aranda", "18", "1.80"
print (f"mi nombre es {name}, tengo {age}, mido {1.80} metros, a y tengo {18} anos")
palabra = "programacion"
print (palabra)
print (palabra.capitalize())
print (palabra.isspace())
print (palabra.isprintable)