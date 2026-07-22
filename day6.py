#Decision making

#comparison operators
# == Equal to
# != Not equal to
# > Greater than
# < Less than
# >= Greater then or equal to
# <= Less than or equal to

#if statements
# if condition:


age = 10
if age >= 18:
    print("You can vote")

#if...else statement
else:
    print("You cannot vote")  

#if...elif...else statement

score = 76

if score >= 90:
    print("A")

elif score >= 80:
    print("B")    

elif score >= 70:

    print("C")

else:
    print ("Fail")   

#LOGICAL OPERATORS
# and
# or
# not    

age = 15
is_available = False

if age >= 18 and is_available:
    print("You can vote")

else:
    print("You cannot vote")    

if age >= 18 or is_available:
    print("You are sexzy")

else:
    print("You is baby")       

if not is_available:
    print("Boy bye!")    

else:
    print("Hell yeah!")    

#ATM
# A person inputs their name
# input password
# inputs their balance    

#use if..elif..else to check if the inputed info is correct