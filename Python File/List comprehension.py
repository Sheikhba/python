#####################################################################################
#List Comprehension
a = [1, 3, 5,7, 9, 11]
# we want to make a new list which is double of previous
 # [2, 6 ,10, 14, 18, 22]
# we can use the .append function to do this

# b = []
# b.append(10)
# b.append(20)
# print(b)

# like this
c = [] # this is a empty list
for x in a: # here we iterate through a and set it to x 
    c.append(x * 2) #then we times we times x by 2 doubling it and then adding it to c 
print(c)# then we prnt it out
#/\           /\
#you can do the same thing using a list comprehension

# like this
d = [x * 2 for x in a] # this says d is a list where each element is going to x times 2 for each x in a
print(d)

e1 = [x ** 2 for x in range(1, 7)] # this is kind of the same as the last one but we are squaring the numbers and we used a range of 1 to 7 
print(e1)                #   /\ this range is between 1 to 7 but not incliuding 7 so only 1 to 6


#if we wanted to do the same thing except back ward somthing like this
# [36, 25, 16, 9, 4, 1]
# we would have to do a reverse range llike this
for x in range(6, 0, -1):
    print(x)# /\ /\  /\
#this says  start at 6 end at 0 not including 0 so it is 6 to 1 and the -1 means decreasing or going downwards

f1 = [x ** 2 for x in range(6, 0, -1)]
print (f1)
# same list comprehension except backwards 
###############################       _________any kinde of value can go in to the list string interger bolean 
# list comprehensin format \/       \/   \/-------------------you can add ny other if statement wether you want to lie if statement 
#          list_name[x for x in ########   ]
#                   /\    /\----------------------
# (what do yo want to do to the value in list)]  |
#                                                |
                                    #(for loop to iterate through the value)
