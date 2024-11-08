# PR0405: Ejercicios de programación funcional

### 1.- Filtrado de una lista de números


```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filtrar_lista(numero):
    return numero % 2 == 0

numeros = list(filter(filtrar_lista, numeros))
print(numeros)
```

    [2, 4, 6, 8, 10]


### 2.- Mapeo de temperaturas


```python
celsius = [0, 20, 37, 100]

fahrenheit = list(map(lambda num: (num * 9) / 5 + 32, celsius))
print(fahrenheit)
```

    [32.0, 68.0, 98.6, 212.0]


### 3- Suma acumulativa


```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]

resultado = reduce(lambda acumulado, numero: acumulado + numero, numeros)
print(resultado)
```

    15


### 4.- Palabras con cierta longitud


```python
palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

def filtrar_palabras(palabra):
    if len(palabra) > 5:
        return palabra

palabras = list(filter(filtrar_palabras, palabras))
palabras = list(map(lambda palabra: palabra.upper(), palabras))
print(palabras)
```

    ['ELEFANTE', 'JIRAFA']


### 5.- Multiplicación de pares


```python
numeros = [1, 2, 3, 4, 5, 6]

def es_par(numero):
    return numero % 2 == 0

resultado = list(filter(es_par, numeros))
resultado = reduce(lambda acumulado, numero: acumulado * numero, resultado)
print(resultado)
```

    48


 ### 6.- Combinar operaciones en listas anidada


```python
numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]

def crear_lista_global(listas):
    lista_global = []
    for lista in listas:
        for elemento in lista:
            lista_global.append(elemento)
    return lista_global
    
def es_positivo(numero):
    return numero >= 0

lista_filtrada = crear_lista_global(numeros)
lista_filtrada = list(filter(es_positivo, lista_filtrada))

resultado = reduce(lambda acumulado, numero: acumulado + numero, lista_filtrada)
print(resultado)
```

    30


### 7.- Frecuencia de palabras


```python
texto = "Hola hola mundo mundo cruel".lower()
palabras = texto.split()


def actualizar_diccionario(diccionario, palabra):
    diccionario[palabra] = diccionario[palabra] + 1 if palabra in diccionario else 1
    return diccionario

resultado = reduce(actualizar_diccionario, palabras, {} )
print(resultado)
```

    {'hola': 2, 'mundo': 2, 'cruel': 1}



```python

```
