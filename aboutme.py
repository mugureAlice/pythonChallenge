# First Name
#Last Name
#age
#height
#weight
#university
#course


#use a global variable to change the course

first_name ="Alice"
last_name = "Mugure"
age = 20
height = 56
weight = 80
university = "Kipchelele"
course = "cybersecurity"

def myfunc():
    global course
    course = "Information technology"
    
myfunc()
print("FIRSTNAME : ", first_name)   
print("LASTNAME : ", last_name)  
print("AGE : ", age) 
print("HEIGHT : ", height) 
print("WEIGHT : ", weight) 
print("UNIVERSITY : ", university) 
print("COURSE : ", course) 



