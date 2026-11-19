import csv
from typing import List, Dict

class DataloggerTexto:
    """Administra el registro secuencial de datos telemétricos en CSV."""
    def __init__(self, ruta_archivo: str) -> None:
        self.ruta_archivo: str = ruta_archivo

    def registrar_lecturas(self, lecturas: List[Dict[str, float]]) -> None:
        """Escribe encabezados y filas telemétricas en modo append ('a')."""
        encabezados = ["timestamp", "voltaje", "temperatura"]
        try:
            # Modo 'a' (append) agrega datos al final sin borrar el contenido previo
            with open(self.ruta_archivo, mode='a', newline='', encoding='utf-8') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=encabezados)
                # Escribir encabezado solo si el archivo está vacío
                if archivo.tell() == 0:
                    escritor.writeheader()
                for lectura in lecturas:
                    escritor.writerow(lectura)
            print(f"✓ [OK]: {len(lecturas)} lecturas registradas en {self.ruta_archivo}")
        except IOError as error:
            print(f"❌ [ERROR I/O]: No se pudo escribir en el archivo: {error}")

    def leer_historial(self) -> None:
        """Lee y muestra el archivo CSV renglón por renglón."""
        try:
            with open(self.ruta_archivo, mode='r', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                print(f"\n=== HISTORIAL DE TELEMETRÍA ({self.ruta_archivo}) ===")
                for fila in lector:
                    print(f"Tiempo: {fila['timestamp']}s | Voltaje: {fila['voltaje']}V | Temp: {fila['temperatura']}°C")
        except FileNotFoundError:
            print(f"⚠️ [ADVERTENCIA]: El archivo '{self.ruta_archivo}' aún no existe.")

# --- DEMOSTRACIÓN EJEMPLO 1 ---
if __name__ == '__main__':
    logger = DataloggerTexto('D:/Ender/telemetria.csv')
    datos_muestra = [
        {'timestamp': 2.0, 'voltaje': 4.01, 'temperatura': 33.5},
        {'timestamp': 4.5, 'voltaje': 4.4, 'temperatura': 20.0},
        {'timestamp': 7.0, 'voltaje': 17.0, 'temperatura': 28.5}
    ]
    logger.registrar_lecturas(datos_muestra)
    logger.leer_historial()
