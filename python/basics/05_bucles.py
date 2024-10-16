magicians = ['alice', 'martin', 'carolina']

for magician in magicians:
    print(f'{magician.title()}, that was a good trick')

## Excercises ##

pizzas = ['Bbq', 'Carnes', 'Peperoni']

for pizza in pizzas:
    print(pizza)
    print(f'Me gusta la pizza de {pizza}')

print('Me encanta la pizza :D')


animals = ['Lion', 'Tiger', 'Cat']

for animal in animals:
    print(animal)
    print(f'Un {animal} sería una excelente mascota')

print('Cualquiera de estos animales sería una excelente mascota')


print('\n ****************************************************************')

## Bucles con numeros ##
for i in range(1, 6):
    print(i)

number_list = list(range(1, 6))
print(number_list)

even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []

# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)

for value in range(1, 11):
    squares.append(value ** 2)

print(squares)


### Estadistica sencilla con una lista de numeros ###


est_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(est_list))
print(max(est_list))
print(sum(est_list))


# Lista por comprensión
squares = [value ** 2 for value in range(1, 11)]
print(squares)


### Excersises ###

number_one_to_twenty = [value for value in range(1, 21)]
print(number_one_to_twenty)


number_one_to_one_million = [value for value in range(1, 1000001)]
print(number_one_to_one_million)
print(min(number_one_to_one_million))
print(max(number_one_to_one_million))
print(sum(number_one_to_one_million))


impar_num = [value for value in range(1, 21, 2)]
print(impar_num)

num_3 = [value for value in range(3, 30, 3)]
print(num_3)

cube_list = [value ** 3 for value in range(1, 11)]
print(cube_list)

part_list = ['Charlie', 'Menfis', 'Lora', 'Megan', 'Jack']

for i in part_list[:3]:
    print(i)


list1 = [2, 3, 4, 7, 4, 8, 9, 3, 1, 10]
# list2 = list1
list2 = list1[:]

print(list1)
print(list2)
