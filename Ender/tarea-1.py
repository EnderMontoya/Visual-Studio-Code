import copy
from typing import Callable

# --- 1. Definición del Objeto Sensor ---
class SensorTemperatura:
    """Representa un sensor de temperatura industrial."""
    def __init__(self, identificador: str, lectura: float):
        self.identificador: str = identificador
        self.lectura: float = lectura

# --- 2. Apuntadores a Funciones (Manejadores de Eventos / Callbacks) ---
def alarma_luces(sensor: SensorTemperatura) -> None:
    """Callback 1: Enciende luces de advertencia."""
    print(f"🚨 [LUCES]: ¡Alerta en {sensor.identificador}! Valor: {sensor.lectura}°C")

def alarma_sonora(sensor: SensorTemperatura) -> None:
    """Callback 2: Activa la sirena de emergencia."""
    print(f"🔊 [SIRENA]: ¡Sonando alarma por {sensor.identificador}!")

# --- 3. Función que recibe Apuntadores a Funciones (Callbacks) ---
def evaluar_sensor(sensor: SensorTemperatura, umbral: float, manejadores: list[Callable[[SensorTemperatura], None]]) -> None:
    """Evalúa un sensor y ejecuta la lista de funciones callbacks si excede el umbral."""
    if sensor.lectura > umbral:
        print(f"\n⚠️ [UMBRAL EXCEDIDO en {sensor.identificador}]:")
        for callback in manejadores:
            callback(sensor)  # Invocación de la función por referencia

# --- Execution Block ---
if __name__ == "__main__":
    s1 = SensorTemperatura("SENSOR_01", 85.5)
    s2 = SensorTemperatura("SENSOR_02", 42.0)

    # Arreglo de Referencias a Objetos
    planta_principal = [s1, s2]

    # Arreglo de Apuntadores a Funciones (Callbacks)
    protocolo_emergencia = [alarma_luces, alarma_sonora]

    # Demostración de Copia Profunda vs Superficial
    planta_respaldo = copy.deepcopy(planta_principal)
    planta_respaldo[0].lectura = 100.0  # No afecta a planta_principal[0]

    # Evaluación usando callbacks
    for s in planta_principal:
        evaluar_sensor(s, umbral=80.0, manejadores=protocolo_emergencia)