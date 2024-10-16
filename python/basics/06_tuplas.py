tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

for i in tupla:
    print(i)

dimensions = (200, 50)

for dimension in dimensions:
    print(dimension)


dishes = ('fish', 'meat', 'oniguiri', 'ramen', 'fruits salad')

for food in dishes:
    print(food)

dishes = ('fish', 'meat', 'oniguiri', 'ramen', 'Nachos')

for food in dishes:
    print(food)
#!/usr/bin/python3

example = (1, 2, 3, 4, 5)

print(type(example))

print(example[-1])

# No se puede actualizar (al menos no de manera directa)
# example[0] = 10 --> Error

tuple_example = (1, "hello", [1, 2, 3], {'manzanas': 1, "peras": 5}, 5, True)
print(tuple_example)

num_tuple_one = (1, 2, 3, 4, 5, 6)
num_tuple_two = (7, 8, 9, 10)
final_tuple = num_tuple_one + num_tuple_two
print(final_tuple)

pares_tuple = tuple(i for i in final_tuple if i % 2 == 0)
print(pares_tuple)

db1_credentials = ("Juanhez", "kjfg98hjrhg8934")

try:
    db1_credentials[0] = 'explotar'
    print(db1_credentials)
except TypeError:
    print("[+] ERROR: No puedes cambiar el contenido de una tupla")
