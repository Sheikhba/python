class Car(object):
    condition = ("new")#<<Class member variables## this information belongs to the class Car
    def __init__ (self, model, color, mpg):
        self.model = ("DeLorean")
        self.color = ("silver")
        self.mpg = (88)
##
    def display_car(self):
        print ("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))
##
    def drive_car(self):
        self.condition = ("used")
##
my_car = Car("DeLorean", "silver", 88)#<<instances
#
print(my_car.condition)# <<calling my_car #<< then we call condition fron the class Car
#
print(my_car.model, my_car.color, my_car.mpg)
#
my_car.display_car()
#
my_car.drive_car()
print (my_car.condition)
###

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
         self.model = model
         self.color = color
         self.mpg   = mpg
         self.battery_type = battery_type
    def drive_car(self):
        self.condition = "like new"
my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

print (my_car.condition)
my_car.drive_car()
print (my_car.condition)
"""/\/\/\/\_same\/\/\/\/
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model<<
    self.color = color<<
    self.mpg   = mpg<<
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

my_car = Car("DeLorean", "silver", 88)

my_car.display_car()
"""


"""
One useful class method to override is the built-in __repr__() method, which is short for representation; by providing a return value in this method, we can tell Python how to represent an object of our class (for instance, when using a print statement)
"""

class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
    
my_point = Point3D(1, 2, 3)
print(my_point)
