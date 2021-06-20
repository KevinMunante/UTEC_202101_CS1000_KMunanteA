#Semana 6
def f(x):
  return x**2

f(3)
9

#Pandas
url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/tips.csv'
print(url)
import pandas as pd

# Lectura del dataset
datos = pd.read_csv( url )
print(datos)

datos['size']
datos['sex']

#Mostrar las columnas: total_bill, tip, smoker, time

columnas = ['total_bill', 'tip', 'smoker', 'time']
datos[columnas]

datos[['total_bill', 'tip', 'smoker', 'time']]

datos2 = datos[['total_bill', 'tip', 'smoker', 'time']]
print(datos2)

#Mostrar las 7 columnas y solo los 5 primeros registros

datos.head(5)

#Mostrar las 7 columnas y los últimos 5 registros

datos.tail(5)

n_registros = int(input("Ingrese el número de registros a mostrar: "))
datos3 = datos.head(n_registros)
print(datos3)

#Mostrar las colunas: tip, sex y size con solo los 10 primeros registros

datos4 = datos[['tip', 'sex', 'size']]
print(datos4.head(10))

datos[["tip","sex","size"]].head(10)

#Valores booleanos
print(datos)

datos['size'] == 3

booleanos = (datos['size']==3)
print(booleanos)

#Mostrar todos los registros donde time='Dinner'

booleanos = (datos['time']=='Dinner')
datos[booleanos]

#Mostrar todos los registros donde sex='Female'

female = datos['sex'] == 'Female'
datos[female]

#Mostrar los primeros 8 registros donde sex='Female'

datos[datos['sex'] == 'Female'].head(8)

#Mostrar todos los registros donde sex='Female' y 'day'='Sun'

booleanos = (datos['sex']=='Female') & (datos['day']=='Sun')
print(datos[booleanos])

bool1 = datos['sex'] == 'Female'
bool2 = datos['day'] == 'Sun'
datos[bool1 & bool2]

#Mostrar los primeros 8 registros donde sex='Male', day= Fri o Thur, smoker='Yes'

booleanos = datos['smoker']=='Yes'
booleanos

booleanos.value_counts()

lista = booleanos.value_counts()
print(lista)

lista[0]

lista[1]

print("En la data, hay {} personas fumadoras".format(lista[1]))

print("En la data, hay {} personas fumadoras".format(booleanos.value_counts()[1]))

print("En la data, hay {} personas fumadoras".format((datos['smoker']=='Yes').value_counts()[1]))

#Mostrar la cantidad de registros donde las personas son fumadoras y han ido el día domingo

condicion = (datos['smoker'] == 'Yes') & (datos['day'] == 'Sun')
condicion.value_counts()[1]

#Mostrar los primeros 10 registros donde sea cena (dinner) y la propina (tip) sea mayor que 5.00

booleanos = (datos["time"] == "Dinner") & (datos["tip"] > 5)
print(datos[booleanos].head(10))

condicion = (datos['time'] == 'Dinner') & (datos['tip'] > 5)
datos[condicion].head(10)

C1 = datos['time'] == 'Dinner'
C2 = datos['tip'] > 5
print(datos[C1 & C2].head(10))

#Mostrar la cantidad de registros donde size sea mayor que 5 y la factura total sea mayor que 45

condicion = (datos['size'] > 5) & (datos['total_bill'] > 45)
condicion.value_counts()[1]

booleanos = (datos["size"] > 5) & (datos["total_bill"] > 45)
print(booleanos.value_counts()[1])

((datos["total_bill"] > 45) & (datos["size"] > 5)).value_counts()[1]

condición = (datos['size']>5) & (datos['total_bill'] >45)
condición.value_counts()[1]

C1 = datos['size'] > 5
C2 = datos['total_bill'] > 45
print((C1 & C2).value_counts()[1])

#Agrupar los datos por 'sex'

datos.groupby('sex').size()

print("Female: {} registros".format(datos.groupby('sex').size()[0]))
print("Male: {} registros".format(datos.groupby('sex').size()[1]))

#Agrupar por día

datos.groupby('day').size()

datos.groupby('day').count()