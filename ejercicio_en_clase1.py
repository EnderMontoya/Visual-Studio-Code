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
        self.siguiente: "NodoEvento | None" = None

class HistorialEvento:
    
    def __init__(self) -> None:
        self.cabeza: "NodoEvento | None" = None

    def regitro_evento(self,lectura: str, tiempo: str, estado: str) -> None:
             if lectura > 60:
                  estado= "critico"
             else:
                  estado= "normal" = None
                 
    def insertar_inicio(self, id_sensor: str, lectura: float, tiempo: str, estado: str) -> None:    
            nuevo_nodo = NodoEvento(id_sensor, lectura, tiempo, estado)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

   

