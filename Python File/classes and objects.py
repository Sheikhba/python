+#to make a class use built in function class and setbit to Robot caps on R
# \/    \/ 
class Robot:
    def introduce_self(self): # here we are making the function introduce_self with one argument called self
        print("My name is " + self.name) # self will refer to any object that we are running the previous function on
######## this code above is basicly a class
r1 = Robot()# this basicly says we are creating a new object called r1 with the class Robot
#to set atributes to the objects
r1.name = ("Tom")
r1.color = ("red")
r1.weight = 30
########this code above is an object
# to run this class and object
r1.introduce_self()
##############################################
# you can have multiple objects set to a class
r2 = Robot()
r2.name = ("Jerry")
r2.color = ("blue")
r2.weight =  40

r2.introduce_self()
#################################################################################
##########################################################################################################

#constructor
# make a cunstructor using __init__ it is a built in function which is used to make cunstructors
class Robot:    #\/ we still use self to know which object we are working with 
    def __init__(self, name, color, weight): #here we defined a function called __init__ with 4 argument 
        self.name = name # the values in the argument name are set into the object set name 
        self.color = color #
        self.weight = weight #

    def introduce_self(self): #then define a new function called introduce_self and give it one argument which is self 
        print("My name is " + self.name) 
####################################################################

#\/ name for the object befor the name of class
r1 = Robot("Tom", "red", 30)#same as the last object
r2 = Robot("Jerry", "blue", 40)#same as the last object
#             /\      /\    /\ 
#            name    color weight
#          these are set to the arguments in the function __init__
r1.introduce_self()# here we are calling the the function introduce_self which has allready set self.name to the name in the previos function
r2.introduce_self()
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
# here we are combineing the Robot class and the Person class and their objects so each person will have their own robot
# multiple classes and object can work togethr and interact together
class Person:
    def __init__(self, n, p, i): # < here we have built a cunstructor which is sort of same a the previous cunstructor
        self.name = n
        self.personality = p
        self.is_sitting = i
############################
    def sit_down(self):# here we have set a function called sit_down with one argument
        self.is_sitting = True # this sets self.is_sitting to true
 # true/false is boolean data type 
    def sit_up(self):
        self.is_sitting = False
###############################################################################
p1 = Person("Alice", "aggressive", False) # here we are seting the new objects p1 from class and used the cunstructor to give tem the attributes 
p2 = Person("Becky", "talkative", True)

p1.robot_owned = r2 # here we define a new atribute called robot_onwned in p1 and set it to r2
p2.robot_owned = r1 # here we define a new atribute called robot_onwned in p2 and set it to r1
######################################################################################
p1.robot_owned.introduce_self() # here the object p1 will bring up the attribute robot_owned which is r1 and the the function introduce_self from the first class
p2.robot_owned.introduce_self()
#############################################################################################################################################


