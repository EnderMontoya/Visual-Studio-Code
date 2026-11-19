import struct
from typing import Tuple

class DataloggerBinario:
    """Maneja tramas binarias de tamaño fijo (Acceso Directo)."""
    # Formato: id_sensor (int 4B), voltaje (float 4B), temp (float 4B) -> Total = 12 Bytes
    FORMATO_TRAMA = "<iff"  # Little-endian, integer, float, float
    TAMANIO_TRAMA = struct.calcsize(FORMATO_TRAMA)

    def __init__(self, ruta_binaria: str) -> None:
        self.ruta_binaria: str = ruta_binaria

    def guardar_trama_binaria(self, id_sensor: int, voltaje: float, temp: float) -> None:
        """Empaqueta y escribe 12 bytes en el archivo binario ('ab')."""
        trama_empaquetada = struct.pack(self.FORMATO_TRAMA, id_sensor, voltaje, temp)
        with open(self.ruta_binaria, 'ab') as archivo:
            archivo.write(trama_empaquetada)
        print(f"-> [BINARIO]: Trama de {len(trama_empaquetada)} bytes escrita.")

    def leer_registro_especifico(self, indice_registro: int) -> Tuple[int, float, float] | None:
        """Acceso Directo: Salta directamente al registro 'N' sin leer los anteriores."""
        offset = indice_registro * self.TAMANIO_TRAMA
        try:
            with open(self.ruta_binaria, 'rb') as archivo:
                # Desplazamos el puntero de archivo directamente al offset objetivo
                archivo.seek(offset, 0)  # 0 = desde el inicio del archivo
                bloque = archivo.read(self.TAMANIO_TRAMA)
                if len(bloque) < self.TAMANIO_TRAMA:
                    print(f"⚠️ [ADVERTENCIA]: El registro #{indice_registro} no existe.")
                    return None
                id_s, volt, temp = struct.unpack(self.FORMATO_TRAMA, bloque)
                return id_s, volt, temp
        except FileNotFoundError:
            print("❌ [ERROR]: Archivo binario no encontrado.")
            return None

# --- DEMOSTRACIÓN EJEMPLO 2 ---
if __name__ == '__main__':
    bin_logger = DataloggerBinario('/workspace/scratch/sensores.dat')
    # Escribimos 3 registros de 12 bytes cada uno
    bin_logger.guardar_trama_binaria(101, 3.31, 22.4)
    bin_logger.guardar_trama_binaria(102, 5.02, 28.1)
    bin_logger.guardar_trama_binaria(103, 12.05, 45.0)

    # Acceso Directo al registro #1 (segundo registro, índice base 0) sin leer el registro 0
    registro = bin_logger.leer_registro_especifico(1)
    if registro:
        print(f"\n=== ACCESO DIRECTO REGISTRO #1 ===")
        print(f"ID Sensor: {registro[0]} | Voltaje: {registro[1]:.2f}V | Temp: {registro[2]:.2f}°C")
