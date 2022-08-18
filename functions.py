def FUNction(a,b,c,x):
    y = ((a*(x**2)) + (b*x) + c)
    yay=(-b+((b**2)-4*a*c)**0.5)/(2*a)
    nay=(-b-((b**2)-4*a*c)**0.5)/(2*a)
    print(y)
    print("(", yay , "," , nay , ")")
FUNction(5,8,-20,7)    

def Whee(a):
    x=-1
    rev = a[x]
    while x != -len(a):
        print(x)
        x = x-1
        rev = rev + a[x]
    return rev
print(Whee("rip me"))