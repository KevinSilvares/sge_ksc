# PR0403: Ejercicios con listas

## 1.- Operaciones con listas

### 1.1.- Ordenando elementos


```python
nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]
nombres.sort(reverse = True)
print(nombres)
```

    ['Óscar', 'Ángela', 'Ángel', 'Álvaro', 'Álex', 'Víctor', 'Victoria', 'Vicente', 'Verónica', 'Valentín', 'Tomás', 'Teresa', 'Tamara', 'Sofía', 'Silvia', 'Sergio', 'Sebastián', 'Sara', 'Santiago', 'Salvador', 'Rubén', 'Rosa', 'Rocío', 'Roberto', 'Ricardo', 'Raúl', 'Raquel', 'Ramón', 'Rafael', 'Pilar', 'Pedro', 'Paula', 'Patricia', 'Pablo', 'Olga', 'Nuria', 'Noelia', 'Nicolás', 'Natalia', 'Mónica', 'Miriam', 'Milagros', 'Miguel', 'Mercedes', 'María', 'Marta', 'Mario', 'Marina', 'Mariano', 'Marcos', 'Marcos', 'Marcelo', 'Manuela', 'Manuel', 'Luis', 'Lucía', 'Lourdes', 'Lorena', 'Lidia', 'Leandro', 'Laura', 'Julián', 'Julio', 'Julia', 'Juan', 'Jorge', 'Joaquín', 'Joaquín', 'Jesús', 'Javier', 'Iván', 'Ismael', 'Isabel', 'Irene', 'Inés', 'Inmaculada', 'Héctor', 'Humberto', 'Hugo', 'Guillermo', 'Gregorio', 'Gonzalo', 'Gloria', 'Gemma', 'Gema', 'Gabriela', 'Félix', 'Fátima', 'Francisco', 'Fernando', 'Federico', 'Fausto', 'Fabián', 'Eva', 'Eugenio', 'Esther', 'Esteban', 'Esperanza', 'Enrique', 'Emilio', 'Emilia', 'Elsa', 'Elisa', 'Elena', 'Eduardo', 'Dolores', 'Diego', 'David', 'Daniela', 'Daniel', 'César', 'Cristina', 'Cristina', 'Consuelo', 'Claudia', 'Celia', 'Carolina', 'Carmen', 'Carlos', 'Carla', 'Candela', 'Braulio', 'Blanca', 'Berta', 'Belén', 'Beatriz', 'Baltasar', 'Ariadna', 'Araceli', 'Aníbal', 'Antonio', 'Andrés', 'Andrea', 'Ana', 'Amparo', 'Amalia', 'Alicia', 'Alfredo', 'Alfonso', 'Alejandro', 'Alejandra', 'Alberto', 'Ainhoa', 'Agustín', 'Adrián', 'Adela']


### 1.2.- Contando elementos


```python
nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]
num_ocurrencias = 0

for nombre in nombres:
    if nombre[0] == 'A' or nombre[0] == 'Á':
        num_ocurrencias += 1

print(num_ocurrencias)
```

    23


### 1.3.- Buscar un elementos


```python
cadena = input("Escribe nombre a buscar")

nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]

existe = False

for nombre in nombres:
    if nombre == cadena:
        existe = True

if existe:
    print("El nombre está en la lista")
else:
    print("El nombre no está en la lista")
        
```

    Escribe nombre a buscar Alejandro


    El nombre está en la lista


### 1.4.- Primeros elementos


```python
cadena = input("Escribe nombre a buscar")

nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]

indice = -1

for nombre in nombres:
    if nombre == cadena:
        indice = nombres.index(nombre)

if indice != -1:
    for nombre in nombres:
        if nombres.index(nombre) != indice:
            print(nombre)
        else:
            break;
```

    Escribe nombre a buscar Miguel


    Alejandro
    María
    Javier
    Lucía
    Carlos
    Sofía


### 1.5.- Obtener número de nombres de una longitud


```python
num_caracteres = int(input("Escribe una longitud"))

nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]

num_ocurrencias = 0

for nombre in nombres:
    if len(nombre) == num_caracteres:
        num_ocurrencias += 1

print(num_ocurrencias)
```

    Escribe una longitud 7


    30


### 1.6.- Nombres cortos


```python
nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]

lista_nombres_cortos = []

for nombre in nombres:
    if len(nombre) <= 4:
        lista_nombres_cortos.append(nombre)

print(lista_nombres_cortos)
```

    ['Ana', 'Juan', 'Luis', 'Sara', 'Hugo', 'Eva', 'Rosa', 'Raúl', 'Iván', 'Olga', 'Álex', 'Inés', 'Gema', 'Elsa']


### 1.7.- Número de vocales


```python
nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]

vocales = {
    'a' : 0,
    'e' : 0,
    'i' : 0,
    'o' : 0,
    'u' : 0
}

for nombre in nombres:
    vocales['a'] += nombre.lower().count('a')
    vocales['e'] += nombre.lower().count('e')
    vocales['i'] += nombre.lower().count('i')
    vocales['o'] += nombre.lower().count('o')
    vocales['u'] += nombre.lower().count('u')

print(vocales)
```

    {'a': 152, 'e': 78, 'i': 75, 'o': 65, 'u': 29}


### 1.8.- Número de letras


```python
nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]

letras = {i:0 for i in "abcdefghijklmnñopqrstuvwxyz"}

for nombre in nombres:
    for caracter in nombre.lower():
        if letras.get(caracter) != None: # Ignora tildes
            letras[caracter] += 1

print(letras)
```

    {'a': 152, 'b': 17, 'c': 34, 'd': 28, 'e': 78, 'f': 11, 'g': 20, 'h': 5, 'i': 75, 'j': 11, 'k': 0, 'l': 70, 'm': 32, 'n': 62, 'ñ': 0, 'o': 65, 'p': 7, 'q': 4, 'r': 79, 's': 41, 't': 27, 'u': 29, 'v': 12, 'w': 0, 'x': 2, 'y': 0, 'z': 3}


### 2.1.- Sumar elementos de una lista


```python
lista_uno = [11, 5, 7, 8]
lista_dos = [56, 8, 2, 123]

lista_dos.extend(lista_uno)

print(sum(lista_dos))
```

    220


### 2.2.- Contar elementos específicos


```python
cadena = input("Escribe una palabra")

palabras = ["Hola", "Adios", "Que Tal", "Adios", "Hola"]

print("La palabra aparece " + str(palabras.count(cadena)) + " veces en la lista")
```

    Escribe una palabra Hola


    La palabra aparece 2 veces en la lista


### 2.3.- Eliminar duplicados


```python
numeros = [1, 2, 3, 4, 1 ,2 ,7, 8, 9, 10, 10, 8]
numeros_unicos = []

for numero in numeros:
    if numeros.count(numero) == 1:
        numeros_unicos.append(numero)

print(numeros_unicos)
```

    [3, 4, 7, 9]


### 2.4.- Máximo y mínimo


```python
import math

numeros = [1, 2, 3, 4, 1 ,2 ,7, 8, 9, 10, 10, 8]

num_maximo = -math.inf
num_minimo = math.inf

for numero in numeros:
    if numero < num_minimo:
        num_minimo = numero
    elif numero > num_maximo:
        num_maximo = numero

print("El numero maximo es " + str(num_maximo))
print("El numero minimo es " + str(num_minimo))
```

    El numero maximo es 10
    El numero minimo es 1


### 2.5.- Filtrar números pares


```python
numeros = [1, 2, 3, 4, 1 ,2 ,7, 8, 9, 10, 10, 8]
numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(numeros_pares)
```

    [2, 4, 2, 8, 10, 10, 8]


### 2.6.- Revertir una lista


```python
numeros = [1, 2, 3, 4, 1 ,2 ,7, 8, 9, 10, 10, 8]
lista_inversa = []

for numero in numeros[::-1]:
    lista_inversa.append(numero)

print(lista_inversa)
```

    [8, 10, 10, 9, 8, 7, 2, 1, 4, 3, 2, 1]


### 2.7.- Concatenar listas


```python
lista_uno = [11, 5, 7, 8]
lista_dos = [56, 8, 2, 123]

lista_resultado = []

for num_uno, num_dos in zip(lista_uno, lista_dos):
    lista_resultado.append(num_uno)
    lista_resultado.append(num_dos)
    
print(lista_resultado)
```

    [11, 56, 5, 8, 7, 2, 8, 123]


### 2.8.- Encuentra elementos comunes


```python
lista_uno = ["Hola", "Adios", "Que Tal", "Hasta Luego"]
lista_dos = ["Adios", "Hola"]

lista_comunes = []

for palabra_uno in lista_uno:
    for palabra_dos in lista_dos:
        if palabra_uno == palabra_dos:
            lista_comunes.append(palabra_uno)

print(lista_comunes)
```

    ['Hola', 'Adios']


### 2.9.- Dividir una lista


```python
numeros = [1, 2, 3, 4, 1 ,2 ,7, 8, 9, 10, 10, 8]
menores = []
mayores = []

media = sum(numeros) / len(numeros)

for numero in numeros:
    if numero >= media:
        mayores.append(numero)
    else:
        menores.append(numero)

print("Media: " + str(media))
print("--Mayores--")
print(mayores)
print("--Menores--")
print(menores)
```

    Media: 5.416666666666667
    --Mayores--
    [7, 8, 9, 10, 10, 8]
    --Menores--
    [1, 2, 3, 4, 1, 2]
