import turtle
import math
import pickle
FILENAME = 'myshapefile.dat.txt'
WIDTH = 800
HEIGHT = 600
pointer = turtle.getturtle()
screen = turtle.getscreen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pointer.hideturtle()

class Shape:
    def __init__(self, color, number_of_sides, x_axis, y_axis):
        self.__color = color
        self.__number_of_sides = number_of_sides
        self.__x_axis = x_axis
        self.__y_axis = y_axis

    def set_color(self, color):
        self.__color = color

    def set_number_of_sides(self, number_of_sides):
        self.__number_of_sides = number_of_sides

    def set_x_axis(self, x_axis):
        self.__x_axis = x_axis

    def set_y_axis(self, y_axis):
        self.__y_axis = y_axis

    def get_color(self):
        return self.__color

    def get_number_of_sides(self):
        return self.__number_of_sides

    def get_x_axis(self):
        return self.__x_axis

    def get_y_axis(self):
        return self.__y_axis

    def compute_area(self):
        print("Specify a shape")

    def draw(self):
        print("You need to specify a shape ")

class Rectangle(Shape):
    def __init__(self, color, number_of_sides, x_axis, y_axis, length, width):
        Shape.__init__(self, color, number_of_sides, x_axis, y_axis)
        self.__length = length
        self.__width = width

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def compute_area(self):
        print("The area of the rectangle is", str(self.get_length() * self.get_width()))

    def draw(self):
        pointer.penup()
        pointer.goto(self.get_x_axis(), self.get_y_axis())
        pointer.color(self.get_color())
        pointer.pendown()
        pointer.seth(0)
        pointer.forward(self.get_length())
        pointer.seth(270)
        pointer.forward(self.get_width())
        pointer.seth(180)
        pointer.forward(self.get_length())
        pointer.seth(90)
        pointer.forward(self.get_width())

class Circle(Shape):
    def __init__(self, color, number_of_sides, x_axis, y_axis, radius):
        Shape.__init__(self, color, number_of_sides, x_axis, y_axis)
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def compute_area(self):
        print("The area of the circle is", str(math.pi * self.get_radius() * self.get_radius()))

    def draw(self):
        pointer.penup()
        pointer.goto(self.get_x_axis(), self.get_y_axis())
        pointer.color(self.get_color())
        pointer.pendown()
        pointer.circle(self.get_radius())

class Square(Shape):
    def __init__(self, color, number_of_sides, x_axis, y_axis, side):
        Shape.__init__(self, color, number_of_sides, x_axis, y_axis)
        self.__side = side

    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side

    def compute_area(self):
        print("The area of a square is", math.pow(self.get_side(), 2))

    def draw(self):
        pointer.penup()
        pointer.goto(self.get_x_axis(), self.get_y_axis())
        pointer.color(self.get_color())
        pointer.pendown()
        pointer.seth(0)
        pointer.forward(self.get_side())
        pointer.seth(270)
        pointer.forward(self.get_side())
        pointer.seth(180)
        pointer.forward(self.get_side())
        pointer.seth(90)
        pointer.forward(self.get_side())

class Traingle(Shape):
    def __init__(self, color, number_of_sides, x_axis, y_axis, side):
        Shape.__init__(self, color, number_of_sides, x_axis, y_axis)
        self.__side = side

    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side

    def compute_area(self):
        print("The area of the triangle is", str((math.pow(3, 0.5) / 4) * math.pow(self.get_side(), 2)))

    def draw(self):
        pointer.penup()
        pointer.goto(self.get_x_axis(), self.get_y_axis())
        pointer.color(self.get_color())
        pointer.pendown()
        pointer.seth(60)
        pointer.forward(self.get_side())
        pointer.seth(300)
        pointer.forward(self.get_side())
        pointer.seth(180)
        pointer.forward(self.get_side())

#Menu

ask_shape = 1
shapes_array = []
input_file = open(FILENAME, 'rb')
ask = input("Do you want to load your previous file? Write yes or no:")
if ask == "yes":
    eof =False
    while not eof:
        try:
            obj = pickle.load(input_file)
            obj.draw()
            shapes_array.append(obj)
        except EOFError:
            eof = True

input_file.close()
output_file = open(FILENAME, 'wb')

while ask_shape != 5:
    ask_shape = int(input("Which shape do you want to find the area for?\n Press 1 for Rectangle, press 2 for Circle,\n press 3 for square,\n press 4 for triangle,\n and 5 for quit\n"))
    if ask_shape != 5:
        ask_color = input("What color do you want?")
        ask_x_axis = int(input("What is the x axis?"))
        ask_y_axis = int(input("What is the y axis?"))

    if ask_shape == 1:
        ask_length = int(input("What is the length?"))
        ask_width = int(input("What is the width?"))
        shape_object = Rectangle(ask_color, 4, ask_x_axis, ask_y_axis, ask_length, ask_width)

    if ask_shape == 2:
        ask_radius = int(input("What is the radius?"))
        shape_object = Circle(ask_color, 0, ask_x_axis, ask_y_axis, ask_radius)

    if ask_shape == 3:
        ask_side = int(input("What is the length of the side?"))
        shape_object = Square(ask_color, 4, ask_x_axis, ask_y_axis, ask_side)

    if ask_shape == 4:
        ask_triangle_side = int(input("What is the length of one side?"))
        shape_object = Traingle(ask_color, 4, ask_x_axis, ask_y_axis, ask_triangle_side)

    if ask_shape != 5:
        shape_object.draw()
        shape_object.compute_area()
        shapes_array.append(shape_object)

store = input("Do you want to save your picture? Press y for yes and press n for no:")

if store == "y":
    for i in shapes_array:
        pickle.dump(i, output_file)
        print("In progress")

print("Succesfully saved")



output_file.close()
turtle.done()