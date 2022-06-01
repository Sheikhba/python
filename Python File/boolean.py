########################################################################
#using boolean in python
# boolean is a type of data like string and interger
# there are only 2 type of value in boolean that is True and False
# you can use the built in type() function to find out what type of data it is

# like this
t = type("microsoft")
print (t)
t = type(1)
print (t)
t = type(True) # for boolean values True and Flse the first character has to be capital
print (t)
#a use of boolean

a = (3)
b = (1)

if a > b: # if true a is greater than b 
    print("a is greater than b") # then it will print this line
#################
# we can use this code instede and it does the same thing
# if True:
#    print("a is greater than b")

#############################################
boolean_value = a > b # here we are setting boolean_value to a is larger than b which sets boolean_value to true 
print(boolean_value) 
# so boolean value is set to True
if boolean_value: # since boolean_value is set to True we can use it here like previosly
    print("a is greater than b")
#######################################################################################################
def are_you_sad(is_rainy, has_umbrella): # defined a fnction called are_you_sad and set it to 2 arguments is_rainyand has_umbrella
    if is_rainy == True and has_umbrella == False: # here we use a if statement to check wether is_rainy is True and has_umbrella is False 
        return True # if the if statement execute with all condition met then it will return True 
    else: # if not it will 
        return False # return False
# you can write the if statement like this
    # if is_rainy and not has_uumbrella: ( this says if it is_rainy and not has_umbrella) 
# its more simpler

############################################################################################################
# if you wanted you can make the code much more shorter and simpeler
# like this
def are_you_sad(is_rainy, has_umbrella):
    return is_rainy and not has_umbrella # this basicly says this whole line will return true when is_rainy is True and has_umbrella is false

sad = are_you_sad(True, False) # here we are setting the argument is_rainy to True and has_umbrella to False in the function are_you_sad
print(sad)
# if i run this code it will return true 
