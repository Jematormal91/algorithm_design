## --> PROBLEMA #1 <--
# 1. Calcular el salario neto de un trabajador. 
# Es necesario conocer horas trabajadas, 
# pago por hora al trabajador y descuentos fijos al trabajo bruto con impuesto (12% del salario bruto). 
# 120 Horas trabajadas a razón de 13.45 por hora.

horas_trabajadas = int(input("Cuantas horas trabajaste: "))
pago_por_hora = float(input("Cuanto es tu pago por hora: "))
salario = pago_por_hora * horas_trabajadas
descuento_fijo = 0.12 * salario
salario_neto = salario - descuento_fijo
print("Tu salario neto es", salario_neto)

## --> PROBLEMA #2 <--
# 2. Suma de todos los números pares. La suma se realizará usando todos los números entre el 2 y el 100.
suma = 0
for i in range(0,102,2):
    suma += i
print("La suma de todos los numeros pares entre 2 y 100 es:", suma)

## --> PROBLEMA #3 <--
# 3. Desplegar (imprimir) la lista de números del 1 al 100 cuyo valor termine 6. 
value = "6"
for i in range(1,101):
    if (str(i).endswith("6")):
        print(i)
    
## --> PROBLEMA #4 <--
# 4. Calcular la suma de los números del 1 al 1000.

suma = 0
for i in range(1,1001):
    suma += i
print("La suma de todos los numeros de 1 al 1000 es:", suma)

## --> PROBLEMA #5 <--
# Calcular la media de las estaturas de las siguientes personas:
# 1     66 
# 2     69 
# 3     71 
# 4     70 
# 5     75 
# 6     67 
# 7     69 
# 8     64 
# 9     73 
# 10    71
# Mencione cuantas de esas personas son más altas que la media de la estatura y cuantas son más bajas.
personas = 1
suma = 0
personasMayorQueMedia = 0
personasMenorQueMedia = 0
estaturas = []

while (personas <= 10):
    estatura = int(input("Entra la estatura en pulgadas: "))
    estaturas.append(estatura)
    suma += estatura
    personas += 1

print("La suma de las estaturas es", suma)
media = suma/10
print("La media de las estaturas de las personas es: %.2f" % (media))
for i in range(0,len(estaturas)):
    if estaturas[i] > media:
        personasMayorQueMedia += 1
    elif estaturas[i] < media:
        personasMenorQueMedia += 1
print("Hay",personasMayorQueMedia,"personas mas altas que la media.\n"+"Hay",personasMenorQueMedia,"personas mas bajas que la media.")
