a = 0
b = 1
c = a + b
fib = 2
empty = 0
while fib < 1337:
    a = b
    b = c
    c = a + b
    fib = fib + 1
emp = c
print(c)
print(c//10)
print(c%10)
while empty == 0:
    if emp//10 == 0:
        empty = empty + 1
    elif emp%10 == 0:
        empty = empty + 1
        print("empty")
    else:
        emp = emp//10
    
