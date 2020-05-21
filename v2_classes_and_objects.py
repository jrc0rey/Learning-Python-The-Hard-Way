
import turtle

class Polygon:
    def __init__(self, sides, name, size = 300, color = "black", line_thickness = 4):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides - 2) * 180
        self.angle = (self.interior_angles / self.sides)

    def draw(self):

        for i in range(self.sides):
            turtle.pensize(self.line_thickness)
            turtle.color(self.color)
            turtle.forward(100)
            turtle.right(180 - self.angle)
        turtle.done()

#Sub class
class Square(Polygon):
    def __init__(self, size = 300, color = "black", line_thickness = 4):
        super().__init__(4, "Square", size, color, line_thickness)
    def fill(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()



square = Square(color = "red")

square.fill()



# hexagon = Polygon(6, "Hexagon")
# square = Polygon(4, "Square")
# pentagon = Polygon(5, "Pentagon")
