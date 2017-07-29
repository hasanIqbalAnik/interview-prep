"""
Singleton, Factory and Facade design patterns are discussed here.

Singleton Design Pattern:
The simplest and very commonly used design pattern. However, it is often criticised as the hindrance in
writing testable code. Some people calls it anti-pattern.

Applications:
1. Using a application Logger, called in many classes.
2. Database connection manager.
3. Reading configuration files.

"""
from abc import ABCMeta, abstractmethod, abstractproperty


class Singleton:
    """there can be only one instance of this class"""
    _single = None

    def __init__(self):
        if Singleton._single:  # if this variable is already initialized, then it's an error
            raise Exception('class was already instantiated')  # we can also return the _single variable instead of
            # raising error
        else:
            Singleton._single = 'database connection'  # assign this variable to something, for example, a db connection


# first_singleton = Singleton()
# second_singleton = Singleton()

# print first_singleton  # won't work, there would be an error in the second instantiation

"""
Factory Method and Design Pattern:

This question explains the difference between these two concepts as well as illustrates them. 
https://softwareengineering.stackexchange.com/questions/233166/factory-method-vs-factory-method-design-pattern

A Factory method is a simple method that returns a specific type of object depending on the parameter. Example:

def toyFactory(toy_name):
    if toy_name == 'car':
        return Car()
    elif toy_name == 'robot':
        return Robot()
                    
A Factory method design pattern is based on that idea. Rather than having just a method, it uses two classes to
encapsulate the object creation from the client. The abstract Creator class and the ConcreteCreator class. As python
don't have abstract keyword, the 'abc' package provides a way to define and use them. 

https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python

this question answers how to create abstract class in python. 

Anyways, here, the creation of the object is hidden from the creator. For the previous example of factory method, 
following could be the factory design pattern. 

"""


class BaseCar:
    """using abc module to get the functionality of abstract classes in python"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def drive(self):
        raise NotImplemented


class HondaFactory(BaseCar):
    """inheriting the basecar. as python supports multiple inheritence, it does not have interface"""

    def __init__(self):
        self.speed = 75
        self.mpg = 20

    def drive(self):
        print 'driving honda with speed ' + str(self.speed) + ' and mpg ' + str(self.mpg)


class ToyotaFactory(BaseCar):
    """inheriting the basecar. as python supports multiple inheritence, it does not have interface"""

    def __init__(self):
        self.speed = 100
        self.mpg = 25

    def drive(self):
        print 'driving toyota with speed ' + str(self.speed) + ' and mpg ' + str(self.mpg)


class CarFactory:
    """this car factory doesn't know how individual car's are made. it just know with what name
    to call them. """

    def __init__(self):
        self._car = None

    def get_car(self, car_name):
        if car_name == 'honda':
            self._car = HondaFactory()
        elif car_name == 'toyota':
            self._car = ToyotaFactory()
        return self._car


car_factory = CarFactory()
car_factory.get_car('toyota').drive()

"""
Facade Design Pattern:
Facade means a door to a building. If there is a situation where a client needs to ask a simple question
to a complex system and he doesn't know how to navigate through the complex system, a Facade design pattern can
be used to prive a single point of query. For example, a user may just want to turn a computer on, but he doesn't know
how to work with all that CPUs, RAMs, Hardwares. He simply asks to a Facade to start the computer, the Facade knows
how to do it.  

Example taken from: 
https://en.wikipedia.org/wiki/Facade_pattern  
"""


class CPU(object):
    """by default in python 2.7, classes don't inherit the object class as base, unlike python 3.
    it becomes a classic class. so to match the future version, a object should be inherited. """

    def freeze(self):
        print('freezing processor')

    def execute(self):
        print('executing processor')


class RAM(object):
    def load(self):
        print('loading data in RAM')


class HardDrive(object):
    def read(self):
        print('reading from hard drive')


class ComputerFacade(object):
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.hd = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.ram.load()
        self.hd.read()


computer_facade = ComputerFacade()
computer_facade.start()
