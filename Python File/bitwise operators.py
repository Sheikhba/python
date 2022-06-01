#Bitwise operations are operations that directly manipulate bits. In all computers, numbers are represented with bits, a series of zeros and ones.
# basic bit wise operation

print (5 >> 4)  # Right Shift
print (5 << 1)  # Left Shift
print (8 & 5)   # Bitwise AND
print (9 | 4)   # Bitwise OR
print (12 ^ 42) # Bitwise XOR
print (~88)     # Bitwise NOT

# In Python, you can write numbers in binary format by starting the number with 0b.
# When doing so, the numbers can be operated on like any other number!

print (0b1,)    #1
print (0b10,)   #2
print (0b11,)   #3
print (0b100,)  #4
print (0b101,)  #5
print (0b110,)  #6
print (0b111)   #7
print ("******")
print (0b1 + 0b11)
print (0b11 * 0b11)
 # to write number in its binary fr you need to type 0b first then the binary number associated withit
#     ___________________________________
#     128 | 64 | 32 | 16 | 8 | 4 | 2 | 1
#     ------------------------------------
#no 1/ 0     0    0    0    0   0   0   1

print (bin(1)) # bin() takes a interger input and give the binary reresentation of that number
print (bin(2))
print (bin(3))
print (bin(4))
print (bin(5))
#Keep in mind that after using the bin function,
# you can no longer operate on the value like a number

#int() <<< a pre defined function in python has more useability 
print (int("110", 2))
 #          /\    /\
 #  the number |  the base that number is in

print (int("1",2))
print (int("10",2))
print (int("111",2))
print (int("0b100",2))
print (int(bin(5),2))
print (int("11001001", 2))

# Left Bit Shift (<<)  
# 0b000001 << 2 == 0b000100 (1 << 2 = 4)
# 0b000101 << 3 == 0b101000 (5 << 3 = 40)       

# Right Bit Shift (>>)
# 0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
# 0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)

#Note that you can only do bitwise operations on an integer.
#Trying to do them on strings or floats will result in nonsensical output!

##########################################################################################################################
# AND (&) operator
# 
#                                   The bitwise AND (&) operator compares two numbers on a bit level
#                                   and returns a number where the bits of that number are turned on
#                                   if the corresponding bits of both numbers are 1.
#  0 & 0 = 0
#  0 & 1 = 0
#  1 & 0 = 0
#  1 & 1 = 1


#     a:   00101010   42
#     b:   00001111   15       
# ===================
# a & b:   00001010   10


a = (0b111) #<<(7)
b = (0b1010) #<<(10)
print(a & b) #<<(2)


print (bin(0b1110 & 0b101)) # here we compare the 2 binary numbers and give the answer in binary

##################################################################################################################################################################
#  OR (|) operator
#                                  The bitwise OR (|) operator compares two numbers on a bit level
#                                  and returns a number where the bits of that number are turned on
#                                  if either of the corresponding bits of either number are 1


#  0 | 0 = 0
#  0 | 1 = 1 
#  1 | 0 = 1
#  1 | 1 = 1




#     a:  00101010  42
#     b:  00001111  15       
# ================
# a | b:  00101111  47

c = (0b110) #(6) 
d = (0b1010)#(10)
print (c | d) #(14)

print (bin(0b1110 | 0b101))# here we compare the 2 binary numbers and give the answer in binary

######################################################################################################################################################################
# XOR (^) or exclusive or operator
#                                   The XOR (^) or exclusive or operator compares two numbers on a bit level
#                                   and returns a number where the bits of that number are turned on
#                                   if either of the corresponding bits of the two numbers are 1, but not both.
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0


#   a:  00101010   42
#   b:  00001111   15       
#================
# a ^ b:  00100101   37

e = (0b111)# (7) 
f = (0b1010)# (10)
print(e ^ f)#(13)

print (bin(0b1110 ^ 0b101))# here we compare the 2 binary numbers and give the answer in binary
##########################################################################################################################################################################
#NOT operator (~)
#              /\       NOT operator (~) just flips all of the bits in a single number.
#              /\        this is equivalent to adding one to the number and then making it negative.
        # adds one then makes it negative
print (~1)   # -2
print (~2)   # -3
print (~3)   # -4
print (~42)  # -43
print (~123) # -124
#################################################################################################################################################################################
def check_bit4(input):# here we defined a function called check_bit4 and gave it one argument called input
  mask = (0b1000) # here we set mask a verible to the binary nmber 8 which is 0b1000
  desired = (input & mask) # here we compare input and mask using the bit wise operator and the later seting it to desired
  if desired > 0: #here we use a if statement to check if disired has any digits that is larger than 0 
    return "on" # if so then return on
  else: # if not (else) return off
    return "off"
biton = (check_bit4(0b1000))
print (biton)
bitoff = (check_bit4(0b0000))
print(bitoff)
###############################################################################################################################################################
a = (0b10111011) # a is set to binary number of 187

mask = (0b100)# mask is set to binary number 4 
desired = (a | mask) # here we used a or bit wise operator to compare a and maskand then set it to desired  
print (bin(desired))# here we printed desired the binary version 
###############################################################################################################################################################
a = (0b11101110) # a is set to the binary version of 238

mask = (0b11111111)#mask is set to the binary version of 255
desired = (a ^ mask) # here we used the xor bit wise operator to compare a and mask and set it to desired 
print (bin(desired)) # here we print desired in its binary form
#################################################################################################################################################
def flip_bit(number, n):# here we define a function called flip_bit that takees 2 argument called mnumber and n
  bit_to_flip = (0b101 << (n -1)) # here we use the verible bit_to_flip and set it to the binary number that we want to shift to the left to argument of n -the move of shift
  result = (number ^ bit_to_flip) # we compare the argument number ad bit_to_flip using the xor bit wise operator and set it to result
  return bin(result) # here we return result as binary version  
print (flip_bit(0b0,0b01))
#######################################################################################################################################################################################
