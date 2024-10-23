class Car:
    """ Representando un coche """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Devuelve un nombre descriptivo correctamente formateado """

        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        """ Imprime el kilometrage actual del vehículo """
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """ Muestra la lectura del kilometrage con el valor dado """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Batery:
    def __init__(self, batery_size=40):
        self.batery_size = batery_size

    def describe_batery(self):
        return f'The car has a {self.batery_size}KWh battery.'

    def upgrade_batery(self):
        if self.batery_size < 65:
            self.batery_size = 65
            return 'Batery upgraded'

    def get_batery_range(self):
        if self.batery_size == 40:
            range = 150
        elif self.batery_size == 65:
            range = 225
        return f'This car can go about {range} miles on a full charge.'
