import math

"""calculate area of a triangle"""
a=3
b=5
c=7
#calculate S
S=(a+b+c)/2
#calculate area using Heron's formula
area=math.sqrt(S*(S-a)*(S-b)*(S-c))
print(area)
