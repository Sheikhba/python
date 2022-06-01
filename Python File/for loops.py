#for loop can be used in   ()   []   {}



names = ["Adam","Alex","Mariah","Martine","Columbus"] #[]
for names in names:
  print (names)



names = ("Adam","Alex","Mariah","Martine","Columbus") #()
for number in names:
  print (names)






webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

for word in webster:
  print (webster[word])








a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for a in a:
  if a % 2 == 0:
    print (a)







a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
  if number % 2 == 0:
    print (number)



def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count








for letter in "Codecademy":
  print (letter)
    


word = "Programming is fun!"

for letter in word:
  if letter == "i":
    print (letter)







prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for food in prices:
  print (food)
  print ("price: " %s  prices [food])
  print ("stock: " %s  stock [food])

total = 0
for food in prices:
  print (prices[food] * stock[food])
  total = total + prices[food] * stock[food]
print (total)








shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}


def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total




