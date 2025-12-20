# recomendado cuando necesitamos una estructura de datos que no admita repetidos elementos y no se necesite un orden obligatorio
my_set = set ()
my_set = {"joaco" ,19,1.5,"aranda", 18}
print (type (my_set)) #es un tipo de dato (type: set)
print (my_set)
print (my_set)
my_set.add ("mouredev")
print (my_set)
my_set.add ("mouredev") # no admite repetidos, el "mouredev" aparecera solo una vez
print (my_set) # no es una estructura con orden como lo son las listas


#no podemos buscar un elemento en especifico como (my_set[1]), pero si preguntar si existe tal elemento en el set
print ("joaco" in my_set) #vemos que nos dice de forma booleana si existe o no el elemento
print ("ailen" in my_set) # "     "           ""                 ""                 ""
 
my_set.remove("mouredev") # borre solo una vez mouredev y ya no existe, por mas que lo añadi dos veces anteriormente
print (my_set)
my_set.clear() # limpia el set, lo deja sin elementos
print (my_set)
del my_set # desaparece el set enteramente
# print (my_set) [dira que es error xq no existe el set en cuetion]

my_set = {"joaco", "aranda", 18}
my_other_set = {"practicando python",18, "joaco","aranda"}
print (my_set)
print (my_other_set) #cree dos sets parecidos

my_ultimate_set = frozenset ({"hello python", "ingenieria en sistemas", 7}) # set inmutable (no admite modificaciones)

my_new_set = my_set.union(my_other_set) # cree un tercer set, mezclando los dos anteriores
print (my_new_set) # se suman los no repetidos
print (my_new_set.difference(my_set)) # se printean los elementos que no aparecen en el set elegido

print (my_new_set.intersection(my_set)) # te da los elementos que tienen ambos sets (contrario a difference)
print (my_new_set.intersection(my_other_set))

print (my_ultimate_set)
#my_ultimate_set.add("ailen teamo") #sera error, xq queremos modificar un set inmodificable

""" ejercicio propuesto por chat gpt:
EJERCICIO 1 — Fundamentos de set (básico)

Dada la siguiente lista:

names = ["ana", "joaco", "ana", "pedro", "joaco", "lucas"]


Creá un set llamado unique_names que elimine los duplicados.

Mostrá cuántos nombres únicos hay.

Verificá si "pedro" está en el set.

Intentá agregar "ana" nuevamente y comprobá que no se duplica."""

names = ["ana", "joaco", "ana", "pedro", "joaco", "lucas"]
print (names)
unique_names = set (names)
print (type(unique_names))
print (unique_names)
print (len(unique_names)) # 4
print ("pedro" in unique_names) #true
unique_names.add("ana")
print (unique_names) # no se puede duplicar elementos en sets

""" ejercicio 2:
EJERCICIO 2 — Operaciones entre sets (intermedio)

Tenés dos sets:

students_python = {"ana", "joaco", "pedro", "lucas"}
students_java = {"joaco", "martin", "lucas", "sofia"}


Obtené los estudiantes que cursan ambos lenguajes.

Obtené los estudiantes que cursan solo Python.

Obtené los estudiantes que cursan al menos uno de los dos.

Obtené los estudiantes que cursan solo uno de los dos (no ambos).
"""

students_python = {"ana", "joaco", "pedro", "lucas"}
students_java = {"joaco", "martin", "lucas", "sofia"}

print (students_java.intersection(students_python)) #lucas y joaco
print (students_python) # 'ana', 'pedro', 'lucas', 'joaco'
print (students_python.union(students_java)) #'ana', 'joaco', 'pedro', 'lucas', 'martin', 'sofia'
print (students_java^students_python) #'ana', 'pedro', 'martin', 'sofia'


"""
🔴 EJERCICIO 5 — Validación real con set (nivel trabajo)

Un sistema permite los siguientes permisos válidos:

valid_permissions = {"read", "write", "delete"}


Un usuario intenta cargar estos permisos:

user_permissions = ["read", "write", "execute", "read"]


Eliminá los duplicados.

Detectá qué permisos no son válidos.

Generá un set solo con los permisos válidos del usuario.
"""
valid_permissions = {"read", "write", "delete"}
user_permissions = ["read", "write", "execute", "read"]
user_permissions_set = set (user_permissions)
print ("se te detectaron perimisos invalidos:", (user_permissions_set-valid_permissions))
valid_user_permissions = valid_permissions.intersection(user_permissions_set)
print (valid_user_permissions)