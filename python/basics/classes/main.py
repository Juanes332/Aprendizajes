from car import *
from electric_car import ElectricCar


my_leaf = ElectricCar('Nissan', 'leaf', 2024)
print(my_leaf.batery_size.upgrade_batery())
print(my_leaf.batery_size.describe_batery())
print(my_leaf.batery_size.get_batery_range())
print(my_leaf.batery_size.describe_batery())
