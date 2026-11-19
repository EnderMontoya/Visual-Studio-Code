# Se requiere un sistema de monitoreo para una caldera industrial. 
# El software debe registrar lecturas de presión dinámicamente mediante la clase autoreferenciada NodoEvento y la clase gestora HistorialEventos. 
# Debe permitir registrar eventos al inicio O(1), contar eventos críticos, mostrar la cadena y realizar una purga de eventos normales 
# reconectando punteros para liberar memoria RAM.
class NodoEvento:
    def __init__(self, id_sensor: str, lectura: float, tiempo: str, estado: str) -> None:
        self.id_sensor: str = id_sensor
        self.lectura: float = lectura
        self.tiempo: str = tiempo
        self.estado: str = estado
        self.siguiente: "NodoEvento" | None = None


class HistorialEventos:
    def __init__(self) -> None:
        self.cabeza: "NodoEvento" | None = None

    def registrar_evento(self, id_sensor: str, lectura: float, tiempo: str) -> None:
        """Determina automáticamente el estado segun la lectura y lo inserta al inicio O(1)."""
        # Determina si es crítico o normal segun la lectura de precion
        if lectura > 68:
            estado = "critico"
        else:
            estado = "normal"
            
        # Crea el nuevo nodo y lo inserta al inicio O(1)
        nuevo_nodo = NodoEvento(id_sensor, lectura, tiempo, estado)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def contar_criticos(self) -> int:
        """Recorre la cadena sumando cuantos eventos tienen estado 'critico'."""
        contador = 0
        actual = self.cabeza
        while actual is not None:
            if actual.estado == "critico":
                contador += 1
            actual = actual.siguiente
        return contador

    def mostrar_cadena(self) -> None:
        """Muestra todos los eventos de la lista enlazada"""
        actual = self.cabeza
        if actual is None:
            print("El historial de eventos esta vacio")
            return
        
        elementos = []
        while actual is not None:
            elementos.append(f"[{actual.id_sensor}: {actual.lectura}psi - {actual.estado}]")
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")

    def purgar_normales(self) -> None:
        """Elimina los eventos normales reconectando punteros, 
        dejando únicamente los eventos críticos"""
        
        # Si la cabeza de la lista es un evento normal se debe saltar
        while self.cabeza is not None and self.cabeza.estado == "normal":
            self.cabeza = self.cabeza.siguiente  # Desconecta la cabeza vieja
            
        # Si la lista quedo vacia
        if self.cabeza is None:
            return

        # Recorre el resto de la lista reconectando punteros
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.estado == "normal":
                # Puentea el nodo normal para sacarlo de la memoria RAM
                actual.siguiente = actual.siguiente.siguiente
            else:
                # Si no es normal avanza al siguiente nodo normal
                actual = actual.siguiente


# --- BLOQUE DE PRUEBA
if __name__ == "__main__":
    historial = HistorialEventos()
    
    
    historial.registrar_evento("SENSOR_01", 45.5, "10:00")
    historial.registrar_evento("SENSOR_02", 78.2, "10:05") 
    historial.registrar_evento("SENSOR_03", 50.0, "10:10")
    historial.registrar_evento("SENSOR_04", 88.9, "10:15") 

    print("=== HISTORIAL ANTES DE LA PURGA ===")
    historial.mostrar_cadena()
    
    print(f"\nCantidad de eventos críticos: {historial.contar_criticos()}")

    print("\nEjecutando purga de eventos normales (liberando RAM)...")
    historial.purgar_normales()

    print("\n=== HISTORIAL DESPUÉS DE LA PURGA (Solo Críticos) ===")
    historial.mostrar_cadena()