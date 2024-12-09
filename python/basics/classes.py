# Creación de una clase básica

class Persona:

    # Constructor
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    # Método
    def saludar(self):
        return f'Hola soy {self.nombre} y tengo {self.edad} años'


persona = Persona('Juan', 21)
print(persona.saludar())


'''

Ejercicio 1: Crea una clase básica
Define una clase Coche con los atributos marca, modelo y año.
Agrega un método detalles que imprima la información del coche.


'''

print('**************************************************************')


class Coche:
    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def details(self):
        return f'El Coche es de la marca {self.marca}, modelo {self.modelo},  del año {self.anio}'


coche1 = Coche('Mercedes', 'Benz', 2014)
print(coche1.details())


print('**************************** Herencia **********************************')


'''

Una clase puede heredar atributos y métodos de otra clase

'''


class Estudiante(Persona):
    # Constructor
    def __init__(self, nombre: str, edad: int, carrera: str):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        return f'El estudiante {self.nombre} está estudiando {self.carrera} con la edad de {self.edad}'


estudiante1 = Estudiante('Pepito', 30, 'Artes')
print(estudiante1.estudiar())

print('**************************************************************')


print('**************************** Encapsulamiento **********************************')


'''

Controla el acceso a los atributos utilizando _ (protegido) o __ (privado).

'''


class CuentaBancaria:

    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            return True
        return False

    def mostrar_saldo(self):
        return self.__saldo


print('**************************************************************')


print('**************************** Polimorfismo **********************************')


'''

Los métodos pueden comportarse de manera diferente dependiendo de la clase.

'''


class Animal:

    def hablar(self):
        pass


class Perro(Animal):

    def hablar(self):
        return 'Guau'


class Gato(Animal):

    def hablar(self):
        return 'Miau'


animales = [Perro(), Gato()]

for animal in animales:
    print(animal.hablar())


print('**************************************************************')


print('**************************** Practica **********************************')


'''

Sistema de biblioteca
Crea una clase Libro con atributos titulo, autor y disponible.
Define un método prestar para cambiar el estado de disponibilidad.
Define un método devolver para marcar el libro como disponible

'''


class Libro:

    def __init__(self, titulo: str, autor: str, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def prestar(self):
        self.disponible = False
        return f'Se ha prestado el libro {self.titulo} del autor {self.autor}. El libro ya no está dispobible'

    def devolver(self):
        self.disponible = True
        return f'Se ha devuelto el libro {self.titulo} del autor {self.autor}. El libro está disponible'


print('**************************************************************')
