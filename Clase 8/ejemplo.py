class NodoMensaje:
    """Nodo autoreferenciado con un dato de texto."""
    def __init__(self, mensaje: str):
        self.mensaje: str = mensaje
        self.siguiente: 'NodoMensaje' | None = None

class ColaFIFO:
    """Estructura FIFO: El primer mensaje en entrar es el primero en salir."""
    def __init__(self):
        self.frente: NodoMensaje | None = None
        self.final: NodoMensaje | None = None

    def enqueue(self, mensaje: str) -> None:
        nuevo = NodoMensaje(mensaje)
        if self.final is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def dequeue(self) -> str | None:
        if self.frente is None:
            return None
        msj = self.frente.mensaje
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return msj

class PilaLIFO:
    """Estructura LIFO: El último comando en entrar es el primero en ejecutarse."""
    def __init__(self):
        self.tope: NodoMensaje | None = None

    def push(self, comando: str) -> None:
        nuevo = NodoMensaje(comando)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def pop(self) -> str | None:
        if self.tope is None:
            return None
        cmd = self.tope.mensaje
        self.tope = self.tope.siguiente
        return cmd

# --- DEMOSTRACIÓN DE USO ---
if __name__ == "__main__":
    # 1. Cola FIFO para lecturas de sensores
    cola_sensores = ColaFIFO()
    cola_sensores.enqueue("LECTURA_1: 44.0°C")
    cola_sensores.enqueue("LECTURA_2: 24.0°C")
    cola_sensores.enqueue("LECTURA_3: 25.5°C")
    print(f"Atendiendo FIFO: {cola_sensores.dequeue()}")

    # 2. Pila LIFO para parada de emergencia
    pila_urgente = PilaLIFO()
    pila_urgente.push("APAGAR_MOTOR")
    pila_urgente.push("CERRAR_VALVULA_EMERGENCIA")
    print(f"Atendiendo LIFO urgente: {pila_urgente.pop()}")