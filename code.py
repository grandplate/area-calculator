"""This is an Area Calculator. It prompts the user to select a shape then calculates 
the area of that shape. It then prints the area of that shape to the user."""

from math import pi

print "Area Calculator"


option = raw_input("Enter C for Circle, S for square or T for Triangle: ")
option = option.upper()

if option == "C":
    radius = float(raw_input("Enter radius: "))
    area = pi * radius ** 2
    print ("Area: %.2f." % (area))
  
elif option == "T":
    base = float(raw_input("Enter base: "))
    height = float(raw_input("Enter height: "))
    area = 0.5 * base * height
    print ("Area: %.2f." % (area))
    
elif option == "S":
    length = float(raw_input("Enter length of side: "))
    area = length ** 2
    print ("Area : %.2f." % (area))
  
else:
    print "Error! Invalid shape selector specified."
