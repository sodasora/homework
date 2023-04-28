class Shape:
    def __init__(self,name):
        self.name = name
       
    def get_area(self):
        return self.area
    
class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = radius
    def get_area(self):
        self.area = self.radius * self.radius * 3.14
        print(self.area)
      

class Rectangle(Shape):
    def __init__(self,name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    def get_area(self):
        self.area = self.width * self.length
        print(self.area)
       
myCircle = Circle("원1",5)
myCircle.get_area()
myRectangle = Rectangle("사각형",3,4)
myRectangle.get_area()

