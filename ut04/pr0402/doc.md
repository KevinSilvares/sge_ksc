# PR0402: Ejercicios de Cadenas

### 1.- Contar vocales y consonante


```python
cadena = input("Escribe una cadena").lower()

num_vocales = 0
num_consonantes = 0

for i in range (0, len(cadena)):
    if(cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "u" or cadena[i] == "o"):
        num_vocales += 1
    elif(cadena[i] != "a" or cadena[i] != "e" or cadena[i] != "i" or cadena[i] != "u" or cadena[i] != "o") and cadena[i].isalpha():
        num_consonantes += 1
        
print("Numero de vocales: " + str(num_vocales))
print("Numero de consonantes: " + str(num_consonantes))
```

    Escribe una cadena Hola Adios


    Numero de vocales: 4
    Numero de consonantes: 5


### 2.- Invertir una cadena


```python
cadena = input("Escribe una cadena")

nueva_cadena = ""

for i in range(len(cadena) - 1, -1, -1):
    nueva_cadena += cadena[i]

print(nueva_cadena)
```

    Escribe una cadena hola


    aloh


### 3.- Verificar palíndromo


```python
cadena = input("Escribe una cadena").lower()

longitud_cadena = len(cadena)
num_coincidencias = 0

for i in range (0, longitud_cadena):
    cadena_al_reves = cadena[::-1]
    if cadena_al_reves[i] == cadena[i]:
        num_coincidencias += 1
        
if(num_coincidencias == longitud_cadena):
    print("Es un palindromo")
else:
    print("No es un palindromo")
        
```

    Escribe una cadena aaoaa


    Es un palindromo


### 4.- Contar palabras


```python
cadena = input("Escribe una cadena")
palabras = cadena.split()
print("Has escrito " + str(len(palabras)) + " palabras")
```

    Escribe una cadena Hola Adios Que Tal


    Has escrito 4 palabras


### 5.- Eliminar caracteres repetidos


```python
cadena = input("Escribe una cadena")

nueva_cadena = ""

print(cadena.replace("a", "", ))
```

    Escribe una cadena hola que tal


    hol que tl


### 6.- Mayúsculas y minúsculas


```python
cadena = input("Escribe una cadena")

nueva_cadena = ""

for i in range (0, len(cadena)):
    if(cadena[i].islower()):
        nueva_cadena += cadena[i].upper()
    else:
        nueva_cadena += cadena[i].lower()

print(nueva_cadena)
```

    Escribe una cadena HoLa


    hOlA


### 7.- Invertir palabras de una cadena


```python
cadena = input("Escribe una cadena")
palabras = cadena.split()
nuevas_palabras = ""

for i in range (len(palabras) -1, -1,  -1):
    nuevas_palabras += palabras[i] + " "

print(nuevas_palabras)
```

    Escribe una cadena Hola Que Tal


    Tal Que Hola 


### 8.- Anagrama


```python
cadena = input("Escribe una cadena").lower()
cadena_dos = input("Escribe otra cadena").lower()

num_coincidencias = 0

if(len(cadena) == len(cadena_dos)):
    for letra in cadena:
        if(cadena.count(letra) == cadena_dos.count(letra)):
            num_coincidencias += 1
else:
    print("No es un anagrama")
        
if num_coincidencias == len(cadena):
    print("Es un anagrama")
```

    Escribe una cadena coleta
    Escribe otra cadena lacteo


    Es un anagrama


### 10.- Quitar caracteres alfanuméricos


```python
cadena = input("Escribe una cadena")
nueva_cadena = ""

for letra in cadena:
    if letra.isalpha():
        nueva_cadena += letra
print(nueva_cadena)
```

    Escribe una cadena hola2, que1, tal


    holaquetal


### 11.- Transformar a camelCase


```python
import re

cadena = input("Escribe una cadena").lower()
palabras = re.split("[ -]", cadena)
nueva_cadena = palabras[0]

for palabra in palabras[1:]:
    nueva_cadena += palabra[0].upper() + palabra[1:].lower() # Lo podría haber hecho con capitalize() o title() y hubiera sido más fácil

print(nueva_cadena)
```

    Escribe una cadena hola-que Tal


    holaQueTal


### 12.- Codificación RLE (Run-Length Enconding)


```python
cadena = input("Escribe una cadena")

letra_actual = ''
letra_anterior = cadena[0]
contador = 0

cadena_resultado = ""

for letra in cadena:
    letra_actual = letra
    if letra_actual == letra_anterior:
        contador += 1
    else:
        cadena_resultado += letra_anterior + str(contador)
        contador = 1
    letra_anterior = letra_actual
    
cadena_resultado += letra_anterior + str(contador)
print(cadena_resultado)
```

    Escribe una cadena aaabbcc


    a3b2c2


### 13.- Decodificar RLE


```python
cadena = input("Escribe una cadena (codificada)")
limite_uno = 0
limite_dos = 1

cadena_resultado = ""

while(limite_dos <= len(cadena)):
    cadena_resultado += cadena[limite_uno] * int(cadena[limite_dos])
    limite_uno += 2
    limite_dos += 2

print(cadena_resultado)
```

    Escribe una cadena (codificada) a3b2c2


    aaabbcc


### 14.- Formateo de cadenas con plantillas


```python
cadena = input("Escribe una cadena")

datos = {
    "nombre" : "Kevin",
    "edad" : 23
}

palabras = cadena.split(" ")

cadena_resultado = ""

for palabra in palabras:
    if palabra[0] == "{":
        cadena_resultado += str(datos[palabra[1:-1]]) + " "
    else:
        cadena_resultado += palabra + " "

print(cadena_resultado)
```

    Escribe una cadena Me llamo {nombre} y tengo {edad} años


    Me llamo Kevin y tengo 23 años 


### 15.- Comparar cadenas por valor ASCII


```python
def comparar_cadena(cadena, cadena_dos):
    numero_cadena_uno = 0
    numero_cadena_dos = 0
    
    for letra in cadena:
        numero_cadena_uno += ord(letra)

    for letra in cadena_dos:
        numero_cadena_dos += ord(letra)

    if numero_cadena_uno > numero_cadena_dos:
        print("La cadena uno tiene un valor ASCII más alto")
    else:
        print("La cadena dos tiene un valor ASCII más alto")

cadena = input("Escribe una cadena")
cadena_dos = input("Escribe otra cadena")

comparar_cadena(cadena, cadena_dos)

```

    Escribe una cadena aaa
    Escribe otra cadena a


    La cadena uno tiene un valor ASCII más alto


### 16.- Contar la longitud de palabra más larga


```python
cadena = input("Escribe una cadena")

palabras = cadena.split(" ")
palabra_mas_larga = ""

for palabra in palabras:
    if(len(palabra) > len(palabra_mas_larga)):
        palabra_mas_larga = palabra
print("La palabra mas larga es: " + palabra_mas_larga)
```

    Escribe una cadena Hola que tal estas


    La palabra mas larga es: estas


### 17.- Formatear número con separador de miles


```python
cadena = input("Introduce un numero")
contador = 0
cadena_resultado = ""

for numero in cadena[::-1]:
    contador += 1
    cadena_resultado += numero
    if contador >= 3:
        cadena_resultado += '.'
        contador = 0

print(cadena_resultado[::-1])
```

    Introduce un numero 1234556


    1.234.556

