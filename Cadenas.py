# texto_variado = 'palbras 123 +-*'
# print (type (texto_variado))

# # podemos utilizar comillas triples para que el texto se muestre como una cadena que hemos escrito 
# print ("""" 
# Funcionamiento de 
# programa: (opciones)
#     -1 para a opciones 
#     -2 ára salir 
# """)

####################################################################################
# subscripting e indexado

# texto = 'Python'

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])
  
# print(texto[6])  # Error! no podemos acceder a una posicion que no existe
# print(texto[-7]) # Error! no podemos acceder a una posicion que no existe 

# letra = texto[0]
# print(letra)

# #texto[0] = 'p' # error! no podemos modificar una cadena

# letra = 'p'
# print(letra)

# texto_compuesto = letra + texto[1] # concatenacion 
# print(texto_compuesto)

#################################################################################

# Slicing o Substringing

# texto = 'Python'

# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1])

# print(texto[::-1])
# print(texto[1:50])

##################################################################################

# Cadenas y formatos 

# texto = 'Hola Mundo! BuenasTardes'
# print (texto.lower())
# print (texto.upper())
# print (texto.capitalize())
# print (texto.title())
# print (texto.swapcase())
# texto = texto.upper()
# print(texto)

# print('{} + {} = {}'.format(2, 3, 2+3))
# print('{} + {} = {}'.format ('Hola', 'Mundo', 'Hola Mundo'))
# print('{:.3f} + {:.4f} = {}'.format(2, 3, 2+3))
# print('{1} + {0} = {2}'.format(2, 3, 2+3))
# print('{2} + {0} = {1}'.format('Hola', 'Mundo', 'Hola Mundo'))
# print('{:d} = {:b} = {:o} = {:x}'.format(15, 15, 15, 15))




