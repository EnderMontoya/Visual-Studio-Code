# --- EJEMPLO 1: Variables como Etiquetas en la RAM --- 
# Dos variables apuntando al mismo entero en memoria 

voltaje_1 = 5.0 
voltaje_2 = voltaje_1 

print(f"Dirección de voltaje_1: {hex(id(voltaje_1))}") 
print(f"Dirección de voltaje_2: {hex(id(voltaje_2))}") 

# ¡Ambas muestran exactamente la misma dirección en la RAM! 
# # Si modificamos voltaje_1, Python crea un NUEVO flotante en otra dirección 

voltaje_1 = voltaje_1 + 1.5 

print("\n--- Después de modificar voltaje_1 ---") 
print(f"Nuevo voltaje_1 ({voltaje_1}V) en dirección: {hex(id(voltaje_1))}") 
print(f"voltaje_2 sigue siendo ({voltaje_2}V) en: {hex(id(voltaje_2))}")