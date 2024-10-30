# PR0401: Ejercicios básicos en Python


### 1.- Lectura de un número válido



```python
n = input("Introduce un numero")
while(not n.isdigit()):
    n = input("Introduce un numero")
          
```

    Introduce un numero a
    Introduce un numero a
    Introduce un numero a
    Introduce un numero 5




### 2.-Tabla de multiplicar



```python
n = int(input("Introduce el numero a multiplicar"))
k = int(input("Introduce la cantidad de veces que se va a multiplicar"))

for num in range(k + 1):  
    cadena = str(n) + " * " + str(num) + " = " + str(n * num)
        
    print(cadena)
```

    Introduce el numero a multiplicar 5
    Introduce la cantidad de veces que se va a multiplicar 12


    5 * 0 = 0
    5 * 1 = 5
    5 * 2 = 10
    5 * 3 = 15
    5 * 4 = 20
    5 * 5 = 25
    5 * 6 = 30
    5 * 7 = 35
    5 * 8 = 40
    5 * 9 = 45
    5 * 10 = 50
    5 * 11 = 55
    5 * 12 = 60




### 3.- Triángulo de asteriscos



```python
n = int(input("Introduce el numero de filas"))

for num in range(1, (n + 1)):
    cadena = "*" * num
    print(cadena)
```

    Introduce el numero de filas 5


    *
    **
    ***
    ****
    *****




### 4- Pirámide de asteriscos



```python
n = int(input("Introduce el numero de filas"))
while(n % 2 == 0):
    n = int(input("Introduce el numero de filas"))

for num in range(1, n + 1, 2):
    espacios = int((n - num) / 2)
    print(" " * espacios + ("*" * num))
```

    Introduce el numero de filas 2
    Introduce el numero de filas 9


        *
       ***
      *****
     *******
    *********




### 5.- Número mayor y menor



```python
import math

coleccion = []

for i in range(5):
    n = int(input("Introduce numero"))
    coleccion.append(n)

numMayor = -math.inf
numMenor = math.inf

for j in range(5):
    if(coleccion[j] < numMenor):
        numMenor = coleccion[j]
    if(coleccion[j] > numMayor):
        numMayor = coleccion[j]

print("El numero mayor es: " + str(numMayor))
print("El numero menor es: " + str(numMenor))
```

    Introduce numero 5
    Introduce numero 6
    Introduce numero 2
    Introduce numero 8
    Introduce numero 2


    El numero mayor es: 8
    El numero menor es: 2




### 6.- Conversión de unidades



```python
cantidad = int(input("Introduce la cantidad"))
medida = input("Introduce la medida(milimetros, centimetros, metros, kilometros)")
conversion = input("Introduce la medida a la que lo quieres convertir(milimetros, centimetros, metros, kilometros)")
resultado = -1

match medida:
    case "kilometros":
        match conversion:
            case "metros":
                resultado = cantidad * 1000
            case "centimetros": 
                resultado = cantidad * 100000
            case "milimetros":
                resultado = cantidad * 1000000
    case "metros":
        match conversion:
            case "kilometros":
                resultado = cantidad / 1000
            case "centimetros":
                resultado = cantidad * 100
            case "milimetros":
                resultado = cantidad * 1000
    case "centimetros":
        match conversion:
            case "kilometros":
                resultado = cantidad / 100000
            case "metros":
                resultado = cantidad / 100
            case "milimetros":
                resultado = cantidad * 10
    case "milimetros":
        match conversion:
            case "kilometros":
                resultado = cantidad / 1000000
            case "metros":
                resultado = cantidad / 1000
            case "centimetros":
                resultado = cantidad / 10
print(resultado)
```

    Introduce la cantidad 1
    Introduce la medida(milimetros, centimetros, metros, kilometros) kilometros
    Introduce la medida a la que lo quieres convertir(milimetros, centimetros, metros, kilometros) milimetros


    10000000




### 7.- Acierta el número



```python
from random import *

numAdivinar = randint(1, 101)
n = int(input("Introduce tu numero"))
              
while(n != numAdivinar):
    if(n < numAdivinar):
        print("Más alto")
    else:
        print("Mas bajo")
    n = int(input("Introduce tu numero"))
print("Adivinaste el numero. Era " + str(numAdivinar))
```

    Introduce tu numero 50


    Más alto


    Introduce tu numero 60


    Más alto


    Introduce tu numero 70


    Mas bajo


    Introduce tu numero 61


    Más alto


    Introduce tu numero 62


    Más alto


    Introduce tu numero 63


    Más alto


    Introduce tu numero 64


    Adivinaste el numero. Era 64




### 8.- Piedra, papel o tijeras



```python
posibles_manos = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"]

manos_ganadas_cpu = 0
manos_ganadas_jugador = 0

ganador = False

while(not ganador):
    jugada_cpu = posibles_manos[(randint(0, len(posibles_manos) - 1))].lower()
    jugada_jugador = input("¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock)")
    print("¡La CPU saca " + jugada_cpu + "!")
    ganador_ronda = ""
    match jugada_jugador.lower():
        case "piedra":
            if (jugada_cpu == "tijeras" or jugada_cpu == "lagarto"):
                ganador_ronda = "jugador"
            elif(jugada_cpu == "papel" or jugada_cpu == "spock"):
                ganador_ronda = "cpu"
            else:
                ganador_ronda = "empate"
        case "papel":
            if (jugada_cpu == "piedra" or jugada_cpu == "spock"):
                ganador_ronda = "jugador"
            elif(jugada_cpu == "tijeras" or jugada_cpu == "lagarto"):
                ganador_ronda = "cpu"
            else:
                ganador_ronda = "empate"
        case "tijeras":
            if (jugada_cpu == "papel" or jugada_cpu == "lagarto"):
                ganador_ronda = "jugador"
            elif(jugada_cpu == "piedra" or jugada_cpu == "spock"):
                ganador_ronda = "cpu"
            else:
                ganador_ronda = "empate"
        case "lagarto":
            if (jugada_cpu == "spock" or jugada_cpu == "papel"):
                ganador_ronda = "jugador"
            elif(jugada_cpu == "piedra" or jugada_cpu == "tijeras"):
                ganador_ronda = "cpu"
            else:
                ganador_ronda = "empate"
        case "spock":
            if (jugada_cpu == "piedra" or jugada_cpu == "tijeras"):
                ganador_ronda = "jugador"
            elif(jugada_cpu == "papel" or jugada_cpu == "lagarto"):
                ganador_ronda = "cpu"
            else:
                ganador_ronda = "empate"

    match ganador_ronda:
        case "jugador":
            print("¡Tú ganas!")
            manos_ganadas_jugador += 1
        case "cpu":
            print("¡Gana la CPU")
            manos_ganadas_cpu += 1
        case "empate":
            print("¡Empate!")

    if manos_ganadas_jugador >= 5:
        ganador = True
        print("¡Ganas la partida!")
    elif manos_ganadas_cpu >= 5:
        ganador = True
        print("¡La CPU gana la partida!")

    print("Tus manos ganadas: " + str(manos_ganadas_jugador))
    print("Manos ganadas por la CPU: " + str(manos_ganadas_cpu))
```

    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) piedra


    ¡La CPU saca piedra!
    ¡Empate!
    Tus manos ganadas: 0
    Manos ganadas por la CPU: 0


    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) lagarto


    ¡La CPU saca tijeras!
    ¡Gana la CPU
    Tus manos ganadas: 0
    Manos ganadas por la CPU: 1


    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) spock


    ¡La CPU saca piedra!
    ¡Tú ganas!
    Tus manos ganadas: 1
    Manos ganadas por la CPU: 1


    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) tijeras


    ¡La CPU saca piedra!
    ¡Gana la CPU
    Tus manos ganadas: 1
    Manos ganadas por la CPU: 2


    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) papel


    ¡La CPU saca spock!
    ¡Tú ganas!
    Tus manos ganadas: 2
    Manos ganadas por la CPU: 2


    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) lagarto


    ¡La CPU saca lagarto!
    ¡Empate!
    Tus manos ganadas: 2
    Manos ganadas por la CPU: 2


    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) spock


    ¡La CPU saca papel!
    ¡Gana la CPU
    Tus manos ganadas: 2
    Manos ganadas por la CPU: 3


    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) piedra


    ¡La CPU saca piedra!
    ¡Empate!
    Tus manos ganadas: 2
    Manos ganadas por la CPU: 3


    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) papel


    ¡La CPU saca piedra!
    ¡Tú ganas!
    Tus manos ganadas: 3
    Manos ganadas por la CPU: 3


    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) papel


    ¡La CPU saca tijeras!
    ¡Gana la CPU
    Tus manos ganadas: 3
    Manos ganadas por la CPU: 4


    ¿Qué vas a jugar? (Piedra, Papel, Tijeras, Lagarto, Spock) papel


    ¡La CPU saca lagarto!
    ¡Gana la CPU
    ¡La CPU gana la partida!
    Tus manos ganadas: 3
    Manos ganadas por la CPU: 5




### 9.- Secuencia de Fibonacci



```python
n = int(input("Introduce numero máximo para la secuencia"))

def fib(num):
    if(num <= 1):
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

for i in range (n + 1):
    print(fib(i))
```

    Introduce numero máximo para la secuencia 5


    1
    1
    2
    3
    5
    8
