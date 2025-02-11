#!/usr/bin/env python3


import pickle


class CustomObject:
    """
    Class that defines a custom object
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the object's attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object to a file
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            return obj
        except FileNotFoundError:
            print("File not found")
            return None
