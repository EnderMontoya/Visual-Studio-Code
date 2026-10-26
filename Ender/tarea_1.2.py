
from typing import Callable

# --- 1. Definición del Objeto Sensor ---
class SensorTemperatura:
    """Representa un simport copyensor de temperatura industrial."""
    def __init__(self, identificador: str, lectura: float):
        self.identificador: str = identificador
        self.lectura: float = lectura

# --- 2. Apuntadores a Funciones (Manejadores de Eventos / Callbacks) ---
def alarma_luces(sensor: SensorTemperatura) -> None:
    """Callback 1: Enciende luces de advertencia."""
    print(f"🚨 [LUCES]:   ¡Alerta en {sensor.identificador}! Valor: {sensor.lectura}°C")

def alarma_sonora(sensor: SensorTemperatura) -> None:
    """Callback 2: Activa la sirena de emergencia."""
    print(f"🔊 [SIRENA]:  ¡Sonando alarma por {sensor.identificador}!")

def alarma_telefonica(sensor: SensorTemperatura) -> None:
    """Callback 3: llama a bomberos."""
    print(f"📱 [llamada]: ¡llamando a bomberos por culpa de este sensor {sensor.identificador}!")    

# --- 2,5. sistema de luses que se activan si un sensor no se activa ---
def evaluar_sensor_no_activo(sensor: SensorTemperatura, umbral: float, manejadores: list[Callable[[SensorTemperatura], None]]) -> None:
    """Evalúa un sensor y ejecuta la lista de funciones callbacks si excede el umbral."""
    if sensor.lectura < umbral:
        print(f"\n⚠️ [UMBRAL NO EXCEDIDO en {sensor.identificador}]:")
        for callback in manejadores:
            callback(sensor) 

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
    s3 = SensorTemperatura("SENSOR_03", 93.2)

    # Arreglo de Referencias a Objetos
    planta_principal = [s1, s2, s3]

    # Arreglo de Apuntadores a Funciones (Callbacks)
    protocolo_emergencia = [alarma_luces, alarma_sonora, alarma_telefonica]

    # Demostración de Copia Profunda vs Superficial
    planta_respaldo = copy.deepcopy(planta_principal)
    planta_respaldo[0].lectura = 100.0  # No afecta a planta_principal[0]

    # Evaluación usando callbacks
    for s in planta_principal:
        evaluar_sensor(s, umbral=80.0, manejadores=protocolo_emergencia)