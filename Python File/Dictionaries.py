## Dictioaries in Python is like a look up table
#################################################
# To make a Dictionaries in python you need to use the currly bracket {}

d = {} # This is an empty dictionary that has no value or keys assoiated with the verible d
d = dict() # This is the the same as the code above but it has normal bracets and the in built code (( dict )) is shorten version of dictionaries      
# We will be using the first code the more simpler version
###
d = {"George": 24, "Tom": 32} # This is a dictionary with keys and value that are assosiated with those keys but must be in that format keys can be any thing and values can be any thing
#^        ^     ^      ^    ^
#verible  key   value  key  value
###
# To an empty dictonary like (( d = {} )) you can add keys and values using this method that I will be going through 
###
d = {} # This is our empty dictionary which we are oinng to put a key and a vale along side the key
d["Geoorge"] = 24 # Here we are getting the empty dictionary which is (( d )) and adding a new key called "George" and which has the value 24 you must use the squre bracket when assigning the key then equals then the value with out any bracket  
#^        ^     ^
#verible  key   value
###
# We can add more keys and values in the same method
d["Tom"] = 32
d["Jenny"] = 16
###
print (d) # this will obviosly print out everything in the dictionary d
###
# if you wanted to see what is in a certain key you can use this kind of code
print(d["Geoorge"]) # to see the value thats in a key you must use this structure and the in that format obviosly tour verible and will be different  
#^     ^        ^
#print verible  key
###
#keys can only be certain type commonly string or number
#Values can be any type
#You can mix different type of keys E.G
# d[10] = 100 #10 is the key 100 is the value
###
#how to iterate over key-value pairs

for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print("")

