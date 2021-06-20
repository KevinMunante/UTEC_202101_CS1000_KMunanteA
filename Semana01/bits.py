#Ej 1 y 2

base = 8
num = int(input("Elige el numer que quieres convertir [13 / 18]: "))

#Primera Division
residuo = num % base
cociente = num // base
n1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
n2 = residuo

print("{} = {}{}".format(num, n2, n1))

#Ej 3

base = 16
num = 48

# Primera Division
residuo = num % base
cociente = num // base
n1 = residuo

# Segunda Division
residuo = cociente % base
cociente = cociente // base
n2 = residuo

if n1 == 10:
    n1 = "a"

elif n1 == 11:
    n1 = "b"

elif n1 == 12:
    n1 = "c"

elif n1 == 13:
    n1 = "d"

elif n1 == 14:
    n1 = "e"

elif n1 == 15:
    n1 = "f"

if n2 == 10:
    n2 = "a"

elif n2 == 11:
    n2 = "b"

elif n2 == 12:
    n2 = "c"

elif n2 == 13:
    n2 = "d"

elif n2 == 14:
    n2 = "e"

elif n2 == 15:
    n2 = "f"

print("{} = {}{}".format(num, n2, n1))

#Ej4

x = 99
hexadecimal = hex(x)

print(type(hexadecimal))

print()

##
hexadecimal = format(x , ¨0x¨)
print(type(hexadecimal))
print(hexadecimal)

#Ej5
base = 16
num = 67

#Primera Division
residuo = num % base
cociente = num // base
n1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
n2 = residuo


if n1 == 10:
  n1 = "a"

elif n1 == 11:
  n1 = "b"

elif n1 == 12:
  n1 = "c"

elif n1 == 13:
  n1 = "d"

elif n1 == 14:
  n1 = "e"

elif n1 == 15:
  n1 = "f"

if n2 == 10:
  n2 = "a"

elif n2 == 11:
  n2 = "b"

elif n2 == 12:
  n2 = "c"

elif n2 == 13:
  n2 = "d"

elif n2 == 14:
  n2 = "e"

elif n2 == 15:
  n2 = "f"

print("{} = {}{}".format(num, n2, n1))

#Ej6

base = 2
num = 104

#Primera Division
residuo = num % base
cociente = num // base
bit1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

# Terceras division
residuo = cociente % base
cociente = cociente // base
bit3 = residuo

#Cuarta Division
residuo = cociente % base
cociente = cociente // base
bit4 = residuo

#Quinta Division
residuo = cociente % base
cociente = cociente // base
bit5 = residuo

#Sexta Division
residuo = cociente % base
cociente = cociente // base
bit6 = residuo

#Septima Division
residuo = cociente % base
cociente = cociente // base
bit7 = residuo

print("{} = {}{}{}{}{}{}{}".format(num, bit7, bit6, bit5, bit4, bit3, bit2, bit1))

#Ej7

base = 2
num = 254

#Primera Division
residuo = num % base
cociente = num // base
bit1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

# Terceras division
residuo = cociente % base
cociente = cociente // base
bit3 = residuo

#Cuarta Division
residuo = cociente % base
cociente = cociente // base
bit4 = residuo

#Quinta Division
residuo = cociente % base
cociente = cociente // base
bit5 = residuo

#Sexta Division
residuo = cociente % base
cociente = cociente // base
bit6 = residuo

#Septima Division
residuo = cociente % base
cociente = cociente // base
bit7 = residuo

#Octava  Division
residuo = cociente % base
cociente = cociente // base
bit8 = residuo

print("{} = {}{}{}{}{}{}{}{}".format(num,bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1))

#Ej8
base = 16
num = 305

#Primera Division
residuo = num % base
cociente = num // base
n1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
n2 = residuo

#Tercera Division
residuo = cociente % base
cociente = cociente // base
n3 = residuo

if n1 == 10:
  n1 = "a"

elif n1 == 11:
  n1 = "b"

elif n1 == 12:
  n1 = "c"

elif n1 == 13:
  n1 = "d"

elif n1 == 14:
  n1 = "e"

elif n1 == 15:
  n1 = "f"

if n2 == 10:
  n2 = "a"

elif n2 == 11:
  n2 = "b"

elif n2 == 12:
  n2 = "c"

elif n2 == 13:
  n2 = "d"

elif n2 == 14:
  n2 = "e"

elif n2 == 15:
  n2 = "f"

if n3 == 10:
  n3 = "a"

elif n3 == 11:
  n3 = "b"

elif n3 == 12:
  n3 = "c"

elif n3 == 13:
  n3 = "d"

elif n3 == 14:
  n3 = "e"

elif n3 == 15:
  n3 = "f"

print("{} = {}{}{}".format(num, n3, n2, n1))

#Ej9
base = 8
num = 587

#Primera ZeroDivisionE
residuo = num % base
cociente = num // base
n1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
n2 = residuo

# Terceras division
residuo = cociente % base
cociente = cociente // base
n3 = residuo

#Cuarta Divisin
residuo = cociente % base
cociente = cociente // base
n4 = residuo

print("{} = {}{}{}{}".format(num, n4, n3, n2, n1))

#Ej10

base = 2
num = 788

#Primera division
residuo = num % base
cociente = num // base
bit1 = residuo

#Segunda division
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

#Tercera division
residuo = cociente % base
cociente = cociente // base
bit3 = residuo

#Cuarta division
residuo = cociente % base
cociente = cociente // base
bit4 = residuo

#Quinta division
residuo = cociente % base
cociente = cociente // base
bit5 = residuo

#Sexta division
residuo = cociente % base
cociente = cociente // base
bit6 = residuo

#Septima division
residuo = cociente % base
cociente = cociente // base
bit7 = residuo

#Octava division
residuo = cociente % base
cociente = cociente // base
bit8 = residuo

#Novena division
residuo = cociente % base
cociente = cociente // base
bit9 = residuo

#Decima division
residuo = cociente % base
cociente = cociente // base
bit10 = residuo

print("{} = {}{}{}{}{}{}{}{}{}{}".format(num, bit10, bit9, bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1))

#Ej11

base = 2
num = 1023

#Primera division
residuo = num % base
cociente = num // base
bit1 = residuo

#Segunda division
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

#Tercera division
residuo = cociente % base
cociente = cociente // base
bit3 = residuo

#Cuarta division
residuo = cociente % base
cociente = cociente // base
bit4 = residuo

#Quinta division
residuo = cociente % base
cociente = cociente // base
bit5 = residuo

#Sexta division
residuo = cociente % base
cociente = cociente // base
bit6 = residuo

#Septima division
residuo = cociente % base
cociente = cociente // base
bit7 = residuo

#Octava division
residuo = cociente % base
cociente = cociente // base
bit8 = residuo

#Novena division
residuo = cociente % base
cociente = cociente // base
bit9 = residuo

#Decima division
residuo = cociente % base
cociente = cociente // base
bit10 = residuo

print("{} = {}{}{}{}{}{}{}{}{}{}".format(num, bit10, bit9, bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1))

#Ej12
base=16
num=1054

#Primera Division
residuo = num  % base
cociente = num // base
n1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
n2 = residuo

#Tercera Division
residuo = cociente % base
cociente = cociente // base
n3 = residuo

if n1 == 10:
  n1 = "a"

elif n1 == 11:
  n1 = "b"

elif n1 == 12:
  n1 = "c"

elif n1 == 13:
  n1 = "d"

elif n1 == 14:
  n1 = "e"

elif n1 == 15:
  n1 = "f"

if n2 == 10:
  n2 = "a"

elif n2 == 11:
  n2 = "b"

elif n2 == 12:
  n2 = "c"

elif n2 == 13:
  n2 = "d"

elif n2 == 14:
  n2 = "e"

elif n2 == 15:
  n2 = "f"

if n3 == 10:
  n3 = "a"

elif n3 == 11:
  n3 = "b"

elif n3 == 12:
  n3 = "c"

elif n3 == 13:
  n3 = "d"

elif n3 == 14:
  n3 = "e"

elif n3 == 15:
  n3 = "f"

print("{} = {}{}{}".format(num,n3, n2, n1))

#Ej13
base = 8
num = 3054

#Primera Division
residuo = num % base
cociente = num // base
n1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
n2 = residuo

#Tercera Division
residuo = cociente % base
cociente = cociente // base
n3 = residuo

#Cuarta Division
residuo = cociente % base
cociente = cociente // base
n4 = residuo

print("{} = {}{}{}{}".format(num, n4, n3, n2, n1))

#Ej14

base = 2
num = 5785

#Primera division
residuo = num % base
cociente = num // base
bit1 = residuo

#Segunda division
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

#Tercera division
residuo = cociente % base
cociente = cociente // base
bit3 = residuo

#Cuarta division
residuo = cociente % base
cociente = cociente // base
bit4 = residuo

#Quinta division
residuo = cociente % base
cociente = cociente // base
bit5 = residuo

#Sexta division
residuo = cociente % base
cociente = cociente // base
bit6 = residuo

#Septima division
residuo = cociente % base
cociente = cociente // base
bit7 = residuo

#Octava division
residuo = cociente % base
cociente = cociente // base
bit8 = residuo

#Novena division
residuo = cociente % base
cociente = cociente // base
bit9 = residuo

#Decima division
residuo = cociente % base
cociente = cociente // base
bit10 = residuo

#Undecima division
residuo = cociente % base
cociente = cociente // base
bit11 = residuo

#Duodecima division
residuo = cociente % base
cociente = cociente // base
bit12 = residuo

#Trigesima division
residuo = cociente % base
cociente = cociente // base
bit13 = residuo

print("{} = {}{}{}{}{}{}{}{}{}{}{}{}{}".format(num, bit13, bit12, bit11, bit10, bit9, bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1))

#Ej15
base=16
num=15850

#Primera Division
residuo = num % base
cociente = num // base
n1 = residuo

#Segunda Division
residuo = cociente % base
cociente = cociente // base
n2 = residuo

#Tercera Division
residuo = cociente % base
cociente = cociente // base
n3 = residuo

#Cuarta Division
residuo = cociente % base
cociente = cociente // base
n4 = residuo


if n1 == 10:
  n1 = "a"

elif n1 == 11:
  n1 = "b"

elif n1 == 12:
  n1 = "c"

elif n1 == 13:
  n1 = "d"

elif n1 == 14:
  n1 = "e"

elif n1 == 15:
  n1 = "f"

if n2 == 10:
  n2 = "a"

elif n2 == 11:
  n2 = "b"

elif n2 == 12:
  n2 = "c"

elif n2 == 13:
  n2 = "d"

elif n2 == 14:
  n2 = "e"

elif n2 == 15:
  n2 = "f"

if n3 == 10:
  n3 = "a"

elif n3 == 11:
  n3 = "b"

elif n3 == 12:
  n3 = "c"

elif n3 == 13:
  n3 = "d"

elif n3 == 14:
  n3 = "e"

elif n3 == 15:
  n3 = "f"

if n4 == 10:
  n4 = "a"

elif n4 == 11:
  n4 = "b"

elif n4 == 12:
  n4 = "c"

elif n4 == 13:
  n4 = "d"

elif n4 == 14:
  n4 = "e"

elif n4 == 15:
  n4 = "f"

print("{} = {}{}{}{}".format(num,n4, n3, n2, n1))

