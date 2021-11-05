import math

# This program is made to find the roots of a polynomial

#Let's start by giving a value for a , b , c
#The float () function converts the specified value into a floating point number and we're using input to give a value to our number

a = float(input("Enter the value of a :"))
b = float(input("Enter the value of b:"))
c = float(input("Enter the value of c:"))

#Now let's define a variable delta

delta = b ** 2 - 4 * a * c

if delta < 0 :
    print("There's no solutions on R")

elif delta==0 :
    x = (-b)/(2*a)
    print("La solution est : ", x)
else :
    x1= (-b-math.sqrt(delta))/(2*a)
    x2=(-b+math.sqrt(delta))/(2*a)

    print ("The solutions are :", format(x1, ".2f") , " et " , format(x2, ".2f"))

#Valentin THEOBALD 1G1

