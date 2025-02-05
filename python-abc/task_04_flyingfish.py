#!/usr/bin/env python3


"""Define a class named Fish ,named swim and habitat"""


class Fish():
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


"""Define a class named Bird,named fly and habitat"""


class Bird():
    def fly(self):
        print("The brird is flying")

    def habitat(self):
        print("The bird lives in the sky")


"""Define a class named FlyingFish, which inherits from Fish and Bird"""


class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
