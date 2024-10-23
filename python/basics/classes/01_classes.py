class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def geating(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old"


juan = Person("Juan", 21)

print(juan.geating())


class Restaurante:
    def __init__(self, nombre_restaurante: str, tipo_cocina: str):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 20

    def describir_restaurante(self):
        return f'Bienvenid@ al restaurante {self.nombre_restaurante}, tenemos cocina tipo {self.tipo_cocina}'

    def abrir_restaurante(self):
        return f'El restaurante {self.nombre_restaurante} está abierto'

    def stablish_serve_num(self, num_serv: int):
        self.numero_servido = num_serv

        return f'Se han servido {num_serv} platos a los clientes'

    def increment_serve_num(self, num_serv: int):
        self.numero_servido += num_serv

    def read_serve(self):
        return f'Se han servido {self.numero_servido}'


class IceCreamCar(Restaurante):
    def __init__(self, nombre_restaurante: str, tipo_cocina: str):

        super().__init__(nombre_restaurante, tipo_cocina)
        self.flavors = ['Vanilla', 'Chocolate', 'Brownie']


restaurante = Restaurante('Las ricuras', 'Buffet')
print(restaurante.describir_restaurante())
print(restaurante.abrir_restaurante())
print(restaurante.numero_servido)
# print(restaurante.stablish_serve_num(89))
restaurante.increment_serve_num(30)
print(restaurante.read_serve())

restaurante1 = Restaurante('McDonalds', 'Carta')
print(restaurante1.describir_restaurante())
print(restaurante1.abrir_restaurante())

restaurante2 = Restaurante('El corral', 'Carta')
print(restaurante2.describir_restaurante())
print(restaurante2.abrir_restaurante())

restaurante3 = Restaurante('Fiching', 'Pesca')
print(restaurante3.describir_restaurante())
print(restaurante3.abrir_restaurante())

ice_cream_car = IceCreamCar('Bonice', 'Car-scratch')
print(ice_cream_car.describir_restaurante())
print(ice_cream_car.abrir_restaurante())
print(ice_cream_car.flavors)


class Usuario:
    def __init__(self, nombre_usuario: str, email: str, edad: int, genero: str, rol: str):
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.edad = edad
        self.genero = genero
        self.rol = rol
        self.tries = 0

    def describir_usuario(self):
        user_description = {

            "nombre": f"{self.nombre_usuario}",
            "email": f"{self.email}",
            "edad": f"{self.edad}",
            "genero": f"{self.genero}",
            "rol": f"{self.rol}"
        }

        return user_description

    def saludar_usuario(self):
        if self.genero == 'hombre':
            return f'Bienvenido {self.nombre_usuario}'
        else:
            return f'Bienvenida {self.nombre_usuario}'

    def increment_tries(self):
        self.tries += 1
        return f'User {self.nombre_usuario} tries {self.tries}'

    def reset_tries(self):
        self.tries = 0
        return f'User {self.nombre_usuario} tries {self.tries}'


class Admin(Usuario):
    def __init__(self, nombre_usuario: str, email: str, edad: int, genero: str, rol: str):
        super().__init__(nombre_usuario, email, edad, genero, rol)

        self.privileges = ['Read ALL', 'Change ALL', 'Edit ALL']

    def show_privilges(self):
        return f'El usuario {self.nombre_usuario} tiene privilegios {self.privileges}'


user1 = Usuario('Juanhez', 'bonillajuanes02@gmail.com', 21, 'hombre', 'admin')
print(user1.describir_usuario())
print(user1.saludar_usuario())
print(user1.increment_tries())
print(user1.increment_tries())
print(user1.increment_tries())
print(user1.increment_tries())
print(user1.increment_tries())
print(user1.increment_tries())
print(user1.increment_tries())
print(user1.reset_tries())

user2 = Usuario('Carla', 'carla@gmail.com', 28, 'mujer', 'Dev')
print(user2.describir_usuario())
print(user2.saludar_usuario())

user_admin = Admin('Juanhez', 'bonillajuanes02@gmail.com',
                   21, 'hombre', 'admin')
print(user_admin.describir_usuario())
print(user_admin.saludar_usuario())
print(user_admin.show_privilges())
