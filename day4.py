#last in first out

#Global variable
x ="NAIROBI"

def myfunc():
    global x 
    x ="MOMBASA"

    print ("I live in", x)

myfunc()
print("I live in ", x)    