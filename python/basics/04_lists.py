### Lists ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [20, 1.85, "Juan", "Hernandez"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Juan"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
# print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("JuanhezDev")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))

# Ejercicios del libro de python (Curso intensivo edicion 3 - Seccion de las listas)

# Resolviendo punto 1

invitados = ['Alan', 'Karen', 'Melissa']

print(
    f'Hola {invitados[0]} te invito a cenar el viernes en la noche ¿Te animas?')
print(
    f'Hola {invitados[1]} te invito a cenar el viernes en la noche ¿Te animas?')
print(
    f'Hola {invitados[2]} te invito a cenar el viernes en la noche ¿Te animas?')

# Resolviendo punto 2

print(f'{invitados[2]} canceló la ida a la cena 🥲')

invitados[2] = 'Zoe'

print(
    f'Hola {invitados[0]} te invito a cenar el viernes en la noche ¿Te animas?')
print(
    f'Hola {invitados[1]} te invito a cenar el viernes en la noche ¿Te animas?')
print(
    f'Hola {invitados[2]} te invito a cenar el viernes en la noche ¿Te animas?')

# Resolviendo punto 3

print('Chicos he encontrrado una mesa más grande!!\nVoy a invitar a otros :3')

invitados.insert(0, 'Aslan')
invitados.insert(1, 'Otto')
invitados.append('Miguel')

print(
    f'Hola {invitados[0]} te invito a cenar el viernes en la noche ¿Te animas?')
print(
    f'Hola {invitados[1]} te invito a cenar el viernes en la noche ¿Te animas?')
print(
    f'Hola {invitados[2]} te invito a cenar el viernes en la noche ¿Te animas?')
print(
    f'Hola {invitados[3]} te invito a cenar el viernes en la noche ¿Te animas?')
print(
    f'Hola {invitados[4]} te invito a cenar el viernes en la noche ¿Te animas?')
print(
    f'Hola {invitados[5]} te invito a cenar el viernes en la noche ¿Te animas?')

# Resolviendo punto 3

print('Lo siento pero solo puedo invitar a dos personas a cena, nos cancelaron la mesa')

invitado1 = invitados.pop(0)
invitado2 = invitados.pop(1)
invitado3 = invitados.pop(2)


print(f'Lo siento {
      invitado1} nos quitaron la mesa grande y se cancelaron las invitaciones\nPrometo invitarte la otra semana <3')
print(f'Lo siento {
      invitado2} nos quitaron la mesa grande y se cancelaron las invitaciones\nPrometo invitarte la otra semana <3')
print(f'Lo siento {
      invitado3} nos quitaron la mesa grande y se cancelaron las invitaciones\nPrometo invitarte la otra semana <3')


print(
    f'Hola {invitados[0]} te invito a cenar el viernes en la noche ¿Te animas?')
print(
    f'Hola {invitados[1]} te invito a cenar el viernes en la noche ¿Te animas?')

# --------------------------------------------------------------------------------------------------------------------

# Ordenar una lista de manera permante sort ()

animes = ['oregairu', 'shigatsu wa kimi no uso',
          'naruto', 'kimetsu no yaiba', 'jujustu kaisen']
animes.sort()  # ordenado alfabeticamente de manera permanente
print(animes)

# Ordenar en alfabetico inverso permanente
animes = ['oregairu', 'shigatsu wa kimi no uso',
          'naruto', 'kimetsu no yaiba', 'jujustu kaisen']
animes.sort(reverse=True)
print(animes)

# Ordenar una lista de manera temporal sorted()
animes = ['oregairu', 'shigatsu wa kimi no uso',
          'naruto', 'kimetsu no yaiba', 'jujustu kaisen']
print(f'Esta es la lista original {animes}')
print(f'Sorted list {sorted(animes)}')
print(f'Esta es la lista original {animes} de nuevo')

# Imprimir una lista en orden inverso
'''
reverse() no invierte la lista en orden alfabetico, si no que la invierte respecto al orden de la lista,
si queremos volver a verla con el orden original solo debemos aplicar reverse() de nuevo
'''

animes = ['oregairu', 'shigatsu wa kimi no uso',
          'naruto', 'kimetsu no yaiba', 'jujustu kaisen']
animes.reverse()
print(f'Animes con reverse {animes}')

# Obtener la longitud de una lista

animes = ['oregairu', 'shigatsu wa kimi no uso',
          'naruto', 'kimetsu no yaiba', 'jujustu kaisen']
print(len(animes))


world_places = ['Noruega', 'Japón', 'Nueva Zelanda', 'Bali', 'España']

print(sorted(world_places))
print(world_places)
print(sorted(world_places, reverse=True))

world_places.reverse()
print(world_places)

world_places.reverse()
print(world_places)

world_places.sort()
print(world_places)

world_places.sort(reverse=True)
print(world_places)

print(len(invitados))


# Todas las funciones para trabajar con listas:3
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Añadir un elemento al final de la lista
list_numbers.append(90)
print(list_numbers)

# Añadir un elemento en una posición concreta de la lista
list_numbers.insert(35, 7)
print(list_numbers)

# Actualizar una lista
list_numbers[1] = 20
print(list_numbers)

# Eliminar un elemento de la lista de manera permanente
del list_numbers[3]
print(list_numbers)

# Eliminar un elemento de la lista y usar este elemento eliminado

popped_element = list_numbers.pop(6)
print(popped_element)
print(list_numbers)

# Ordenar una lista
print(sorted(list_numbers))
print(sorted(list_numbers, reverse=True))

list_numbers.reverse()
print(list_numbers)


list_numbers.reverse()
print(list_numbers)


list_numbers.sort()
print(list_numbers)

list_numbers.sort(reverse=True)
print(list_numbers)
