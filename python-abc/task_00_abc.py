#!/usr/bin/env python3

"""Abstract Base Class"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Declare the abstart method sound"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Implement the sound method for Dog"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Implement the sound method for Cat"""
    def sound(self):
        return "Meow"