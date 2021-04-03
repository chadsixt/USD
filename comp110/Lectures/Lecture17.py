# # animals = open('animals.txt', 'w')
# # animals.
# # done = False
# # while not done:
# #   a = input("Enter an animal or STOP to finish:")
# #   if a == "STOP":
# #     done = True
# #   else:
# #     animals.write(a + '\n')

# # Append-adds at last
# file1 = open("animals.txt", "a")  # append mode
# file1.write("Today \n")
# file1.close()

# file1 = open("animals.txt", "r")
# print("Output of Readlines after appending")
# print(file1.read())
# print()
# file1.close()

# def foo(in_name, out_name, n) :
#   print(type(in_name))
#   in_file = open(in_name, 'r')
#   out_file = open(out_name, 'w')
#   i = 0
#   count = 0
#   line = in_file.readline()
#   print(type(in_file))
#   while ((i < n) and (line != "")):
#     count +=1
#     if int(line) < 0:
#       out_file.write(line)
#       i += 1
#     line = in_file.readline()
#   print(count)  
#   in_file.close()
#   out_file.close()
    
# foo("nums.txt", "nums2.txt", 2)

def is_prime(n):
  if n < 2:
    return False
  i = 2
  while i < n:
    if n % i == 0:
      return False
    i += 1
  return True

def is_prime(n):
  if n < 2:
      return False
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

def NumberOfPrimes(n):
  i = 2
  numOfPrimes = 0
  total = 0
  while total < n:
    if is_prime(i):
      total += i
      print(i)
      numOfPrimes += 1
    i += 1
  return numOfPrimes

    
print(NumberOfPrimes(100))
# def bar(n):
#   i = 2
#   j = 0
#   sumOfPrimes = 0
#   totalPrimes = 0
#   while sumOfPrimes < n:
#     if is_prime(i):
#       sumOfPrimes += i
#       totalPrimes += 1
#     i += 1
#   return j
  



