#1
# ClassName = "COMP-110-FA20-S02"
# print(ClassName[:3] )
# print(ClassName[2:9])
# print(ClassName[-5:])

# 2
# def file_mystery(filename):
#     f = open(filename, 'r')
#     biggest = 0
#     for line in f:
#         vals = line.split(',')
#         diff = int(vals[1]) - int(vals[0])
#         if diff > biggest:
#            biggest = diff
#     return biggest
# print(file_mystery('data.csv'))

#3
# def print_bigrams(my_str):
#     for i in range(0, len(my_str), 2):     
#         print(my_str[i] + my_str[i+1])
# print(print_bigrams('odd'))
#print(print_bigrams('even'))

#4
# import turtle 
# wn = turtle.Screen() 
# def draw_L_at(my_turtle, x, y): 
#     my_turtle = turtle.Turtle() 
#     my_turtle.penup() 
#     my_turtle.goto(x, y) 
#     my_turtle.forward(20)
#     my_turtle.pendown() 
#     my_turtle.left(180) 
#     my_turtle.forward(20) 
#     my_turtle.right(90) 
#     my_turtle.forward(40) 
    
#     wn.exitonclick()
# t = turtle.Turtle()    
# draw_L_at(t, 100, 200)

# 5

# meow = open("bar.txt", "r")
# meow.readline()
# for line in meow:
#     fields = line.split(",")
#     if len(fields) > 2:
#         print(fields[2])
#     elif int(float(fields[0])) > int(float(fields[1])):
#         print(fields[0])
#     else:
#         print(fields[1])

# #6
# def lol(x):
#     return x % 3

# def omg(y):
#     m = y * 2
#     n = ttyl(m)
#     return n

# def ttyl(y):
#     r = y + 1
#     # indicated line
#     # in scope
#     print('y -> ', y)
#     print('r -> ', r)
#     print('a -> ', a)
#     #Not in scope x, m, b
#     #print(x)
#     #print(m)
#     #print(b)
#     return r

# a = lol(8)
# b = omg(a + 1)
# print(b)

# 7
def   centripetal_force ( mass ,  velocity ,  radius ):
    fc  =  (mass * velocity ** 2 ) / radius
    return  fc

force = centripetal_force(30.5, 12.7, 44.21)
print(force)