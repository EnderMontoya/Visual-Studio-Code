class ListaEnlazadaSensores:
    """Clase gestora que administra la cadena de nodos dinámicos."""

    def __init__(self) -> None:
        self.cabeza: "NodoSensor | None" = None

    def insertar_inicio(self, id_sensor: str, lectura: float) -> None:
        """Inserta un nodo al inicio de la cadena en tiempo O(1)."""
        nuevo_nodo = NodoSensor(id_sensor, lectura)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_final(self, id_sensor: str, lectura: float) -> None:
        """Inserta un nodo al final de la cadena recorriendo la memoria O(N)."""
        nuevo_nodo = NodoSensor(id_sensor, lectura)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def mostrar_lista(self) -> None:
        """Recorre la lista e imprime la secuencia ordenada de sensores."""
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía.")
            return

        elementos = []
        while actual is not None:
            elementos.append(f"[{actual.id_sensor}: {actual.lectura}°C]")
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")


# --- PRUEBA DE LA CLASE GESTORA ---
sistema_monitoreo = ListaEnlazadaSensores()

# Inserción al inicio (O(1))
sistema_monitoreo.insertar_inicio("SENSOR_URGENTE", 95.0)

# Inserción al final (O(N))
sistema_monitoreo.insertar_final("SENSOR_TANQUE_1", 22.0)
sistema_monitoreo.insertar_final("SENSOR_TANQUE_2", 23.5)

print("=== ESTADO DE LA LISTA ENLAZADA ===")
sistema_monitoreo.mostrar_lista()