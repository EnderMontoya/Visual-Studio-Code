class Glosario:
    def __init__(self) -> None:
        self.terminos: dict[str,str]={}

    def agregar_terminos(self,palabra:str,concepto:str) -> None:
        palabra_actual=palabra.strip()
        self.terminos[palabra_actual]=concepto.strip().lower()
        return f"termino guardado,{palabra_actual.upper()}"
    
    def buscar_terminos(self,palabra:str) ->str:
        palabra_buscar=palabra.strip()
        concepto = self.terminos.get (palabra_buscar)
    
    def mostrar_todos (self) -> None:
        if not self.terminos:
            print ("no hay glosario")
            return
        for palabra,concepto in self.terminos.items():
            print(f"{palabra}:{concepto}")
            
if __name__ == "__main__":
    diccionario= Glosario()
    diccionario.agregar_terminos("robot","maquina electromecanica programable semiautomatica")
    diccionario.agregar_terminos("maquina","es un aparato mecanico")
    buscar=diccionario.buscar_terminos("robot")
    print(buscar)
    diccionario.mostrar_todos()
