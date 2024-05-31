# Desarrollaremos una calculadora de indice de masa corporal 
# IMC = peso en kilograamos / estatura en metros al cuadrado

#creamos uan funcion para que no queden datos vacios   
def obtener_datos (mensaje, tipo = str, valida = lambda x: x.strip() != ""):
    while  True:
        dato = input(mensaje).strip()
        try:
            dato = tipo(dato)
            if valida(dato):
                return dato
        except ValueError:
            pass
        print('Entrada inválida, por favor, inténtelo de nuevo.')
        
# Creamos una funcion usando la formula para el IMC
def calcular_imc(peso, altura):
     imc = peso / (altura ** 2)
     return imc
 
# Creamos una funcion usando la clasificación de IMC según las categorías estándar
def clasificar_imc(imc):
     if imc < 18.9:
         return "Bajo peso"
     elif 18.5 <= imc < 24.99:
         return "Normal"
     elif 25 <= imc < 29.99:
         return "Sobrepeso"
     elif 30 <= imc < 34.99:
         return "Obesidad tipo I"
     elif 35 <= imc < 39.99:
         return "Obesidad tipo II"
     else:
         return ('Obesidad tipo III')
     
# Obtenemos datos del usuraio       
nombre = obtener_datos('Ingrese su nombre porfavor:')
apellido_paterno = obtener_datos('Ingrese su apellido paterno:')
apellido_materno = obtener_datos('Ingrese su apellido materno:')
edad = obtener_datos('Cuantos años tines:', int, lambda x: x > 18)
peso = obtener_datos('Cual es tu peso en kg:', int, lambda x: x > 0)
estatura = obtener_datos('Cual es tu estatura en metros:', float, lambda x: x > 0)

# Calcular el IMC llamando a la función
indice_masa_corporal = calcular_imc(peso, estatura)
        
# Clasificar el IMC llamando a la función de clasificación
clasificacion = clasificar_imc(indice_masa_corporal)

# Mostrar resultados
print("\nInformación del Usuario:")
print(f"Nombre Completo: {nombre}")
print(f"Tu apellido paterno: {apellido_paterno}")
print(f"Tu appelido materno: {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso en kg: {peso:.2f}")
print(f"Estatura en metros: {estatura}")
print(f"Tu IMC es: {indice_masa_corporal:.2f}")
print(f"Clasificación: {clasificacion}")
