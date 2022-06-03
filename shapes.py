from math import pi
class Circle():
    def __init__(self,radius) :
        self.radius=radius

    def area(self):
        area_of_a_circle = pi*self.radius**2
        return area_of_a_circle
    def circumference(self):
        circumference_of_a_circle=2*pi*self.radius
        return circumference_of_a_circle
    
    
my_circle = Circle(radius=14)
print(my_circle.radius)
print(my_circle.area())
print(my_circle.circumference())
 
 
class Square():
     def __init__(self,a):
        self.a =a   
     def area(self):
         area_of_a_square = self.a**2
         return area_of_a_square
     def perimeter(self):
         perimeter_of_a_square = 4*self.a
         return perimeter_of_a_square
     
my_square = Square(a=10)
print(my_square.area())
print(my_square.perimeter())


class  Rectangle():
    def __init__(self,w,l) :
        self.w = w
        self.l = l
    def area(self):
        area_of_a_rectangle = self.w * self.l
        return area_of_a_rectangle
    def perimeter(self):
        perimeter_of_a_rectangle  = self.l
        return perimeter_of_a_rectangle
    
    
my_rectangle = Rectangle(l=12,w=10)
print(my_rectangle.area())
print(my_rectangle.perimeter())

class Sphere():
    def __init__(self,r) :
        self.r =r
    
    def surface_area(self):
        surface_area_of_a_sphere =4*pi*self.r
        return  surface_area_of_a_sphere
    def volume(self):
        volume_of_a_sphere = 1.333333*pi*self.r**3
        return volume_of_a_sphere
    
my_sphere = Sphere(r=9)
print(my_sphere.r)
print(my_sphere.surface_area())
print(my_sphere.volume())