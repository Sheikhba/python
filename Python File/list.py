zoo_animals = ["pangolin", "cassowary", "sloth", "snake" ];

if len(zoo_animals) > 3:
  print ("The first animal at the zoo is the " + zoo_animals[0])
  print ("The second animal at the zoo is the " + zoo_animals[1])
  print ("The third animal at the zoo is the " + zoo_animals[2])
  print ("The fourth animal at the zoo is the " + zoo_animals[3])




numbers = [5, 6, 7, 8]

print ("Adding the numbers at indices 0 and 2...")
print (numbers[0] + numbers[2])
print ("Adding the numbers at indices 1 and 3...")
print (numbers[1] + numbers[3])



zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
print (zoo_animals)

zoo_animals[2] = "hyena"

zoo_animals[3] = "lion"

print (zoo_animals)



letters = ['a', 'b', 'c']
letters.append('d')
print (len(letters))
print (letters)



suitcase = [] 
suitcase.append("sunglasses")

suitcase.append("underwear")
suitcase.append("bathing suit")
suitcase.append("clothe")

list_length = (len(suitcase)) 

print ("There are %d items in the suitcase." % (list_length))
print (suitcase)

"""
letters[1:3]. In Python, when we specify a portion
of a list that we want to splice the first index number,
we include the element with the first index, 1,
but we exclude the element with the second index, 3.
"""





            # 0 counts
                 #0         #1      #2           #3      #4       #5
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first = suitcase[0:2] #prints 0 1
print (first)

middle = suitcase[2:4]#prints 2 3
print (middle)

last = suitcase[4:6] #prints 4 5
print (last)

#string index works with individual charachters

#          0123456789
animals = "catdogfrog"
print (animals)

cat = animals[:3]
print (cat)

dog = animals[3:6]
print (dog)

frog = animals[6:10]
print (frog)







animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]


"""
to find the index of anything in a list you can use  .index()   as a way to find it
"""
duck_index = animals.index("duck")


#  animals.insert(duck_index,"cobra")  alterntive 
"""
to add any thing in to a list you can use   .insert(index, item)   where the index is where
you want to put it ***but it will only put the item before whatever indexyou type if
you put it in index 2 it will be between 1 and 2 it wll not relace tht index***
item is the item that you wan to put in
"""
animals.insert(2, "cobra")

print (animals) 


my_list = [1,9,3,8,5,7]

for number in my_list:
  print (2 * number)




animals = ["cat", "ant", "bat"]

# sort()  sorts things in alphabetical order. 
animals.sort()

for animal in animals:
  print (animal)





start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print (square_list)


  




residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin'])

print (residents['Sloth'])
print (residents['Burmese Python'])


"""
This is a dictionary called d with three key-value pairs.
The key 'key1' points to the value 1, 'key2' to 2, and so on.
"""





menu = {} 
menu['Chicken Alfredo'] = 14.50 
print (menu['Chicken Alfredo'])


menu['somosa'] = 14.60
menu['kababs'] = 14.70
menu['katlama'] = 14.80



print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)

"""
 Items can be removed from a dictionary with the del command:

del dict_name[key_name]
"""

"""
A new value can be associated with a key by assigning a value to the key, like so:

dict_name[key] = new_value
"""








# key - animal_name : value - location 
zoo_animals = {
  'Unicorn' : 'Cotton Candy House',
  'Sloth' : 'Rainforest Exhibit',
  'Bengal Tiger' : 'Jungle House',
  'Atlantic Puffin' : 'Arctic Exhibit',
  'Rockhopper Penguin' : 'Arctic Exhibit'
}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']


zoo_animals['Rockhopper Penguin'] = 'horse'


print (zoo_animals)




"""
to remove anything from a list you can use .remove() for example


beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles

which will print out

 ["john","paul","george","ringo"]
"""




backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')





inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50


print (inventory)

















