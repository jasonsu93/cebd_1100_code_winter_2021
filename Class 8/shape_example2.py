from ShapeClasses.Square import Square
from ShapeClasses.Circle import Circle
from ShapeClasses.Rectangle import Rectangle

sq1 = Square("White", "Metal", 5.2)
sq2 = Square("White", "Metal", 7.5)
cir1 = Circle("White", "Metal", 7.5)
cir2 = Circle("White", "Metal", 10)
rec1 = Rectangle("White", "Metal", 5, 10)
rec2 = Rectangle("White", "Metal", 50, 10)

shapes_array = [sq1, sq2, cir1, cir2, rec1, rec2]

total_area = 0.0

for shape in shapes_array:
    total_area += shape.area()

print("The total areais " + str(total_area))

print("The perimeter of sq1 and rec1 is " + str(sq1.perimeter() + rec1.perimeter()))