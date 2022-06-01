d = {                          # a typycal dictionry
  "Name": "Guido",
  "Age": 56,
  "BDFL": True
}
print  (d["Name"]) # here we are printing the dictioary d and the value from the key "Name"
print (d.items()) # here we use the built in function .items() to iterate through th dictionary d
# The method items() returns a list of dict's (key, value) tuple pairs
                                            #               /\
                                            # Tuples are sequences, just like lists
                                            # The differences between tuples and lists are, the tuples cannot be changed
                                            #unlike lists and tuples use parentheses, whereas lists use square brackets.
                                            # Creating a tuple is as simple as putting different comma-separated values

#######################################################################################################################################################################
#######################################################################################################################################################################
my_dict = {
    "Google": "supirior",    # here we have made a dictionary
    "Apple": "trillionair",
    "microsoft": "the biggining"
}
print(my_dict.items()) # here vwe print the dictionary with the .items function which iterate through it 
#######################################################################################################################################################################
#######################################################################################################################################################################
print(my_dict.keys())# here we use .keys built in function to print ot all the keys in that dictionay
print(my_dict.values())# sort of same as the last one except we use .values built in function which will print out all the values in the dictionary.  
#######################################################################################################################################################################
#######################################################################################################################################################################
for x in my_dict: # here we use  for loop to iterate through my_dict and set it to key
  print (x, my_dict[x]) # here we print out key in the dictionary then the value associated to that key
    #    /\       /\---------------------------------------\/
#     prints the key yhat is in the dictionary           prints the value in that key
#######################################################################################################################################################################
#######################################################################################################################################################################
# list comprehension
evens_to_50 = [i for i in range(51) if i % 2 == 0] #  here we use a for loop which iterates through the range and sets it to i we then use  if statement to check whether i divided by 2 equals 0 this shows its even this whole code is enclosed within the list evens_to_50
print (evens_to_50) # then we print the list  /\
#                                              |
#                                              |
#   -------------------------------------------|-------------------------------                                           
#  | here is an example of list comprehension we are generating a set of numbers
#  |0 to 50 to be exact but we only want the even numbers
#  | instede of writing all the numbers out we can use this type on code to generate the numbers
#######################################################################################################################################################################
#######################################################################################################################################################################
new_list = [x for x in range(1, 6)] # simple list comprehension we are making a list from 1 to 5
print (new_list)

doubles = [x * 2 for x in range(1, 6)] # more complex list comprehension before for the forloop we use * 2 to multiply the numbers by 2 
print (doubles)

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0] # here it is kind oof same as the last one but we check if the number divided by 3 is equaled to 0 after we doubled it
print (doubles_by_3)

even_squares = [x ** 2 for x in range (1, 12) if x % 2 == 0] # kind of the same concept but we are only squaring the number ** 2 and then we check if it is even be dividing it by 2 to se if it gives us a remainder of 0
print (even_squares)
########################################################################################################################################################################
########################################################################################################################################################################
cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0 ] # here we are cubeing the number ** 3 then we check whether the number is divisible by 4  
print (cubes_by_four)
########################################################################################################################################################################
########################################################################################################################################################################
# List Slicing Syntax
# lets you pick out  specific part of a list so yu could have the end of the list only or the biggining only or the middle
# this is the list slicing syntax format\/
#                               [start:end:stride]

# Where [start] describes where the slice starts (inclusive),
# [end] is where it ends (exclusive),
# and [stride] describes the space between items in the sliced list. (space after each index )

# For example,
# a stride of 2 would select every other item from the original list to place in the sliced list.


l = [i ** 2 for i in range(1, 11)] # simple list comprehension
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#     \/-------------------list veribles
print (l[2:9:2])
#        /\___/\--- here we are sliceing the list 
#       starting from 2 till 9 incrementing in 2
########################################################################################################################################################################
########################################################################################################################################################################
my_list = [i for i in range(1, 11)] # here is basic list comprehension that i used to make alist from 1 to 11

print (my_list[::2]) # [1, 3, 5, 7, 9]
#here we use a list slicing techniques to print out only the odd numbers
# we are able to do this by the use of stride [start:end:stride]
# here stride is set to 2 as we did set the stride to print
#it will print out every second number

# when using list slicing [start:end:stride] if we want to use the whole list
# we can leave the start and end empty BUT LEAVE THE COLONS that by default includes the whole list
#########################################################################################################################################################################
#########################################################################################################################################################################
# Reversing a List

letters = ['A', 'B', 'C', 'D', 'E']
print (letters[::-1]) # here useing -1 will print out the list from right to left
# reversed
my_list = [i for i in range(1, 11)] # here is basic list comprehension that i used to make alist from 1 to 11

backwards = (my_list[::-1]) # then we set the list to  verible called backwards we also use -1 to print the list right to left reversed 

print (backwards) # then we print the verible
#########################################################################################################################################################################
#########################################################################################################################################################################    

to_one_hundred = [i for i in range(101)] # list comprehension

backwards_by_tens = (to_one_hundred[::-10])
# here we have a new verible called backwards_by_ten and we set it to to_one_hundred
#we slice the list from the biggining to the end with a stride of -10 this will give us all the tenth value in the list like so

print (backwards_by_tens) # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
#########################################################################################################################################################################
#########################################################################################################################################################################    

to_21 = [i for i in range(1, 22)]
# here is a list comprehension eccept the range has (1, 22) instede of just 22' including 1 will make the list start at 1 insteade of 0
odds = (to_21[::2]) # we slice the list to_21 bigging to the end in stride 2 so we miss all the even numbers and leave the odd numbers
# here we use a new verible and set it to to_21
middle_third = (to_21[7:14:]) # we slice the list to_21 from 7 to 14 as indexes ths would be the middle of the list
# here we have a new verible called middle_third that is set to to_21 
#########################################################################################################################################################################
#########################################################################################################################################################################    
# lambda

my_list = [i for i in range(16)] # simple list comprenhension
#       
print (list(filter(lambda x: x % 3 == 0, my_list)))
#/\ here we filter through the list comprehension and print it out 
#########################################################################################################################################################################
#########################################################################################################################################################################    
languages = ["HTML", "JavaScript", "Python", "Ruby"]

print (list(filter(lambda x: x == "Python", languages)))
#########################################################################################################################################################################
#########################################################################################################################################################################    
squares = [x ** 2 for x in range(1, 11)]

print (list(filter(lambda x: x >= 30 and x <= 70, squares)))
#########################################################################################################################################################################
#########################################################################################################################################################################    
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
print (movies.items()) # here we use .items()to iterate through the dictioary movies
#########################################################################################################################################################################
#########################################################################################################################################################################    
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]# here is a list comprehension 
                     #                                    /\_______the use of (or) makes it so that it will only show number that are etheir equally divisible by 3 or 5 
print(threes_and_fives)
#########################################################################################################################################################################
#########################################################################################################################################################################    
# List Slicing
garbled = ("!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI")
#                   \/ the stride is set to -2 so it will take the list backwards with a space of 2
message = (garbled[::-2])
print (message)
#########################################################################################################################################################################
#########################################################################################################################################################################    
garbled = ("IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX")
#                                  \/ here we check whether x is not equalled to "X" and then they set it to message
message = (list(filter(lambda x: x != "X", garbled))) # 
print (message)         #              
#########################################################################################################################################################################
#########################################################################################################################################################################    
