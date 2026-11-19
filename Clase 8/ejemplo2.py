class NodoDoble:
    """Clase autoreferenciada con doble puntero (siguiente y anterior)."""
    def __init__(self, id_sensor: str, lectura: float):
        self.id_sensor: str = id_sensor
        self.lectura: float = lectura
        self.siguiente: 'NodoDoble' | None = None
        self.anterior: 'NodoDoble' | None = None

class ListaDoblementeEnlazada:
    """Permite recorridos bidireccionales en memoria RAM."""
    def __init__(self):
        self.cabeza: NodoDoble | None = None
        self.cola: NodoDoble | None = None

    def agregar_final(self, id_sensor: str, lectura: float) -> None:
        nuevo = NodoDoble(id_sensor, lectura)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo

    def recorrer_hacia_adelante(self) -> None:
        actual = self.cabeza
        print("\n--- Recorrido Adelante (Cabeza -> Cola) ---")
        while actual is not None:
            print(f"[{actual.id_sensor}: {actual.lectura}V]", end=" <-> ")
            actual = actual.siguiente
        print("End")

    def recorrer_hacia_atras(self) -> None:
        actual = self.cola
        print("\n--- Recorrido Atrás (Cola -> Cabeza) ---")
        while actual is not None:
            print(f"[{actual.id_sensor}: {actual.lectura}V]", end=" <-> ")
            actual = actual.anterior
        print("Start")

# --- DEMOSTRACIÓN ---
if __name__ == "__main__":
    panel = ListaDoblementeEnlazada()
    panel.agregar_final("CANAL_1", 3.3)
    panel.agregar_final("CANAL_2", 5.0)
    panel.agregar_final("CANAL_3", 1.8)
    panel.agregar_final("CANAL_4", 3.0)
    panel.agregar_final("CANAL_5", 5.6)
    panel.agregar_final("CANAL_6", 7.4)

    panel.recorrer_hacia_adelante()
    panel.recorrer_hacia_atras()