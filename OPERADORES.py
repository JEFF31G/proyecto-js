"""
OPERADORES
"""

# Operadores Aritméticos
print (f"suma: 10 + 3 = {10 + 3}")
print (f"resta: 10 - 3 = {10 - 3}")
print (f"multplicacion: 10 * 3 = {10 * 3}")
print (f"dibicion: 10 / 3 = {10 / 3}")
print (f"modulo: 10 % 3 = {10 % 3}")
print (f"potencia: 10 ** 3 = {10 ** 3}")
print (f"division entera: 10 // 3 = {10 // 3}")

# Operadores de Comparación
print (f"10 > 3 = {10 > 3}")
print (f"10 < 3 = {10 < 3}")
print (f"10 >= 3 = {10 >= 3}")
print (f"10 <= 3 = {10 <= 3}")
print (f"10 == 3 = {10 == 3}")
print (f"10 != 3 = {10 != 3}")

# Operadores Lógicos
print (f"True and False = {True and False}")
print (f"True or False = {True or False}")
print (f"not True = {not True}")

# Operadores de Asignación
a = 10
print (f"a = {a}")
a += 5
print (f"a += 23 = {a}")
a -= 5
print (f"a -= 5 = {a}")
a *= 5
print (f"a *= 5 = {a}")
a /= 5
print (f"a /= 5 = {a}")
a %= 5
print (f"a %= 5 = {a}")
a **= 5
print (f"a **= 5 = {a}")
a //= 5
print (f"a //= 6 = {a}")

print (f"a &= 5 = {a}")

# Operadores de Identidad
a = [1, 2, 3]
b = a
print (f"a is b = {a is b}")
print (f"a is not b = {a is not b}")

# Operadores de pertenencia
a = [1, 2, 3]
b = a
print (f"2 in a = {b in a}")
print (f"4 in a = {b not in a}")

# Operadores Bit a Bit
a = 69
b = 23
print (f"a & b = {a & b}")
print (f"a | b = {a | b}")
print (f"a ^ b = {a ^ b}")
print (f"~a = {~a}")
print (f"a << 2 = {a << 2}")
print (f"a >> 2 = {a >> 2}")

# Operadores de Membresía
a = [1, 2, 3]
b = 2
print (f"b in a = {b in a}")
print (f"b not in a = {b not in a}")

"""
estructuras de control
"""

# condicionales

my_variable = "10"
if my_variable == "10":
    print("es 10")
elif my_variable == "20":
    print("es 20")
else:
    print("no es 10 ni 20")

    # interativas

for i in range(23):
    print(i)

i = 8
while i < 23:
    print(i)
    i += 1

    # MANEJO DE EXCEPCIONES

try:
    print("23 / 8")
except:
    print("no se puede dividir entre cero")
finally:
    print("hemos terminado")

# FUNCIONES

def suma(A, b):
    return a + b        
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b
def potencia(a, b):
    return a ** b
def modulo(a, b):
    return a % b
def division_entera(a, b):
    return a // b

# FUNCIONES LAMBDA
suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplicacion = lambda a, b: a * b
division = lambda a, b: a / b
potencia = lambda a, b: a ** b
modulo = lambda a, b: a % b
division_entera = lambda a, b: a // b

# FUNCIONES RECURSIVAS

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# FUNCIONES ANIDADAS

def funcion_externa(x):
    def funcion_interna(y):
        return x + y
    return funcion_interna

# FUNCIONES DE ORDEN SUPERIOR

def funcion_de_orden_superior(funcion, x):
    return funcion(x)
def suma(x):
    return x + 1
def resta(x):
    return x - 1
def multiplicacion(x):
    return x * 2
def division(x):
    return x / 2
def potencia(x):
    return x ** 2
def modulo(x):
    return x % 2
def division_entera(x):
    return x // 2

# FUNCIONES DE ALTO NIVEL

def funcion_de_alto_nivel(funcion, x):
    return funcion(x)
def suma(x):
    return x + 1           
def resta(x):
    return x - 1
def multiplicacion(x):
    return x * 2
def division(x):
    return x / 2
def potencia(x):
    return x ** 2
def modulo(x):
    return x % 2
def division_entera(x):
    return x // 2

# FUNCIONES DE BAJO NIVEL

def funcion_de_bajo_nivel(funcion, x):
    return funcion(x)
def suma(x):
    return x + 1
def resta(x):
    return x - 1
def multiplicacion(x):
    return x * 2
def division(x):
    return x / 2
def potencia(x):
    return x ** 2
def modulo(x):
    return x % 2
def division_entera(x):
    return x // 2

"""
extra
"""
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number) 