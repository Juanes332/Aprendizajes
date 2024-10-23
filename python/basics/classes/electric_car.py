from car import Car as cr  # importación con alias
from car import Batery as bt  # importación con alias


class ElectricCar(cr):
    def __init__(self, make, model, year):

        super().__init__(make, model, year)
        self.batery_size = bt()
