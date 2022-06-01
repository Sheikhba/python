count = 0

if count < 5:
  print ("Hello, I am an if statement and count is", count)

while count < 10: # As long as count is less than 10 it wll continue to print.
  print ("Hello, I am a while and count is", count)
  count += 1

# while loop will continue to execute as long as the condition is true.
# In other words, instead of executing if something is true,
# it executes while that thing is true.
#############################################################
loop_condition = True # verible set to true 

while loop_condition: # the whlile loop is set too defult to only accept True 
  print ("I am a loop")
  loop_condition = False # the verible is set to false so the while loop stop because it is set to find a verible set to true

# The condition is the expression
# that decides whether the loop is going to continue being executed or not.
# there are 5 step
# The loop_condition variable is set to True

# The while loop checks to see if loop_condition is True. It is, so the loop is entered.

# The print statement is executed.

# The variable loop_condition is set to False.

# The while loop again checks to see if loop_condition is True. It is not, so the loop is not executed a second time.
############################################################################################


choice = input('Enjoying the course? (y/n)') # here we asking the users input

while choice != 'y' and choice != 'n':  # here we check wheather the user put a y or a n as answer
  choice = input("Sorry, I didn't catch that. Enter again: ") # if they didnt it will ask the to enter again and will check again if they put y or a n
###############################################################################################
count = 0 # count set to 0

while count < 10: # if count smaller than 0
    print (count) # print this statement
    count += 1 # add 1 to count
####################################################################################

count = 0 #count is set to 0

while True: # the while loop is set to true 
  print (count) # we print the value of count
  count += 1 # we increment the value of count by 1
  if count >= 10: # we use a an if statement to check wheather if the value of count is larger or equal to 10
    break # if it is then we break the if statement
###############################################################################################

import random # we using the module random

print ("Lucky Numbers! 3 numbers will be generated.") # normal print statement
print ("If one of them is a '5', you lose!") # normal print statement 

count = 0 # count is valued to 0 this is to make sure that we pick 3 random numbers  
while count < 3: # we a while loop and make sure that count is set to lower than 3 so we only get 3 numbers
  num = random.randint(1, 6) # here we pick a rando number between 1 to 6 and asig that number to the verible num
  print (num)
  if num == 5: # here in the if statement we check whether the random number that was picked is 5
    print ("Sorry, you lose!") # if te random number is a 5 then it will print this statement
    break # and it will break the for loop    
  count += 1 # here we increment count so it will pick another random number 
else: # if it is any other number then it is okay 
  print ("You win!")
# else block are executed anytime when evaluated as false  
######################################################################################################
  
from random import randint  # her we are gettin a specific function from a module in this case we are getint the function randint from the module random
    #module      #function  

random_number = randint(1, 10) # picking a random number and asinging it to random_number

guesses_left = 3 # we asinge 3 to guesses_left this is to make sure that the user only gets 3 guesses
while guesses_left > 0: # the while loop make sure that the value of guesses left is larger than 0
  guess = int(input("Your guess: ")) # here we ask for the user input making sure thst it is a number we se int() to make sure that the user puts in a number
  if guess == random_number: # we use a if state ment to check weather the user guess is equal to the random_number 
    print ("You win!") # if it is you win
    break # and the code breaks
  guesses_left -= 1 # if you get it wrong your guess reduces by 1
else: # if you guess the wrong the number 
  print("You lose.") # it prints that you lose
##########################################################################################################
hobbies = [] # here is empty list to store the hobby


for i in range(3): # for loop to run a set of code for a specific amount of time
  hobby = input("Tell me one of your favorite hobbies: ") # ask te users hobby
  hobbies.append(hobby) #put the hobby in to the list

print(hobbies) # printing the list
#####################################################################################################

thing = ("spam!") # here we set string to the verible thing

for i in thing: # here we use a for loop to iterrate through everything in the verible thing
  print (i) # then we print out wht we iterated


word = ("eggs!") # here we set string to the verible word

for i in word: # here we use a for loop to iterrate through everything in the verible word
  print (i) # then we print out wht we iterated
#####################################################################################################################


word = ("Marble")
for char in word:
  print (char)
###########################################################################################################################

phrase = ("A bird in the hand...")


for char in phrase:
  if char == ("A") or char == ("a"):
    print ( "X", end="")
  else:
    print ( char, end="")
    
# look into   , end=""  anotate later
####################################################################################################################

numbers  = [7, 9, 12, 54, 99] # here we set a few numbers in to a list that we have asinged to the verible numbers

print ("This list contains: " ) # typical print statement

for num in numbers: # for loop which iterate through the values in the verible numbers
  print (num) # here we print the values that we iterated through
for num in numbers: # here we iterate through the values again
  print (num**2) # we print the same thing eccept that we only squre the numbers in the proces
#######################################################################################################################
print(end="\n")

d = {'x': 9, 'y': 10, 'z': 20} # here we make a dictonary and assing it to the verible d
for key in d: #here we use a for loop which itrerate the keys in the dictonary assinged to d, we then assinge the thing that we iterate to the verible key  
  if d[key] == 10: # here we use a if statement to check if any of those key that we iterated through have the value 10 
    print ("This dictionary has the value 10!") # if it does it wiill print this statement

print(end="\n")

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'} # here is a dictinary that is assinged to the verible d 

for key in d: # here we iterate through the keys in the dictonary that is assinged to d we then assinge them to the verible key  
  print (key, d[key]) # here we are simply printing out the key and then the associated value to it
#       #key###value
########################################################################################################
print(end="\n")
choices = ['pizza', 'pasta', 'salad', 'nachos'] # here is a simple list assinged to the verible chocies

print ('Your choices are:') # print statement
for idx, item in enumerate(choices): # here is a for loop that usees 2 built in function idx and enumerate enumerate allows you to supply the corosponding list an index and idx allows you ot change that index if you wish
  print (idx + 1, item) # here index (idx) has + 1 this will add 0ne to the index that will be added so it wont start from 0 but from 1
# enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater
################################################################################################################################
print(end="\n")
#                        \/
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
#                       /\
# zip put 2 or more list together and at the shorter one for both of the list 
for a, b in zip(list_a, list_b): #zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list in this case it will stop at the end of list_a and on list_b it will stop the same place up to 3o
  big = max(a, b) # max will find the giggist number in both the list
  print (big, end=",")
"""
str(list_a)
str(list_b)

for a in (list_a):
  print (a, end=",")
  
print (end="\n")

for b in (list_b):
  print (b, end=",")
  
 

print (end="\n")
print (end="\n")
"""

############################################################################################################################
print(end="\n")# line break
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape'] # string

print ('You have...') # print statement
for f in fruits: # for loop iterates through the list fruits sets it to f
  if f == ('tomato'): # if f contains tomato
    print ('A tomato is not a fruit!') # it will print his
    break # and break the for loop
  print ('A', f) # if for loop dosent break then it will print A, and the fruits name
else: # else statement
  print ('A fine selection of fruits!') # if for loop dosent break then it will print this 
######################################################################################################################################
# same code as above slight difference
print(end="\n")
print(end="\n")
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
  if f == ('tomato'):
    print ('A tomato is not a fruit!') # (It actually is.)
    #no break function
  print ('A', f)
else:
  print ('A fine selection of fruits!')
####################################################################################################################
print(end="\n")
print(end="\n")
google = list() # empty list
for i in range(3): # for loop which will count to 3
  user = input("what do you want") # ask the user what they want
  if user == "cat": #if user respons is cat
    break # it will break for loop
  else: # else statement
    google.append(user) # .append built in function, add user input to google  
print(google, end="") #print list
#######################################################################################################################
