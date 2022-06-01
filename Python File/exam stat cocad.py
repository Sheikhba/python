##############################################
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5] # here is a simple list with the verible grade
print ("Grades:", grades) # print statement we print Grades and the values in the verible grades
def print_grades(grades_input): #here we define a function called print_grades and give it one argument called grades_input
    for x in grades_input: # here we use a for loop to iterate through grades_input
        print(x) #then we print out what we have iterated through 

print_grades(grades) # here we call the function print_grades and give grades as its prameter
##########################################################################################################################################
##########################################################################################################################################
def grades_sum(scores): # define a function called grades_sum and give it one argument called scores
  total = 0 # total is equaled to 0 
  for score in scores:  #here we iterate through the argument scores 
    total += score # then we add the values from score to total
  return total # we return back to total

print (grades_sum(grades)) # here we are calling the function grades_sum and give grades as its parameters 
##########################################################################################################################################
##########################################################################################################################################
def grades_average(grades_input):# here define a function callded grades-averages and take 1 input grades_input
   sum_of_grades = grades_sum(grades_input)# here we make a new verible callled sum_of_grades which is assinged to the privious function called grades_sum and takes grades_averages argument grades_input
   average = sum_of_grades / float(len(grades_input)) # we then make a new verible called averages which is assinged to sum_of_grades divided by (/) float length grades_input  
   return average #we return to average   /\
                                #    float is used to make numbers in to decimal  
print (grades_average(grades))
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
def grades_variance(scores):# here we defin a function called grades_vaiance that takes one argument caled scores
    average = grades_average(scores) # here we make a new verible called averages that takes the privous function called grades_average and give iitt the argument scores
    variance = 0 # here we make a new verible called variance that is assinged to 0
    for score in scores: # here we use a for loop to iterate through scores
        variance += (average - score) ** 2 # here we minus average to score and then squre it then we add it all to variance 
    return variance / len(scores) # then we return variance divided (/) by the length of scores

print (grades_variance(grades))
#########################################################################################################################################################################################################################
#########################################################################################################################################################################################################################
def grades_std_deviation(variance): # here we defined  function called grades_std_diviation that takes one argument called variance 
     return variance ** 0.5 # we then return variance to square root 

variance = grades_variance(grades) # here we made a new verible called variance that takes the privious function called grades_variance but takes the argument grades

print (grades_std_deviation(variance))
#########################################################################################################################################################################################################################
#########################################################################################################################################################################################################################

