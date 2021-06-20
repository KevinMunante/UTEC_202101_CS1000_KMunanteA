#Ej 1
a = int(input())
b = int(input())

x = ((a != b) or (a >= b)) and (a%b == 1)
x = x*1
print(x)

#Ej 2
a = int(input())
b = int(input())

x = not(a == b or a <= b) and ((a % b)!=2)
x = x * 1
print(x)

#Ej 3
a = int(input())
b = int(input())

x = (a != b**2) and (b/a == 1)
x = x * 1
print(x)

#Ej 4
4. a = float(input())
b = int(input())
a = round(a,0)
x = (b==a) or ((a*b)>10)
x = x * 1
print(x)

#Ej 5
import math

a = int(input())
b = int(input())

x = not(math.sqrt(a2 + b2) == (2a - b))
x = x1
print(x)

#Ej 6

a = float(input())
b = float(input())

astr = str(a)[:5]
afloat = float(astr)

x = afloat == b
x = x1
print(x)

#Ej 7
a = int(input())
b = int(input())

bin_a = bin(a)
bin_b = bin(b)

a = (bin_a[3:6])
b = (bin_b[3:6])

x = a == b
x = x1
print(x)

#Ej 8
a = input()
b = input()

x = ((a!=b) and (len(a) == len(b)))

x = x * 1
print(x)

#Ej 9
a = float(input())
b = float(input())

a = round(a,2)
b = round(b,2)

x = (a == b)
x = x * 1
print(x)

#Ej 10
a = input()
b = input()
c = input()

x = ((a > b or ((b > c) and (a > c))))
x = x * 1
print(x)

#Ej 11
a = int(input())

x = bin(a)

x = x[2:]

print(x)

#FIN