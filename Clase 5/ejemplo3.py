class ListaEnlazadaAvanzada(ListaEnlazadaSensores):
    """Extensión de la clase gestora con búsqueda y eliminación de memoria."""

    def buscar_sensor(self, id_sensor: str) -> bool:
        """Busca si un sensor existe en la estructura dinámicamente."""
        actual = self.cabeza
        while actual is not None:
            if actual.id_sensor == id_sensor:
                return True
            actual = actual.siguiente
        return False

    def eliminar_sensor(self, id_sensor: str) -> bool:
        """Elimina un nodo desconectando sus referencias en la RAM."""
        actual = self.cabeza
        anterior: "NodoSensor | None" = None

        if actual is None:
            return False  # La lista está vacía

        # Caso 1: El nodo a eliminar es la cabeza de la lista
        if actual.id_sensor == id_sensor:
            self.cabeza = actual.siguiente  # Avanzamos la cabeza
            return True

        # Caso 2: El nodo está en el medio o al final
        while actual is not None and actual.id_sensor != id_sensor:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            return False  # El sensor no se encontró en la lista

        # Reconexión de punteros (se "puentea" el nodo actual)
        anterior.siguiente = actual.siguiente
        return True


# --- PRUEBA DE BÚSQUEDA Y ELIMINACIÓN ---
red_sensores = ListaEnlazadaAvanzada()
red_sensores.insertar_final("S_01", 18.2)
red_sensores.insertar_final("S_ERRONEO", -999.0)  # Lectura ruidosa a eliminar
red_sensores.insertar_final("S_03", 21.4)

print("=== ANTES DE LA ELIMINACIÓN ===")
red_sensores.mostrar_lista()

# Búsqueda
print(f"\n¿Existe S_ERRONEO?: {red_sensores.buscar_sensor('S_ERRONEO')}")

# Eliminación y reconexión
red_sensores.eliminar_sensor("S_ERRONEO")

print("\n=== DESPUÉS DE ELIMINAR Y PUENTEAR EN RAM ===")
red_sensores.mostrar_lista()