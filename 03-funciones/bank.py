"""
    Primero, funcion depositar saldo, definir variable global
    para usuario. Igual con la funcion retirar.
    Segundo, condicional para que el saldo no quede nunca en
    negativo.
    Tercero, mostrar el saldo inicial y despues de cada 
    operacion
"""
saldo = 0
prueba_deposito = 100
prueba_retiro = 30
prueba_retiro_excesivo = 500
minimo_introducir = 10

def depositar(saldo, cantidad, minimo_introducir):
    if (cantidad <= 0):
        print("Compruebe que la cantidad sea mayor que 0")
        return saldo
    elif (cantidad < minimo_introducir):
        print("Compruebe que la cantidad que seleccione sea superior o igual a", minimo_introducir)
        return saldo
    else:
        saldo += cantidad
        print("Saldo actualizado correctamente")
        return saldo


def retirar(saldo, cantidad, minimo_introducir):
    if (cantidad > saldo):
        print("Compruebe que su saldo sea superior a la cantidad que desea retirar")
        return saldo
    elif (cantidad < minimo_introducir):
        print("Compruebe que la cantidad que seleccione sea superior o igual a", minimo_introducir)
        return saldo
    else:
        saldo -= cantidad
        print("Saldo retirado correctamente")
        return saldo


def mostrar_saldo(saldo):
    print("Su saldo final es:", saldo)


saldo=depositar(saldo, prueba_deposito, minimo_introducir)
saldo=retirar(saldo, prueba_retiro, minimo_introducir)
saldo=retirar(saldo, prueba_retiro_excesivo, minimo_introducir)
mostrar_saldo(saldo)
input_usuario = int(input("Introduce la cantidad que quieres depositar: "))
saldo=depositar(saldo, input_usuario, minimo_introducir)
input_usuario = int(input("Introduce la cantidad que quieres retirar: "))
saldo=retirar(saldo, input_usuario, minimo_introducir)
mostrar_saldo(saldo)