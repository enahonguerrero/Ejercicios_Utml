from enum import Enum, auto
from typing import List, Optional
from abc import ABC

# --- 1. CLASES AUXILIARES (Extract Class) ---

class Dimension:
    """
    Refactorización: Extraemos la complejidad de las dimensiones 
    a su propia clase en lugar de dejarlo como un atributo vago.
    """
    def __init__(self, valor: float, unidad: str, tipo_medida: str):
        self.valor = valor
        self.unidad = unidad
        self.tipo_medida = tipo_medida # Ej: "Largo", "Superficie", "Profundidad"

    def __repr__(self):
        return f"{self.tipo_medida}: {self.valor} {self.unidad}"

class Lugar:
    def __init__(self, nombre: str, provincia: str, pais: str):
        self.nombre = nombre
        self.provincia = provincia
        self.pais = pais

    def __repr__(self):
        return f"{self.nombre} ({self.provincia}, {self.pais})"

class TipoSitio(Enum):
    """
    Refactorización: Usamos este Enum en lugar de crear 
    subclases vacías (Asentamiento, Enterramiento, etc).
    """
    ASENTAMIENTO = auto()
    ENTERRAMIENTO = auto()
    AREA_EXPLOTACION = auto()

# --- 2. JERARQUÍA PRINCIPAL ---

class EntidadArqueologica(ABC):
    """
    Clase Padre Refactorizada.
    - Contiene 'cronologia' (Pull Up Field).
    - Contiene la relación con Lugar y Dimensiones.
    """
    def __init__(self, codigo: str, cronologia: str, lugar: Lugar):
        self.codigo = codigo
        self.cronologia = cronologia # Movido aquí desde las subclases
        self.lugar = lugar
        self.dimensiones: List[Dimension] = []

    def agregar_dimension(self, dimension: Dimension):
        self.dimensiones.append(dimension)

    def __str__(self):
        return f"[{self.codigo}] {self.__class__.__name__} ({self.cronologia})"

# --- 3. SUBCLASES CONCRETAS ---

class SitioArqueologico(EntidadArqueologica):
    """
    Representa un sitio singular.
    Sustituye la herencia compleja anterior por un atributo 'tipo'.
    """
    def __init__(self, codigo: str, cronologia: str, lugar: Lugar, tipo: TipoSitio):
        super().__init__(codigo, cronologia, lugar)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f" - Tipo: {self.tipo.name}"

class ConjuntoArqueologico(EntidadArqueologica):
    """
    Representa una agrupación.
    Usa el patrón COMPOSITE: contiene una lista de EntidadArqueologica.
    """
    def __init__(self, codigo: str, cronologia: str, lugar: Lugar):
        super().__init__(codigo, cronologia, lugar)
        self.elementos: List[EntidadArqueologica] = []

    def agregar_elemento(self, entidad: EntidadArqueologica):
        self.elementos.append(entidad)

    def mostrar_detalle(self):
        print(f"{self} contiene:")
        for elemento in self.elementos:
            # Recursividad simple para mostrar contenido
            print(f"  -> {elemento}")

# --- EJEMPLO DE USO ---

if __name__ == "__main__":
    # 1. Crear Objetos Auxiliares
    lugar_sevilla = Lugar("Valencina", "Sevilla", "España")
    
    # 2. Crear Sitios (Refactorizado: Usando Enum en vez de clases distintas)
    dolmen = SitioArqueologico(
        "S01", "Edad del Cobre", lugar_sevilla, TipoSitio.ENTERRAMIENTO
    )
    dolmen.agregar_dimension(Dimension(50, "m", "Longitud Corredor"))

    taller = SitioArqueologico(
        "S02", "Edad del Cobre", lugar_sevilla, TipoSitio.AREA_EXPLOTACION
    )

    # 3. Crear Conjunto (Composite)
    yacimiento_completo = ConjuntoArqueologico("C01", "Neolítico-Bronce", lugar_sevilla)
    
    # El conjunto agrupa los sitios anteriores
    