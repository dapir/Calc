x = 0
y = 0

def fun(a, b):
    global x
    global y
    x = a
    y = b

def sum():
    return x + y

def diff():
    return x - y

def mult():
    return x * y

def div():
    return round(x / y)    
