my_tuple = tuple()
my_other_tuple = ()

my_tuple = (18, 1.80, "joaquin", "aranda", 2007, "aranda")
my_other_tuple = (1, 2, 3, 4, 5)
print (my_tuple)
print (type (my_tuple))
print (my_tuple [0])
print (my_tuple [4])
print (type (my_tuple [1])) #se puede ver el "type", de un elemento dentro de una tupla o lista
print (type (my_tuple [3])) #se puede ver el "type", de un elemento dentro de una tupla o lista
print (len (my_tuple)) #lee cantidad de elementos de la tuple
print (len (my_tuple [3]))#lee la cantidad de caracteres del elemento seleccionado de la tuple
print (my_tuple.index ("aranda")) #te dice la posicion del elemento seleccionado (si se repite el elemento, solo pone el primero)
print (type(my_other_tuple))


print (type (my_tuple + my_other_tuple))
my_plus_tuple = my_tuple + my_other_tuple #no se puede modificar las tuples pero si se puede sumarlas para una nueva
print (type (my_plus_tuple))
print (my_plus_tuple [3:6])
del my_plus_tuple
print (my_plus_tuple) #de esta forma (del my_plus_tuple) se elimina por completo la variable tuple seleccionada