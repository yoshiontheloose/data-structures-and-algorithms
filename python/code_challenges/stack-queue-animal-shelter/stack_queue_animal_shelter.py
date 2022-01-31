# Create a class called AnimalShelter which holds only dogs and cats

from ctypes import cast


class Animal_Shelter:
    def __init__(self, dogs, cats):
        self.cats = cats
        self.dogs = dogs


    def enqueue(self, animal):
        if animal is True:
            animal = self.cats
        else:
            animal = self.dogs

    def dequeue(pref):

