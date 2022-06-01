####################################################################################################
####################################################################################################
# lambda is  operator or function
# able to create function without name

# functional programming, which means that you're allowed to pass functions around
# just as if they were variables or values. 

# Lambda functions are mainly used in combination
# with the functions filter(), map() and reduce().

########
# An anonymous inline function consisting of a single expression
# which is evaluated when the function is called.
# The syntax to create a lambda function is lambda [arguments]: expression 

###########
  #\/--------------------------------dont have to give it a function name
# lambda x: x % 3 == 0               it will still return a value
# lambda creates is an anonymous function.

  #\/
#is the same as
  #\/

#       \/--------------function name              
#def by_three(x):
  #return x % 3 == 0
#   /\------------------------if you call he function name it will ru through that script and return that value 
###################

my_list = [i for i in range(16)]

print (list(filter(lambda x: x % 3 == 0, my_list)))
# when using filter(), map() and reduce() you must add the list function before it to make it work

# When we pass the lambda to filter, filter uses the lambda to determine what to filter,
# and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.

# Lambdas are useful when you need a quick function to do some work for you.

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print (list(filter(lambda x: x == "Python", languages)))
# filters can be used with string
#################################################################################
#  LAMBDA SYNTAX
# lambda [arguments]: expression
# example
                        #  \/-----what we are going to do with the argument 
#verible| |argument| |expression|
#\/          | \/ | |  \/  |
add = (lambda x, y : x + y) # this whole lise act as a function and return 
#argument x   y     
#         \/  \/ 
print (add(2, 3))# here we are printing out what is in the verible add

p = type (add)
print (p)
##################################################################################
# FILTER SYNTAX
# filter(function, iterable)

# function - function that tests if elements of an iterable returns true or false
#If None, the function defaults to Identity function - which returns false if any elements are false

# iterable - iterable which is to be filtered,
#could be sets, lists, tuples, or containers of any iterator

#THE FILLTER FUNCTION RESEMBLES A FOR LOOP BUT FASTER ITS A WAY TO ITERATE THROUGH THINGS BUT FASSTER
hello1 = ("Hello")
hello = (list(filter(None, hello1)))
print (hello) # ['H', 'e', 'l', 'l', 'o']
