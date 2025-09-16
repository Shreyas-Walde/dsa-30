def our_print(s): # parameter -> temp stored value
    print(s)      # passing parameter
    print(s+"hola")

our_print("nihao ") # function calling with (argument)

  
def our_print(s): 
    print(s)      
    print(s+"hola")
#   return None     -> py has in func by default
our_print("2 ")

print("*******************")

def times_2(x):
    return x*2

number = times_2(5)
print(number)

print(None)

print("*******************")

def add(a,b):
    return a+b

print(add(3,9))

def add(a,b,c=4):  # seting a default value c=4
    return a+b+c  # no error

funcadd = add(1,4)
print(funcadd)

