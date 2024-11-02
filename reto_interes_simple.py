''' 
El interés simple es el dinero extra que se gana o se paga por prestar o invertir una cantidad de dinero, calculado solo sobre el monto inicial (o capital).

Por ejemplo, si prestas $100 a una tasa de interés simple del 5% anual durante 3 años, el interés será:
C * i * t = I
100×0.05×3=15

Así que, al final, recibirías $115 en total ($100 de capital + $15 de interés).

1 ) Crear una aplicacion en python que le permita al usuario calcular el total a pagar de una deuda 
el programa debe solicitar al usuario los montos de: 
(capital inicial, tasa de interes anual, tiempo en años) 
'''


# Función que calcula el valor a pagar
def calcular_interes_simple(capital, tasa_interes, tiempo):
    interes = capital * tasa_interes * tiempo
    total_a_pagar = capital + interes
    return total_a_pagar

# Entrada de datos por consola
capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (en porcentaje): ")) / 100
tiempo = float(input("Ingrese el tiempo en años: "))

# Se invoca la funcion calcular_interes_simple para obtener el valor a pagar
total = calcular_interes_simple(capital_inicial, tasa_interes_anual, tiempo)

# Impresion del resultado en pantalla
print(f"El valor total a pagar después de {tiempo} años es: ${total}")
