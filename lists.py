x = [0,1,1,2,3,5,8,13]
xpt2 = [0,1,1,2,3,5,8,13,21]
y = []
ypt2 = []
a = 0
b = 0
while a <len(x):
    b = b + x[a]
    a = a + 1
average = b/len(x)
print(average)
a = 0
while a <len(x):
    c = abs(x[a]-average)
    y.append(c)
    a = a + 1
print(y)
a = 0
b = 0
while a <len(y):
    b = b + y[a]
    a = a + 1
average2 = b/len(y)
print(average2)
d = 0
e = 0
while d <len(xpt2):
    e = e + xpt2[d]
    d = d + 1
average3 = e/len(xpt2)
print(average3)
d = 0
while d <len(xpt2):
    f = abs(xpt2[d]-average3)
    ypt2.append(f)
    d = d + 1
print(xpt2, ypt2)
d = 0
e = 0
while d <len(ypt2):
    e = e + ypt2[d]
    d = d + 1
average4 = e/len(ypt2)
print(average4)
woo = (average3/average) * 100
weee = (average4/average2) * 100
print("The two averages changed:" , woo, weee)