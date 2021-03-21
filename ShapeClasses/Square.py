from ShapeClasses.Shape import Shape


#  This inherits from Shape
class Square(Shape):
    
    def __init__(self, colour, material, bottom_side):

        self.bottom_side = bottom_side
        # self.colour = colour

        #Find a way to call the constructor of the parent "shape" here

        super().__init__(colour, material)

    def area(self):
        return self.bottom_side ** 2

    def perimeter(self):
        return self.bottom_side * 4
