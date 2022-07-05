import numpy
import cv2

class Graphics:
    def __init__(self, name):
       self.name = name
       self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def display(self, name, frame):
        for elm in elements:
            frame = elm.draw()

        cv2.imshow(name, frame)
        