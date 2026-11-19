import copy

# ACA CREO LA CLASE COMANDO
class Comando:
    def __init__(self, cod, prec):
        self.cod = cod
        self.prec = prec

# ESTE ES EL NODO PARA LA PILA QUE GUARDA EL COMANDO Y EL APUNTADOR SIGUIENTE
class NodoComando:
    def __init__(self, com):
        self.com = com
        self.siguiente = None

# AQUI ESTA LA PILA CON EL PUNTERO CABEZA
class PilaComandos:
    def __init__(self):
        self.cabeza = None

    # METODO PARA INSERTAR AL INICIO O(1)
    def insertar_al_inicio(self, com):
        nuevo = NodoComando(com)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # METODO DE PURGA PARA QUE EL GARBAGE COLLECTOR BORRE LOS MENORES A 80
    def purgar_imprecisos(self):
        
        while self.cabeza is not None and self.cabeza.com.prec < 80.0:
            self.cabeza = self.cabeza.siguiente

        if self.cabeza is None:
            return
        
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.com.prec < 80.0:
                
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

    # ESTO MUESTRA COMO QUEDO LA PILA
    def mostrar_pila(self):
        actual = self.cabeza
        if actual is None:
            print("pila vacia")
            return
        
        while actual is not None:
            print("comando:", actual.com.cod, " precision:", actual.com.prec)
            actual = actual.siguiente

if __name__ == "__main__":
    
    # DEEPCOPY
    print(" prueba de copy")
    c1 = Comando("mover arriba", 40.0)
    
    # ESTA ES LA COPIA PROFUNDA
    c2 = copy.deepcopy(c1)
    
    # MODIFICO LA COPIA PARA MOSTRAR QUE NO AFECTO AL ORIGIAL
    c2.cod = "mover abajo"
    c2.prec = 88.0

    print("original:", c1.cod, c1.prec)
    print("copia modificada:", c2.cod, c2.prec)

    # AQUI PRUEBO LA PILA Y METO VARIOS VALORES PARA PROBARLA
    print("\n prueba de pila y purga ")
    pila = PilaComandos()
    
    pila.insertar_al_inicio(Comando("girar der", 95.0))
    pila.insertar_al_inicio(Comando("bajar brazo", 45.0)) 
    pila.insertar_al_inicio(Comando("avanzar", 82.0))
    pila.insertar_al_inicio(Comando("subir", 30.0))       
    print("como queda al inicio:")
    pila.mostrar_pila()

    print("\npurgando")
    pila.purgar_imprecisos()

    print("\npurgado:")
    pila.mostrar_pila()