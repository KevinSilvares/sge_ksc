# PR0404: Ejercicios con diccionarios

### 1.- Buscar valor en un diccionario


```python
cadena = input("Introduce fruta")

frutas = {
    "Pera" : 1.3,
    "Manzana" : 1,
    "Naranja" : 1.5,
    "Platano" : 1.1
}

if frutas.get(cadena) != None:
    print("El precio de " + cadena + " es " + str(frutas.get(cadena)))
else:
    print("Fruta no válida")
```

    Introduce fruta Pera


    El precio de Pera es 1.3


### 2.- Contar elementos en un diccionario


```python
productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}
num_total_productos = 0

for clave in productos.keys():
    num_total_productos += len(productos.get(clave))

print("El diccionario tiene " + str(len(productos.keys())) + " categorías")
print("El diccionario tiene " + str(len(productos.get("Electrónica"))) + " productos por categoría")
print("El diccionario tiene " + str(num_total_productos) + " productos en total")
```

    El diccionario tiene 5 categorías
    El diccionario tiene 5 productos por categoría
    El diccionario tiene 25 productos en total


### 3.- Contador de frecuencias de palabras


```python
cadena = input("Escribe una cadena")
cadena_segmentada = cadena.split()

palabras = {palabra:0 for palabra in cadena_segmentada}

for palabra in cadena_segmentada:
    palabras[palabra] = palabras.get(palabra) + 1

print(palabras)
```

    Escribe una cadena hola adios que tal hola hola adios


    {'hola': 3, 'adios': 2, 'que': 1, 'tal': 1}


### 4.- Diccionario de listas


```python
print("""\
    1.- Listar estudiantes matriculados en una asignatura
    2.- Matricular un estudiante en una asignatura
    3.- Dar de baja un estudiante de una asignatura
""")

accion = int(input("Introduce un número para llevar a cabo una acción"))

asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

match accion:
    case 1:
        asignatura = input("Introduce asignatura CON TILDES (Matemáticas, Física, Programación, Historia, Inglés)")
        print("Estudiantes matriculados en " + asignatura + ": ")
        print(asignaturas.get(asignatura))
    case 2:
        alumno = input("Introduce alumno para matricular")
        asignatura = input("Introduce asignatura CON TILDES (Matemáticas, Física, Programación, Historia, Inglés)")
        asignaturas.get(asignatura).append(alumno)
        print("Alumno añadido a " + asignatura)
        print(asignaturas[asignatura])
    case 3:
        alumno = input("Introduce alumno para dar de baja")
        asignatura = input("Introduce asignatura CON TILDES (Matemáticas, Física, Programación, Historia, Inglés)")
        asignaturas.get(asignatura).remove(alumno)
        print("Alumno eliminado de " + asignatura)
        print(asignaturas[asignatura])
```

        1.- Listar estudiantes matriculados en una asignatura
        2.- Matricular un estudiante en una asignatura
        3.- Dar de baja un estudiante de una asignatura
    


    Introduce un número para llevar a cabo una acción 3
    Introduce alumno para dar de baja Carlos
    Introduce asignatura CON TILDES (Matemáticas, Física, Programación, Historia, Inglés) Inglés


    Alumno eliminado de Inglés
    ['Sofía', 'Jorge', 'María']


### 5.- Diccionario invertido


```python
frutas = {
    "Pera" : 1.3,
    "Manzana" : 1,
    "Naranja" : 1.5,
    "Platano" : 1.1
}

frutas_invertido = {frutas.get(fruta):fruta for fruta in frutas}
print(frutas_invertido)
```

    {1.3: 'Pera', 1: 'Manzana', 1.5: 'Naranja', 1.1: 'Platano'}


### 6.- Combinar dos diccionarios

### 7.- Filtrar claves y valores


```python
umbral = float(input("Escribe un numero para filtrar"))

empleados = {
    "Paco" : 1000,
    "Belen" : 200,
    "Ana" : 1500,
    "Manolo" : 1689,
    "Alejandra" : 1370,
    "Juan" : 1050,
}

for empleado in empleados:
    if empleados.get(empleado) >= umbral:
        print(empleado)

```

    Escribe un numero para filtrar 1200.2


    Ana
    Manolo
    Alejandra



```python

```
