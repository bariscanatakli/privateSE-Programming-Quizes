

a = 1
b = 45

def f (x):
    if x == b:
        
        return x
    else:
        print(x)
        return f(x+a)

print(f(a))