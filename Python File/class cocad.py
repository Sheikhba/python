#class name of class
#\/     \/   class inherits
#              \/
class Animal(object): 
    def __init__(self, name): # __init__ is used to initialize the object
        self.name = name
        pass    #/\         # pass dosent do anythin but its a place holder
            # self refers to the object being created
zebra = Animal("Jeffrey") # here we initilaize a verible called zebra that is set to the class name Animale that takes Jeffrey as the class inherits
print(zebra.name) # then we preint the verible zebra but with the object .name
###########################################################################################################################################################
"""
class Animal1(object):
  is_alive = True
  health = ("good")

  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def description(self):
      print (self.name)
      print (self.age)
    
hippo = Animal1("Anderson", 36)
sloth = Animal1("Dale", 15)
ocelot = Animal1("Fuzzy", 7)

print (hippo.health)
print (sloth.health)
print (ocelot.health)

hippo.description()
"""
"""
zebra = Animal1("Jeffrey", 2, True)
giraffe = Animal1("Bruce", 1, False)
panda = Animal1("Chad", 7, True)

print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)
"""
###################################################################################################################
class ShoppingCart(object):
  
  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}
#
#
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print (product + " added.")
    else:
      print (product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print (product + " removed.")
    else:
      print (product + " is not in the cart.")

my_cart = ShoppingCart("Eric")
my_cart.add_item("Ukelele", 10)
################################################################################################################################
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print ("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print ("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
###############################################################################################################################
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
##################################################################################################################################
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print (milton.full_time_wage(10))
########################################################################################################################################
##################################################################################################
# You can directly access the attributes or methods of a superclass with Python's built-in super call
"""
class Derived(Base):#       accses super class
  def m(self):          #      \/
    return super(Derived, self).m()
         /\ also accses super class
"""
# Where m() is a method from the base class.
# You can directly access the attributes or methods of a superclass with Python's built-in super call.
####################################################################################################################################################
#######################################################################################################################################
class Triangle(object):
    number_of_sides = (3)
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == (180):
            return True
        else:
            return False
            
my_triangle = Triangle(30, 60, 90)

print (my_triangle.number_of_sides)
print (my_triangle.check_angles())



class Equilateral(Triangle):
  angle = (60)
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle
