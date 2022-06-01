print(end="\n")
print(end="\n")
#to check whether the number is even
def is_even(x): # defined function called is_even with 1 argument called x
  if x % 2 == 0: # if x is dividble by 2 and has a remainder of 0
    return True #return true
  else:# else statement
    False # else return false
######################################################################################################################################
#this peice of code check wheather the number is an interger a whole number number without a decimal eccept numbers that have a "0" to the right like thes 6.0 they will be considerd an interger including negative numbers
# number with decimal ecept number tat end in .0 are not intergers    
print(end="\n")
print(end="\n")
def is_int(x): # defined function called is_int with one argument x
  absolute = abs(x) # abs pre defined function we find the adsolute value of x and assinge that to the verible absolute
  rounded = round(absolute) # find the rounded number of absolute and assine it to rounded
  # round built in function will round any decimal to its nerest interger eg 1.2 will be 1, 1.5 will be 1, 1.6 will be 2 and 1.9 wil be 2
  return absolute - rounded == 0 # here we check whether the number is a whole inerger by minusing absolute to rounded  and if it equals 0 its a interger  
# if x is a decimal it will say false
# if x is a interger then will say true 1.0 count as intergers as they are same as 1 
################################################################################
# this add all the numbers that you set in x
print(end="\n")
print(end="\n")
def digit_sum(x): # defined function called digit_sum with one argument called x
    total = 0 # total is set to 0
    while x > 0: # if x is larger than 0
        total += x % 10 #divide x by 10 and assine it to total 
        x = x // 10 #divide x by 10 with floor division give you a intger set that interger to x 
        # // floor division gives you a whole number instede of a dicimal number thst you might get from a singular / division
        print (x) # prints value in x 
    return total #returns to total
# % shwos the remainder of the division not answer eg 3 % 2, 3 goes into 2, 1 with 1 remainder
# / basic division
# // basic division but it removes all decimal so your left with the first number
###########################################################################################################
 # this will times a singel number all the way down to 1
print(end="\n")
print(end="\n")
def factorial(x): #we define a function called factorial and give it one argument called x 
    total = 1 # total set to 1
    while x > 0: # if x is larger than 0
        total *= x # multiply total by x and set it to total
        x -=1 # minus 1 to x
    return total # start the while loop again again
###############################################################################################################################
# this code check whether the number that picked is a prime number
print(end="\n")
print(end="\n")
def is_prime(x): # here we define a function called is_prime and give it one argument called x
    if x < 2: # here we check whether x is smaller than 2 using if statement
        return False # if it is then it will return false
    else: # if not it will continue to a else statement
        for n in range(2, x-1): # we uses a for loop to build a range from 2 to x-1
          # we go lower than the x so we check all the numbers from 2 to the number bellow x so we check which  
            if x % n == 0: # with this if statement we are checking if x divided by any number between 2 to x-1 which is n has a remainder of 0 
              # here we have established another if statement which is within a forloop and the forloop is in a else statement
                return False #if it does it will return false as it isnt a prime 
        return True #if not it will return true
################################################################################################################################################################
# this will reverse any text tthat you insert
print(end="\n")
print(end="\n")
def reverse(text): # here we have defined a function called reverse and gave it one argument called (text)
    word = "" #word is set to an empty string
    l = len(text) - 1 # here we establish a new verible called 1 and set it to yhe length of the text - 1 we romove 1 from the text inde
    while l >= 0: #here we use  while loop to check whether he content of 1 is larger or equal to 0
        word = word + text[l] # if it is then we get the empty string word we add the text first index to word and add thet to word
        l -= 1  #we minus 1 from the verible 1
    return word # then we return Back to word and start it all over again 


#7/15 practice make perfect
##########################################################################################################################################################
# this remove all vowles
print(end="\n")
print(end="\n")
def anti_vowel(text): # here we have defined a function called anti_vowel and gave it one argument called text
    t = "" # here we have put t in a empty string
    for c in text: # here we use a for loop to iterate throgh the content of text  
        for i in "ieaouIEAOU": # here we have used a for loop which is with in the previous for loop to itate through the all the vowel upper and lowwer case   
            if c == i: # here we use an if statement to compare the text for loop and the vowel forloop to see if any of them match
                c = "" # if they do match then we then we remove them from c 
            else:
                c=c # if not then c is kept the same
        t=t+c #depending on the if/else statement c is added to t then it is assinge it to t  
    return t # then we return to t
############################################################################################################################################################################
print(end="\n")
print(end="\n")
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10} # a dictionary that has a lletter as a key and a number for its value
def scrabble_score(word): #here we have defined a function called scrabble_score that takes one argument called word 
  word = word.lower() # here we use .lower() on word so incase we use any upper case letters it will be turened to lower case by deafeult then we asine that right back to word 
  total = 0 #here we have a verible called total with the value 0
  for letter in word: # here we are using a for loop to iterate through the string in word and assine it to letter
    for leter in score: #here we use another for loop within the previos for loop to iterate through score and assine it to leter 
      if letter == leter: #here we use a if statement to check if letter from the first for loop is equaled to the leter in the second for loop (if the word is equaled to the key in score)   
        total = total + score[leter] #if the if statement dose execute then we add the score value to total and assine it back to total   
  return total # we then return backto total and start it all over again
#############################################################################################################################################################################################################  
# here we replace any word that we look for with an * 
print(end="\n")
print(end="\n")
def censor(text, word): # here we define a function called censor and give it 2 function called text and word 
    words = text.split() #here we have a new verible called words that is assined to text  and we use a built in function called .split() to split text
    result = "" # here we have made a new verible called result  that is assined to an empty string 
    stars = "*" * len(word) # here we have assined a new verible called stars that is assined to a single * which is multipleied by the length of the argoment word
    count = 0 # here we set a new verible called count which is set to 0
    for i in words: # here we use a for loop to iterate through words which has been set to text.split  
        if i == word: # here we check whether i (i is the iterated value of words) is equal to the argument word 
            words[count] = stars #if the if statement does execute we are replace all the words that are equal to word with stars
        count += 1 #then we add 1 to count
    result =' '.join(words) # then we join words together and assine it to result

    return result #then  we return to result 
##########################################################################################################################################################################################################
#this will be able to find the amount of numbers that there is in a list 
print(end="\n")
print(end="\n")
def count(sequence, item): # here we define a function called count an give it 2 argument called sequence and item
    count = 0 #here we make a new verible called count and ssine it to 0
    for i in sequence: # here we use a for loop to iterate through sequence
        if i == item: # here we check whether the item we are looking for is in the iterated sequence
            count += 1 #if it is we add 1 to count
    return #count then we return back to count
###########################################################################################################################################################################################################################
# this will remove all odd numbers that would be in a list and will leave only the even numbers
print(end="\n")
print(end="\n")
def purify(lst): # here we define a function called purify with one argument called 1st
    res = [] # here we have a verible called res with an empty list
    for ele in lst: # here we use a for loop to itrate through 1st
        if ele % 2 == 0: # here we check if the numbers that we iterated through are even  
            res.append(ele) #if they are then we add them to res 
    return res # then we return back to res 
#p = purify([1, 2, 3, 4, 5])
#print(p)
##################################################################################################################################
#this will multily any set of numers in a list 
print(end="\n")
print(end="\n")
def product(list): # here  we have dfined a function called product which we gave it takes one argument called list
  total = 1 # here we have a verible called total which we assinged it to 1
  for num in list: # here we have a for loop which will iterate through list 
    total = total * num #here we multiply total by num and num being the iterated alues in list 
  return total # then we return back to total 
#p = product([1, 2, 3, 4])
#print (p)
####################################################################################################################################################################
# this will remove any duplicat numbers in a list
print(end="\n")
print(end="\n")
def remove_duplicates(inputlist): # here we define function called remove_duplicates and give it on argument called inputlist
    if inputlist == []: # here we use a if statement to have iinputlist equalled to an empty list
        return [] # then we return back to the empty list
    
# Sort the input list from low to high    
    inputlist = sorted(inputlist) # here we sort the numbers using the built in sorted function
# Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]] # here we make a new list called outputlist and assinge it to the first index value of inputlist 

# Go through the values of the sorted list and append to the output list
# ...any values that are greater than the last value of the output list
    for i in inputlist: # here we iterate through inputlist
        if i > outputlist[-1]: # here check if any of the value of i (the iterated values in inputlist) is larger than outputlist
            outputlist.append(i) #if it is then we add it to outputlist 
        
    return outputlist #then we return back to output list
##################################################################################################################################################################
print(end="\n")
print(end="\n")
def median(lst): # here we define a function called median with a argument called lst
    sorted_list = sorted(lst)#then we sort lst and assinge it to sorted_list  
    if len(sorted_list) % 2 != 0: # then we use a if statement to get the length of the sorted_list then we check if dividing it by 2 will or will not give us a remainder of 0
        #odd number of elements # ^ we check for th odd number odd number dont fully dived by 2
        index = len(sorted_list)//2 # then we do floor division to th length of sorted_list to 2
        return sorted_list[index] # then we return to sorted list and index
    elif len(sorted_list) % 2 == 0:  # then we use a if statement to get the length of the sorted_list then we check if dividing it by 2 will or will not give us a remainder of 0
        #even no. of elements # ^ we check for th even number even number dont fully dived by 2
        index_1 = len(sorted_list)/2 - 1 # here we made a new verible called index_1 which we set to the length of sorted_list divded by 2 -1
        index_2 = len(sorted_list)/2     # here we made a new verible called index_2 which we set to the length of sorted_list divded by 2 -1
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0 # here we make a new verible called mean which we set to  sorted_list[index_1] plus sorted_list[index_2] divided by 2.0
        return mean # then here we return to mean
   
print median([2, 4, 5, 9])
