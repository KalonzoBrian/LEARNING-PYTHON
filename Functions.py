from math import pi
def circumference(r):
    return 2 *pi * r

def area(r):
    return pi * r**2

def volume(r):
    return (4/3) * pi * r**3

r = float(input("Enter the radius: "))
print(f"Circumference: {circumference(r)}")
print(f"Area: {area(r)}")
print(f"Volume: {volume(r)}")