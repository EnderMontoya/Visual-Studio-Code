# --- EJEMPLO 3: Construcción y Recorrido de Nodos en Memoria ---

class NodoSensor:
    """Representa un elemento dinámico en la memoria RAM."""
    def __init__(self, lectura: float):
        self.lectura: float = lectura
        self.siguiente: 'NodoSensor' | None = None  # Apuntador al siguiente nodo


# 1. Creación de tres nodos independientes en la RAM
nodo1 = NodoSensor(12.4)
nodo2 = NodoSensor(15.8)
nodo3 = NodoSensor(18.2)

# 2. Enlazado manual mediante referencias (punteros en Python)
nodo1.siguiente = nodo2  # nodo1 almacena la referencia a nodo2
nodo2.siguiente = nodo3  # nodo2 almacena la referencia a nodo3

# 3. Recorrido dinámico siguiendo la cadena de direcciones
print("--- Recorriendo la Lista Enlazada ---")
nodo_actual = nodo1
while nodo_actual is not None:
    print(f"Lectura: {nodo_actual.lectura}°C | Dirección RAM: {hex(id(nodo_actual))}")
    dir_sig = hex(id(nodo_actual.siguiente)) if nodo_actual.siguiente else "None"
    print(f"  └── Apunta a: {dir_sig}\n")
    nodo_actual = nodo_actual.siguiente
