print("Bienvenido a Autubidoo, el asistente de pujas automáticas de bidooo.com")

### Configuración de conexión a bidooo.com
print("Por favor, introduce tu nombre de usuario y contraseña para continuar.")
username = input("Usuario: ")
password = input("Contraseña: ")
print("Conectando a bidooo.com...")
# Aquí iría el código para conectarse a bidooo.com con las credenciales proporcionadas 

print("Conexión exitosa. Ahora puedes empezar a pujar automáticamente en las subastas de bidooo.com.")


### Configuración de pujas automáticas
print("Configura tus pujas automáticas.")

respuesta = "aaa"
respuesta_incorrecta = False

while respuesta != "si":
    respuesta = "aaa"
    url_subasta = input("Introduce el URL de la subasta en la que quieres pujar: ")
    nombre_del_producto = "aaa" #Buscar el nombre del producto en la URL 
    while respuesta not in ("no", "si"):
        respuesta = input(f"El producto de la subasta es:{nombre_del_producto} (si/no): ").lower()
        if respuesta not in ("no", "si"):
            print("Por favor, responde con 'si' o 'no'.")
            respuesta_incorrecta = True
        elif respuesta == "no":
            print("Parece que ha habido un error con la URL.")
            respuesta_incorrecta = False
        else:
            print("¡Perfecto! Procedemos a configurar los parámetros de puja.")
            respuesta_incorrecta = False

### PRECIO MÍNIMO
activar_precio_mínimo = False
respuesta = "aaa"

while respuesta not in ("no", "si"):
    respuesta = input ("¿Quieres introducir un precio mínimo para iniciar la puja? (si/no)").lower()
    if respuesta == "si":
        activar_precio_mínimo = True
    elif respuesta == "no":
        activar_precio_mínimo = False
    else:
        print("Por favor, responde con 'si' o 'no'.")

if activar_precio_mínimo:
    precio_mínimo= input("Introduce el precio mínimo:")
    while precio_mínimo not in range (0,200000):
        print("No has introducido un valor valido.")
        precio_mínimo= input("Introduce el precio mínimo:")
    print (f"Precio mínimo se ha establecido: {precio_mínimo}€")

### PRECIO MÁXIMO
activar_precio_máximo = False
respuesta = "aaa"

while respuesta not in ("no", "si"):
    respuesta = input ("¿Quieres introducir un precio máximo para iniciar la puja? (si/no)").lower()
    if respuesta == "si":
        activar_precio_máximo = True
    elif respuesta == "no":
        activar_precio_máximo = False
    else:
        print("Por favor, responde con 'si' o 'no'.")

if activar_precio_máximo:
    precio_máximo= input("Introduce el precio mínimo:")
    while precio_máximo not in range (0,200000):
        print("No has introducido un valor valido.")
        precio_máximo= input("Introduce el precio mínimo:")
    print (f"Precio máximo se ha establecido: {precio_máximo}€")

### PUJAS MÁXIMAS:
activar_pujas_máximas = False
respuesta = "aaa"

while respuesta not in ("no", "si"):
    respuesta = input ("¿Quieres introducir un precio máximo para iniciar la puja? (si/no)").lower()
    if respuesta == "si":
        activar_pujas_máximas = True
    elif respuesta == "no":
        activar_pujas_máximas = False
    else:
        print("Por favor, responde con 'si' o 'no'.")

if activar_pujas_máximas:
    pujas_máximas= input("Introduce el precio mínimo:")
    while pujas_máximas not in range (0,200000):
        print("No has introducido un valor valido.")
        pujas_máximas= input("Introduce el precio mínimo:")
    print (f"Precio máximo se ha establecido: {pujas_máximas}€")

