class NodoArbol:
    """Clase autoreferenciada jerárquica para un Árbol Binario."""
    def __init__(self, lectura: float):
        self.lectura: float = lectura
        self.izquierdo: 'NodoArbol' | None = None
        self.derecho: 'NodoArbol' | None = None

class ArbolBusquedaTemperatura:
    """Estructura jerárquica no lineal para ordenamiento de datos."""
    def __init__(self):
        self.raiz: NodoArbol | None = None

    def insertar(self, lectura: float) -> None:
        self.raiz = self._insertar_recursivo(self.raiz, lectura)

    def _insertar_recursivo(self, actual: NodoArbol | None, lectura: float) -> NodoArbol:
        if actual is None:
            return NodoArbol(lectura)
        
        if lectura < actual.lectura:
            actual.izquierdo = self._insertar_recursivo(actual.izquierdo, lectura)
        else:
            actual.derecho = self._insertar_recursivo(actual.derecho, lectura)
        return actual

    def recorrido_inorden(self, actual: NodoArbol | None) -> None:
        """Imprime los datos ordenados de menor a mayor (Inorden)."""
        if actual is not None:
            self.recorrido_inorden(actual.izquierdo)
            print(f"[{actual.lectura}°C]", end=" ")
            self.recorrido_inorden(actual.derecho)

# --- DEMOSTRACIÓN ---
if __name__ == "__main__":
    arbol = ArbolBusquedaTemperatura()
    lecturas = [25.4, 18.2, 30.1, 12.0, 22.5, 28.0]
    for temp in lecturas:
        arbol.insertar(temp)

    print("\n=== LECTURAS ORDENADAS AUTOMÁTICAMENTE (RECORRIDO INORDEN) ===")
    arbol.recorrido_inorden(arbol.raiz)
    print("\n")
