lloyd = {
  "name" : "Lloyd",
  "homework" : [], # [] squre bracket in dictionaries next to a key means empty value
  "quizzes" : [],
  "tests" : []
}
# indentation must be on point
alice = {
  "name" : "Alice",
  "homework" : [],
  "quizzes" : [],
  "tests" : []
}

tyler = {
  "name" : "Tyler",
  "homework" : [],
  "quizzes" : [],
  "tests" : []
}
##################################################################
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],                          
  "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]

print (lloyd["name"])
print (alice["name"])#in these 4 block of code we are just printing out all the keys in the dictionaries 
print (tyler["name"])

print (lloyd["homework"])
print (alice["homework"])
print (tyler["homework"])

print (lloyd["quizzes"])
print (alice["quizzes"])
print (tyler["quizzes"])

print (lloyd["tests"])
print (alice["tests"])
print (tyler["tests"])


def averag(number):  
  total = sum(number) # sum just add the numbers in tthe argument number together and assinge it to total
  total = float(total) # we get the numbers in total and use float which will make them a decimal and then reassinge thatto total
  return total / len(number) #here we are deviding total by the length of the numbers


def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  
  total = homework *.1 + quizzes * .3 + tests * .6
  return total


def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >=80:
    return "B"
  elif score >=70:
    return "C"
  elif score >=60:
    return "D"
  else:
    return "F"
  
print (get_letter_grade(get_average(lloyd)))
print (get_letter_grade(get_average(alice)))
print (get_letter_grade(get_average(tyler)))


def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

students = [lloyd, alice, tyler]

print (get_class_average(students))




