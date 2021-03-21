from ShapeClasses.Shape import Shape
import math

#  This inherits from Shape, measurement is radius.
class Circle(Shape):
    
    def __init__(self, colour, material, radius):

        self.radius = radius
        # self.colour = colour

        #Find a way to call the constructor of the parent "shape" here

        super().__init__(colour, material)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
