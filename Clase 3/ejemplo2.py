# --- EJEMPLO 2: El 'Efecto Fantasma' con Listas Mutables --- 
# Un buffer de lecturas de temperatura
# 
buffer_original = [23.5, 24.1, 22.8] 
buffer_respaldo = buffer_original 

# CUIDADO: No es una copia, es la misma dirección 

print(f"ID Original: {hex(id(buffer_original))}")
print(f"ID Respaldo: {hex(id(buffer_respaldo))}") 

# Agregamos una lectura crítica al respaldo 
buffer_respaldo.append(85.0) 

# ¡El buffer original también cambió porque comparten el mismo ID! 
print(f"\nBuffer Original modificado sin querer: {buffer_original}") 

# ¿CÓMO SE SOLUCIONA? Haciendo una copia explícita en otra dirección de RAM: 
buffer_copia_real = buffer_original.copy() 
print(f"ID Copia Real: {hex(id(buffer_copia_real))}") # ¡Dirección distinta!
