#Write a program that stores 3 sides of a cuboid as variables (doubles)
#The program should write the surface area and volume of the cuboid.

#Set the 3 sides to 10.4, 13.5, 8.2 and your program should produce the following output:
#Surface Area: 672.76
#Volume: 1151.28

l=float(10.4)
w=float(13.5)
h=float(8.2)

a=w*h*l
v=2*(w*l+h*l+h*w)

print(f"a test felszine: {a} es terfogata: {v}")


#Print the Body mass index (BMI) based on these values. Example:
#mass_in_kg = 81.2
#height_in_m = 1.78

import math

suly=float(245)
magassag=float(1.75)

bmi=suly/math.pow(magassag,2)
testtomegindex=round(bmi,2)

print(f"bmi: {testtomegindex}")


#Write a program that checks if a given year is a leap year or not.
#Leap years: 2000, 2004, 1904, 2024, 1600
#Not leap years: 1900, 1929, 1933, 2023, 1867

##nem jo
ev=int(input("irjon be egy evszamot a szokoev ellenorzesere: "))

if(ev%4==0) and (ev%100==0) or (ev%400==0):
    print(f"az ev szokoev.")

else:
    print(f"az ev nem szokoev.")