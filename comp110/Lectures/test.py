# import matplotlib.pyplot as pp
# import math

# def pearson_r(x_vals, y_vals):
#   x_mean = mean(x_vals)
#   y_mean = mean(y_vals)
#   numerator = 0
#   x_diffs = 0
#   y_diffs = 0
#   for i in range(len(x_vals)):
#     xd=x_vals[i] - x_mean
#     yd=y_vals[i] - y_mean
#     numerator += xd*yd
#     x_diffs += xd**2 
#     y_diffs += yd**2
  
#   denom = math.sqrt(x_diffs) * math.sqrt(y_diffs)
#   return numerator/denom


# def mean(x_vals):
#   total = 0
#   for i in range(len(x_vals)):
#     total = total + x_vals[i]
#   return total / len(x_vals)

# x_vals = [1,2,3,4,5,6]
# y_vals = [-2,-3,8,0,-5,-6]
# pp.scatter(x_vals,y_vals)
# #pp.show()
# r = pearson_r(x_vals, y_vals)
# print(mean(y_vals))
# print(r)

my_dict = { "foo" : 10, "bar": 33 }
my_dict["baz"] = 18
print(my_dict)
print("foo" in my_dict, "woof" in my_dict)
my_dict[33] = 18
print(my_dict)
print(33 in my_dict)
if("woof" in my_dict):
  print(my_dict['woof'])
else:
  my_dict['woof'] = 12
print(my_dict)

