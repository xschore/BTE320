import math

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distance(self,other):
        x_diff=self.x-other.x
        y_diff=self.y-other.y
        d=math.sqrt(x_diff**2+y_diff**2)
        print(d)

p1=Point(3,4)
p2=Point(6,8)
# p1.distance(p2)

class Point3D(Point):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
    
    def distance(self,other):
        x_diff=self.x-other.x
        y_diff=self.y-other.y
        z_diff=self.z-other.z
        d=math.sqrt(x_diff**2+y_diff**2+z_diff**2)
        print(d)

p3=Point3D(4,5,6)
p4=Point3D(7,8,9)
p3.distance(p4) #does not matter which instance you use as 'self' since differences are squared

class Animal:
    def __init__(self,legs):
        print('Animal Created')
        self.legs=legs
        
    def whoAmI(self):
        print('I am an animal')

class Bird(Animal): #class bird inherits from class animal
    def __init__(self,legs,wings):
        super().__init__(legs) #refers to parent class for parameters occurring in both classes. Need to do this when using constructor in child class
        self.wings=wings
        print('Bird Created')

    def fly(self):
        print('Birds can fly') #bird has 3 methods: fly, whoami, and constructor (init)
    
# a=Animal(4)
# b=Bird(2,2)
# b.fly()