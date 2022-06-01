total = 0              
for i in range(1, 5):  #gets all the numbers from 1 to 5 but not including 5
    total += i         # the total which is 0 adds all the numbers with the += and puts the answer in the total verible
print (total) # it will print 10 cuz 1 + 2 + 3 + 4 = 10
              #not including 5
################################################################################

total2 = 0
j = 1
while j < 5:    #whille loop will run the same pice of code till it has to break like here after the while j < 5 until j is not smaller than 5 it will stop running that code
    total2 += j #here it will add total2 to what ever j is which is 1 then it will put that number in to total2      
    j += 1      # here j is adding 1 every time it runs the code and they put that number back in to j
    print(j)
print(total2)
###################################################################################

#here we are adding only the numbers that is larger than 0 basicly not negative
given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total3 = 0
i = 0 # the i verible will be used for you index in the list and be used alongside the verible given_list[i] wher the i verible will be in the squre bracket
while i < len(given_list) and given_list[i] > 0: # here it says that if the given index on given_list is larger than 0 then it should continue
    total3 += given_list[i] # add the number that is larger than 0 to total3
    i += 1 # then move on to the next index by addin on 1 goes to the next item
print(total3) #this will give us 17 because it will only add 5 + 4 + 4 + 3 + 1 as they are only larger than 0

 #  after the while word there is a special code ( i < len(given_list) and ) this code allows us to no get an error when the list dosenot contain any negatie numbers
 #   it does this by checking the length of the list with the len code

 ################################################################################################
 
given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list2: # here its going to add up all the ellements in given_list to total4 it will add both + - numbers
    if element <= 0: # if you wanted to add only the positive numbers then wee can do this line of code here we are checking if the element in given_list is larger thanor equals to 0
        break # if it is larger than or equals to 0 then we break the code with the in built code break which will break out of the for loop
    total4 += element # here its just adding it into total 4
print (total4) # this will give us 17 because it will only add 5 + 4 + 4 + 3 + 1 as they are only larger than 0

#####################################################################################################################################
# the break code can be used in while loops

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total5 = 0
i = 0
while True: # here we made the while True 
    total5 += given_list2[i] # here we are saying add the current element in given_list 2 and put it in to total5
    i += 1 # here increment i by 1
    if given_list2[i] <= 0: # if you wanted to add only the positive numbers then wee can do this line of code here we are checking if the element in given_list2 is larger than or equals to 0
        break # if it is larger than or equals to 0 then we break the code with the in built code break which will break out of the for loop
print(total5) # this will give us 17 because it will only add 5 + 4 + 4 + 3 + 1 as they are only larger than 0


##############################################################################################################################


a = ["apple", "banana", "republic"]
print (a) # this will print whats in verible a that include the [] "" , the symbols
for element in a: # here we used a simple for loop statement to iterate through everything in a
    print(element) # this will print the words in a ( apple banana republic ) in a descending order and without the symbole [] "" ,

###############################################################################################################################################

for i in range(0, 3):
# for i in range(3): <<<  this dose the same as the code above except its without the 0
    print(i) # this will print 0 1 2 in descendingg order it does not  count the 3 as it is going from index so 0 = 1|1 = 2|2 = 3 and our range is 3 as index  

###########################################################################################################################

for i in range(len(a)): #ths does the same thing as the top line of code it only it will know the length of a 
    for j in range(i + 1) # this is a for loop wiithin a for loop it will help us print apple once banana twice and republic three times this will be done through the index:
    # i = 0 -> j = 0 "apple"
    # i = 1 -> j = 0, 1 "banana" x2
    # i = 2 -> j = 0, 1, 2 "republic" x3
    print (a[i])


