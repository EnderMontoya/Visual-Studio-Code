import json
from typing import Dict, Any

class GestorConfiguracion:
    """Maneja archivos de configuración JSON con gestión de excepciones."""
    def __init__(self, ruta_config: str) -> None:
        self.ruta_config: str = ruta_config

    def guardar_configuracion(self, parametros: Dict[str, Any]) -> bool:
        """Serializa un diccionario a un archivo JSON."""
        try:
            with open(self.ruta_config, 'w', encoding='utf-8') as archivo:
                json.dump(parametros, archivo, indent=4)
            print(f"✓ [CONFIG]: Parámetros guardados exitosamente en '{self.ruta_config}'.")
            return True
        except (IOError, TypeError) as err:
            print(f"❌ [ERROR AL GUARDAR CONFIG]: {err}")
            return False

    def cargar_configuracion_defensiva(self) -> Dict[str, Any]:
        """Carga configuración. Si el archivo no existe, crea valores por defecto."""
        config_default = {"frecuencia_muestreo_hz": 10, "umbral_alerta_volts": 5.0, "modo": "AUTOMATICO"}
        try:
            with open(self.ruta_config, 'r', encoding='utf-8') as archivo:
                config_cargada = json.load(archivo)
                print(f"✓ [CONFIG CARGADA]: {config_cargada}")
                return config_cargada
        except FileNotFoundError:
            print(f"⚠️ [AVISO]: Archivo '{self.ruta_config}' no hallado. Generando configuración por defecto...")
            self.guardar_configuracion(config_default)
            return config_default
        except json.JSONDecodeError:
            print("❌ [ERROR]: Archivo JSON corrupto. Retornando valores seguros por defecto.")
            return config_default

# --- DEMOSTRACIÓN EJEMPLO 3 ---
if __name__ == '__main__':
    gestor_cfg = GestorConfiguracion('/workspace/scratch/config_planta.json')
    # Intento 1: Carga defensiva (El archivo no existe, lo genera automáticamente)
    cfg = gestor_cfg.cargar_configuracion_defensiva()
    # Modificamos la frecuencia de muestreo y guardamos nuevamente
    cfg['frecuencia_muestreo_hz'] = 50
    gestor_cfg.guardar_configuracion(cfg)
