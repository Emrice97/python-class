a = 2
b = -12
c = 18
y=(-b+((b**2)-4*a*c)**0.5)/(2*a)
z=(-b-((b**2)-4*a*c)**0.5)/(2*a)
D= (b**2)-4*a*c
if D > 0:
    print("2 real solutions")
    print (y, z)
elif D==0:
    print ("1 real solution")
    print (y, z)
else :
    print ("2 imaginary solutions")
    print (y, z)