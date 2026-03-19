## USO BÁSICO DE WHILE
# Inicializamos el contador
numero_actual = 1

# El ciclo se ejecuta mientras numero_actual sea menor o igual a 5
while numero_actual <= 5:
    print(numero_actual)
    # Incrementamos para evitar un ciclo infinito y alcanzar el final
    numero_actual += 1



## USO BÁSICO DE FOR
lista_frutas = ["manzana", "plátano", "naranja"]

# Recorre cada elemento de la lista uno por uno
for fruta in lista_frutas:
    print(fruta)

# El ciclo finaliza automáticamente cuando se agotan los elementos de la lista.


## CONDICIÓN EN UN CICLO
# Generamos números del 1 al 10 usando range()
for numero_evaluado in range(1, 11):
    # Verificamos si el residuo de la división por 2 es cero (par)
    if numero_evaluado % 2 == 0:
        print(f"{numero_evaluado}: Par")
    else:
        print(f"{numero_evaluado}: Impar")

# El ciclo termina al llegar al final del rango definido.


## CICLO INFINITO CONTROLADO CON BREAK
while True:
    # Solicitamos la entrada y la convertimos a entero
    entrada_usuario = int(input("Ingresa un número (0 para salir): "))
    
    # La condición de salida se controla internamente
    if entrada_usuario == 0:
        print("Saliendo del programa...")
        break  # Rompe el ciclo inmediatamente
    
    print(f"Ingresaste el número: {entrada_usuario}")


    ## CICLO ANIDADO
    # El primer ciclo controla el multiplicador principal
for i in range(1, 4):
    print(f"--- Tabla del {i} ---")
    # El segundo ciclo realiza las multiplicaciones internas
    for j in range(1, 11):
        resultado_multiplicacion = i * j
        print(f"{i} x {j} = {resultado_multiplicacion}")

# El ciclo exterior termina cuando i llega a 3 y el interior completa su última vuelta.


## USO DE CONTÍNUE
lista_nombres = ["Ana", "Juan", "Pedro", "Lucía"]

# Recorremos la lista de nombres
for nombre_persona in lista_nombres:
    # Si el nombre es "Juan", saltamos a la siguiente iteración
    if nombre_persona == "Juan":
        continue 
    
    # Esta línea no se ejecuta si el nombre fue "Juan"
    print(f"Hola, {nombre_persona}")

# El ciclo termina tras evaluar el último nombre de la lista.

