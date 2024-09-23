def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def add_then_multiply(x,y,z):
    return multiply(add(x,y),z)

print("result = ",add_then_multiply(2,4,3))
