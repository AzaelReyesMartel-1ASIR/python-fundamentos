"""
    Primero, bucle *for* para contar los num
    del 1 al 10 con una variable que se incrementa en el bucle.
    Segundo, indicar los pares e impares mediante un condicional.
    Tercero, sumar cada bloque con variable en cada condicional
    y mostrar suma total de pares e impares.
"""

suma_par=0
suma_impar=0

for i in range(1,11):
    if i%2==0:
        print(i,"es par")
        suma_par=suma_par+i
    else:
        print(i,"es impar")
        suma_impar=suma_impar+i
print("Suma total pares:",suma_par)
print("Suma total impares:",suma_impar)
print("Suma total pares e impares:",(suma_impar+suma_par))