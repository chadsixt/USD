# fileObject = open('Quiz4.txt','r')
# fileObject.readline()
# names = []
# names_str = ''
# for line in fileObject:
#     items = line.split(',')
#     names_str = names_str + items[1]
#     names.append(items[1])

# print(names_str)

# print(names)
# names.sort()
# print(names)
animals = open('animals.txt', 'w')
animals.
done = False
while not done:
  a = input("Enter an animal or STOP to finish:")
  if a == "STOP":
    done = True
  else:
    animals.write(a + '\n')


