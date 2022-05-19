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

## --> PROBLEMA #6 <--

# Realizar un programa en donde, cuando el usuario entre un numero entre 1 y 7 el programa
# arroje un mensaje que indique s que dia corresponde ese numero ingresado, ademas, 
# si el usuario entra un numero que no esta entre 1 y 7 el programa debe pedir que 
# se entre otro numero entre eses rango y al entrar el numero 9 el programa se cierre.

opcionusuario = 0

while (opcionusuario != 9):
    
    opcionusuario = int(input("Escribe un numero para saber a que dia de la semana corresponde (Si desea cerrar el programa persione 9): "))

    if opcionusuario == 1:
        print("Lunes\n")
    
    elif opcionusuario == 2:
        print("Martes\n")

    elif opcionusuario == 3:
        print("Miercoles\n")
    
    elif opcionusuario == 4:
        print("Jueves\n")

    elif opcionusuario == 5:
        print("Viernes\n")

    elif opcionusuario == 6:
        print("Sabado\n")

    elif opcionusuario == 7:
        print("Domingo\n")
    
    elif opcionusuario != 9:
        print("\nEntra un numero entre 1 y 7.")
 
## ---> QUESTION 6 <---

food_charge = input("Enter the charge for the food: ")

food_charge = float(food_charge)

# 20% tip
tip = 0.20 * food_charge

# 8% sales tax
sales_tax = 0.08 * food_charge

total_owed = food_charge + tip + sales_tax

print("The tip owed is $"+str(format(tip,",.2f"))+".\n"+"The sales tax owed is $"+str(format(sales_tax,",.2f"))+".\n"+"The total amount owed is $"+str(format(total_owed,",.2f"))+".")

## --> QUESTION 7 <--
number = input ("enter a number between 1 and 100: ")

try:
    number = int(number)
    if number < 1 or number > 100: 
        print("error invalid number")

    elif number % 2 == 0:
        print("number is even")

    elif number % 2 != 0:
        print("number is odd")

except ValueError:
    print("error enter a number")
    
## --> QUESTION 8 <--

first_color, second_color = input("enter the names of two primary colors to mix: ").split()

if first_color == second_color:
    print("enter two different primary colors")

elif first_color == "red" or second_color == "red":
    if first_color == "blue" or second_color == "blue":
        print("you get purple")
    elif first_color == "yellow" or second_color == "yellow":
        print("you get orange")

elif first_color == "blue" or second_color == "blue":
    if first_color == "yellow" or second_color == "yellow":
        print("you get green")

else:
    print("invalid color entry")
