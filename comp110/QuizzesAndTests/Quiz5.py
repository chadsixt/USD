# 1 
# The following sting has been encrypted “qi#uz3”. 
# Using the two-rail method, Write function that will accept a 
# string and return a decrypted string. (2 pts)
cipher= ('qi#uz3')
def rail_encrypt(cipher):
     top = ""
     bottom = ""
     for i in range(len(cipher)):
          if i % 2 == 0:  
               top = top + cipher[i]
          else:
               bottom = bottom + cipher[i]
     return top + bottom

print(rail_encrypt(cipher)) 

def rail_decrypt(cipher): 
    plain = "" 
    half = len(cipher) // 2 
    for i in range(0, half): 
        plain = plain + cipher[i] 
        plain = plain + cipher[i + half]  
   
    return plain 
print(rail_decrypt(cipher)) 
# 2
# Part 1:
# What is an alias in python? (1 pt)
#
## Answer: Multiple variables that reference the same object in memory
#
# Part 2:
# Write a function accepts a list of integers and multiplies all values in the list by 100 and returns the list to the caller. (1 pt)
def mult_hundred(int_list):
  for i in range(len(int_list)):
    int_list[i] = int_list[i] * 100
  return int_list

int_list = [1,2,3,4,5]
int1_list = int_list
print (int1_list is int_list)
print( mult_hundred(int_list) )

# 3
#Part 1:
#What is cloning in python? (1 pt)
#
#Answer: create multiple variables that reference the same values, basically a copy
#
#Part 2:
#Provide an example of how you would create a clone in python (1 pt)

#4
#What is a Tuple?
#
# Answer: a sequence of items that is is immutable 

#what is the ourtput of the following code#

def TestFunc(lot, target):
  total = 0
  found = 0
  names = []
  for item in lot:
    if item[1] > target:
        names.append(item[0])
        total = total + item[1]
        found = found + 1
  return (names, total/len(names))
ClassList = [('Bob', 100), ('Billy', 95), ('Sheryl', 85), ('Dug', 70)]
print(TestFunc (ClassList, 75))
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
cpy = list(nums)
print(nums is cpy)