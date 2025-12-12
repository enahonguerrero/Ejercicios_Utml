from abc import ABC, abstractmethod
from typing import List

# --- 1. STATE INTERFACE (La interfaz del Estado) ---
class UsoEdificio(ABC):
    """
    Define la interfaz común para todos los usos posibles del edificio.
    """
    @abstractmethod
    def describir_actividad(self):
        pass

    @abstractmethod
    def calcular_coeficiente_impuesto(self) -> float:
        pass

# --- 2. CONCRETE STATES (Los Estados Concretos) ---
class EstadoHospital(UsoEdificio):
    def __init__(self, numero_camas: int):
        self.numero_camas = numero_camas

    def describir_actividad(self):
        print(f"  - Funciona como HOSPITAL con capacidad para {self.numero_camas} camas.")

    def calcular_coeficiente_impuesto(self) -> float:
        return 0.5  # Los hospitales pagan menos impuestos (ejemplo)

class EstadoEscuela(UsoEdificio):
    def __init__(self, tipo: str):
        self.tipo = tipo  # Primaria, Secundaria, Universidad

    def describir_actividad(self):
        print(f"  - Funciona como ESCUELA de nivel {self.tipo}.")

    def calcular_coeficiente_impuesto(self) -> float:
        return 0.8  # Impuesto reducido educativo

class EstadoVivienda(UsoEdificio):
    def __init__(self, familias: int):
        self.familias = familias

    def describir_actividad(self):
        print(f"  - Funciona como VIVIENDA para {self.familias} familias.")

    def calcular_coeficiente_impuesto(self) -> float:
        return 1.2  # Impuesto residencial estándar

# --- 3. CONTEXT (El Edificio) ---
class Edificio:
    """
    El Contexto. Mantiene una referencia a uno o varios estados concretos.
    El comportamiento del edificio cambia según los estados que contenga.
    """
    def __init__(self, direccion: str):
        self.direccion = direccion
        # Para permitir simultaneidad, usamos una lista en lugar de una variable única.
        self.usos_activos: List[UsoEdificio] = []

    def agregar_uso(self, uso: UsoEdificio):
        """Transición o adición de estado."""
        self.usos_activos.append(uso)

    def limpiar_usos(self):
        """Reinicia el edificio (ej. queda abandonado o vacío)."""
        self.usos_activos = []

    def mostrar_situacion_actual(self):
        print(f"\n--- Estado del Edificio en {self.direccion} ---")
        if not self.usos_activos:
            print("  (Edificio actualmente sin uso / abandonado)")
            return
            
        for uso in self.usos_activos:
            # Polimorfismo: Delega la acción al objeto estado
            uso.describir_actividad()

    def calcular_impuestos_totales(self, base_imponible: float):
        total = 0
        for uso in self.usos_activos:
            total += base_imponible * uso.calcular_coeficiente_impuesto()
        print(f"  > Impuestos totales a pagar: ${total:.2f}")

# --- EJECUCIÓN DEL MODELO (Línea de tiempo) ---

if __name__ == "__main__":
    # 1. Se construye el edificio
    edificio_centro = Edificio("Av. Libertad 123")