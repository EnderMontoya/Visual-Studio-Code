# 1. Creamos una variable
temperatura = 25

# 2. Mostramos el ID en decimal (el número 'feo' y largo)
print(id(temperatura))  
# Resultado: 140708912345600

# 3. Lo convertimos a Hexadecimal para ver la 'dirección de memoria' real
print(hex(id(temperatura)))  
# Resultado: 0x7f8a1234  (El '0x' solo significa "esto está en Hexadecimal")
