my_list = [i ** 2 for i in range(1, 11)] # list comprehension
# Generates a list of squares of the numbers 1 - 10
#   \/open text file\/¦ \/ write
f = open("output.txt", "w")# we store this operation in f
#    /\open is bultin function that opens file 

#                                           name of file
# f = open("output.txt","w")                       \/     \/---------type of file
#             /\-------------------------------- "output.txt"

for item in my_list:
  f.write(str(item) + "\n")

f.close()
"""
wrote all the contents of my_list to a text file called output.txt.
"""

#> f = open("output.txt", "w")

"""
This told Python to open output.txt in "w" mode ("w" stands for "write").
We stored the result of this operation in a file object, f.

Doing this opens the file
in write-mode and prepares Python to send data into the file.
"""
my_list = [i ** 2 for i in range(1, 11)] 
my_file = open("output.txt", "r+")
#                             /\ your second argument can be differiient 4 important
"""
write-only mode ("w")

read-only mode ("r")

read and write mode ("r+")

append mode ("a"), which adds any new data you write to the file
to the end of the file
"""
for items in my_list:
    my_file.write(str(items) + "\n")
#           /\ The .write() method takes a string argument, 
my_file.close()#<<< you must close the file with .close()

################
my_file = open("output.txt", "r")
#               \/ .read() is slightily simelier as .write() we ony read what is in the file  
print (my_file.read())
my_file.close()
###############

my_file = open("text.txt", "r+")
my_file.write("I'm the first line of the file! \n I'm the second line. \n Third line here, boss.")


print (my_file.readline())

print (my_file.readline())

print (my_file.readline())

"""
If you open a file and call
.readline() on the file object,
you'll get the first line of the file;
subsequent calls to .readline()
will return successive lines.
"""

my_file.close()
#############################################
with open("text.txt", "w") as textfile:
  textfile.write("Success!")

# special pair of built-in methods: __enter__() and __exit__()
# when a file object's __exit__() method is invoked,
#it automatically closes the file.

# to invoke this method? we use the (with) and (as) .

###############################

with open("text.txt", "a") as textfile:
    textfile.write("= faliulare")
############

"""
f = open("bg.txt")
####
f.closed
# False
~~~~~
f.close()
f.closed
# True

Python file objects have a closed attribute
which is True when the file is closed and False otherwise.

By checking file_object.closed,
we'll know whether our file is closed and can call close()
on it if it's still open.
"""

with open("text.txt", "w") as my_file:
  my_file.write("My Data!")
  
if not my_file.closed:
  my_file.close()
#               \/ .closed can check whther the file is closed true if closed false if still open
print (my_file.closed)
