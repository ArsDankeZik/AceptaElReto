'''
Elige un número de cuatro dígitos que tenga al menos dos diferentes (es válido colocar el dígito 0 al principio, por lo que el número 0009 es válido).

Coloca sus dígitos en orden ascendente y en orden descendente para formar dos nuevos números. Puedes añadir los dígitos 0 que necesites al principio.

Resta el menor al mayor.

Vuelve al paso 2.
'''

import sys
import os

'''
 Solo está creado con el propósito de tener una vista de lo que va 
 sucediendo en el caso de que se le pase un parámetro al programa.
 EX: py -3 main.py [TRUE]
 ----------------------------------------------------------------
'''
def log(msg, active):
    if active == True:
        print(msg)

sys_active = None

if len(sys.argv) > 1:
    sys_active = True
else:
    sys_active = False
# ---------------------------------------------------------------

'''
Leémos la cantidad de números a meter y vamos introduciendo los 
números correspondientes.
EX: 
5
3524
1111
1121
6174
1893
----------------------------------------------------------------
'''
n_numbers = int(input())
items = []
for i in range(0, n_numbers):
    items.append(input())
log(items, sys_active)
# ---------------------------------------------------------------

'''
Función para la validación del número con los requerimientos de
https://www.aceptaelreto.com/problem/statement.php?id=100
@parameter : string (número)
@return : boolean (True sí es incorrecto | False en caso de que sí lo sea)
----------------------------------------------------------------
'''
def validN(n):
    repeticiones = 0
    for i in n:
        if i != "0" or n == "1000":
            repeticiones = n.count(i)   
            if repeticiones > 2:
                return False
    return True


'''
Función para realizar las el sort y el sort reverse con las 
operaciones correspondientes
@parameter : string (número)
@return : int (resultado)
----------------------------------------------------------------
'''
def operation(x):
    nsorted = ''.join(sorted(list(str(x)), reverse=True))
    ninverted = ''.join(sorted(nsorted))

    nsorted = int(nsorted)
    ninverted = int(ninverted)
    log("{} - {} = {}".format(nsorted, ninverted, nsorted-ninverted), sys_active)
    return nsorted - ninverted
# ---------------------------------------------------------------

'''
Llamada a las funciones correspondientes para la comprobaciónd 
de cada número en 'items'
----------------------------------------------------------------
'''
for n in items:    
    times = 0
    if n != 6174 and validN(n):
        while n != 6174 and times-1 != 7:
            n = operation(n)
            times = times + 1 
        print("{0}".format(times))
    else:
        print(0)
