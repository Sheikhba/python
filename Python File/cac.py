

pop = 2

lol = "2"

print (str(pop))
print (str(lol))

pop = "Hello"
print (pop.upper())


ministry = "The Ministry of Silly Walks"

print (len(ministry))
print (ministry.upper())


print ("Monty Pytho")

the_machine_goes = ("ping!")

print (the_machine_goes)


print ("Spam " + "of " + "eggs")


print ("The value of pi is around " + str(3.14))

string_1 = "Camelot"
string_2 = "place"

print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))



print ("I am a {type}".format(type="string"))
my_name = "Michael"
print ("Hello, my name is {name}".format(name=my_name))




name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))



my_string = "fhjfhhgjhgf"
print (len(my_string))
print (my_string.upper())


from datetime import datetime
now = datetime.now()
print (now)


from datetime import datetime
now = datetime.now()
print (now)
print (now.year)
print (now.month)
print (now.day)


from datetime import datetime
now = datetime.now()

print ('%s/%s/%s' % (now.month, now.day, now.year))

from datetime import datetime
now = datetime.now()

print ('%s:%s:%s' % (now.hour, now.minute, now.second))




from datetime import datetime
now = datetime.now()

print ( '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))

print ('Welcome to the Pig Latin Translator!')


original = input("Enter a word:")
if len(original) > 0:
  print ("the user's word")
  
else:
    print ("empty")




original = input("Enter a word:")
if len(original) > 0:
  print (original)
  
else:
    print ("empty")











print ('Welcome to the Pig Latin Translator!')


original = input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print (original)
else:
    print ("empty")



    
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    print (word, first)

    print (original)
else:
  print ('empty')



pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  print (new_word)
else:
    print ('empty')




"""Well done! However, now we have the first letter showing up both at the beginning and near the end.

s = "Charlie"

print s[0]
# will print "C"

print s[1:4]
# will print "har"
First we create a variable s and give it the string "Charlie"
Next we access the first letter of "Charlie" using s[0]. Remember letter positions start at 0.
Then we access a slice of "Charlie" using s[1:4]. This returns everything from the letter at position 1 up till position 4.
We are going to slice the string just like in the 3rd example above."""


pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print ('empty')







def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print ("With tax: %f" % bill)
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print ("With tip: %f" % bill)
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)





def spam():
  """print eggs"""
  print ("Eggs!")
spam()



def square(n):
  squared = n ** 2
  print ("%d squared is %d." % (n, squared))
  return squared
square(10)






def power(base, exponent):  
  result = base ** exponent
  print ("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)




def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2


def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")



def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False




from math import sqrt
print (sqrt(25))

import math
print (math.sqrt(25))

"""how to use all all variales and function in a module but not write the module in front of the function or variables"""
"""Universal import can handle this for you. The syntax for this is:
 any module like math or anything"""
     #\/
     #\/ 
#from module import *



    
"""If you have a function of your very own named sqrt and you import math, your function is safe:
there is your sqrt and there is math.sqrt. If you do from math import *, however,
you have a problem: namely, two different functions with the exact same name."""





import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print (everything) # Prints 'em all!



maximum = max(43, 50, 100, 600,)
"""max() ... if you type any whole number in the bracket of max() the max function will pick the number that is the highest in the bracket"""
print (maximum)

minimum = min(40, 40, 30, 20, 6, 7, 1, 0)
"""min() ... if you type any whole number in the bracket of min() the min function will pick the number that is the smallest in the bracket"""
print (minimum)

absolute = abs(-42)
"""abs() ... the abs() function find the absolute value of a number distance to 0
lets say you put the number 5 in to the bracket of the function abs() it will return you 5, it takes you to count 5 from 0 to get to 5 this works with - + numbers"""
print (absolute)


# type() function finds the data type of anything that you put in to python 
print (type(42))#interger no qoute mark only whole number
print (type(4.2))#float a decimal number no qoute number
print (type("pop"))#anthing with qoute marks




def shut_down(s):
  if s == "yes":
    return ("Shutting down")
  elif s == "no":
    return ("Shutdown aborted")
  else:
    return ("Sorry")




from math import sqrt
print (sqrt(13689))

import math
print (math.sqrt(13689))

def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return ("Nope")



def hotel_cost(nights):
  return 140 * nights
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost
def trip_cost(city, days,spending_money ):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


print (trip_cost("Los Angeles", 5, 600))












