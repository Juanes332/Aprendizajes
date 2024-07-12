#!/usr/bin/python3

mi_conjunto = {1, 2, 3}

mi_conjunto.update({4, 5, 6, 7})
mi_conjunto.add(5)
mi_conjunto.remove(3)
mi_conjunto.discard(4)
# Discard elimina el elemento si se encuentra en el conjunto, si no, no se ejecuta
mi_conjunto.discard(10)
print(mi_conjunto)

mi_primer_conjunto = {1, 2, 3, 4, 5, 6}
mi_segundo_conjunto = {2, 23, 4, 3, 85, 3, 7}

conjunto_final = mi_primer_conjunto.intersection(mi_segundo_conjunto)
print(conjunto_final)

conjunto_final = mi_primer_conjunto.union(mi_segundo_conjunto)
print(conjunto_final)

conjunto_final = mi_primer_conjunto.difference(mi_segundo_conjunto)
print(conjunto_final)

# Quitar repetidos de las listas con sets

num_list = [1, 4, 7, 6445, 43, 6, 8, 5, 7, 9, 5, 2, 1, 45, 7, 2, 346, 4734]
print(num_list)

num_set = set(num_list)
print(num_set)

# Busquedas (salen mejor con sets que con listas)

conjunto = set(range(10001))
print(5555 in conjunto)
