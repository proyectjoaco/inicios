""" lista es una cadena de datos la cual cuenta como un tipo "type" pro si misma y puede abarcar muchos "types" dentro"""
my_list = list()
my_list = ["joaquin", 18, 1.88, "75kg", "hola"]

print (my_list)
print (type (my_list)) #aca se ve que por mas que dentro haya "int, decimal y str" cuenta como type "list"

"""el "len" contara la cantidad de elementos dentro del "kist" no la cantidad de caracteres"""
print (len (my_list))

print (my_list [0])
print (my_list [1])
print (my_list [2])
print (my_list [3])
print (my_list [4])
print (my_list [-1])
print (my_list [-2])
print (my_list [0]) # de esta forma se elije el elemento al que se quiere acceder

print (my_list.count (18)) #contara la cantidad de veces que se repite un elemento seleccionado

name = input ("cual es tu nombre?")
age = input ("cual es tu edad?")
height = input ("cuanto mides?")
user1_list = list ()
user1_list = [name, age, height]
que_user_quieres_ver_ = input ("que user quieres ver?")
if que_user_quieres_ver_ == "1":
   print (user1_list)
else :
  print ("ese user no existe")

my_list = list()
my_list = ["joaquin","aranda",18,1.80]
print (my_list)
print (my_list [3])
name, surname, age, height = my_list
print (name)
print (my_list * 2)
my_list.append ("me gusta programar")
print (my_list)

print (my_list[4])
my_list.insert (0, "verde")
print (my_list)
print (age)

my_list_pop = my_list.pop(1)
print (my_list)
print (my_list_pop)
my_new_list =my_list.copy()
#my_list.clear()
print (my_new_list)
print (my_list)
print (my_list.count("aranda"))
my_list.reverse()
print (my_list)
#my_list.sort
print (age * 2)