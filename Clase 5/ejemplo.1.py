class NodoSensor:
    """Representa un elemento individual en la memoria RAM (Unidad 3.3)."""

    def __init__(self, id_sensor: str, lectura: float) -> None:
        self.id_sensor: str = id_sensor
        self.lectura: float = lectura
        self.siguiente: "NodoSensor | None" = None


# --- PRUEBA Y ENLACE MANUAL ---

# 1. Creamos tres instancias independientes en distintas ubicaciones de la RAM
nodo_temperatura = NodoSensor("TEMP_01", 24.5)
nodo_presion = NodoSensor("PRES_01", 101.3)
nodo_flujo = NodoSensor("FLUJ_01", 12.8)

# 2. Conectamos los nodos a mano guardando la referencia del siguiente
nodo_temperatura.siguiente = nodo_presion
nodo_presion.siguiente = nodo_flujo

# 3. Recorremos manualmente siguiendo las referencias de memoria
nodo_actual = nodo_temperatura
print("=== RECORRIDO MANUAL DE NODOS EN MEMORIA ===")

while nodo_actual is not None:
    print(f"Sensor: {nodo_actual.id_sensor} | Lectura: {nodo_actual.lectura}")
    print(f"  └── Dirección actual: {hex(id(nodo_actual))}")
    if nodo_actual.siguiente:
        print(f"  └── Apunta a: {hex(id(nodo_actual.siguiente))}\n")
    else:
        print("  └── Apunta a: None (Fin de la cadena)\n")
    nodo_actual = nodo_actual.siguiente