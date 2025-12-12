from abc import ABC, abstractmethod
from typing import List

# --- NIVEL 4: ELEMENTOS ARQUITECTÓNICOS (Las partes más pequeñas) ---

class ElementoArquitectonico(ABC):
    """Clase abstracta para cualquier elemento de la fachada."""
    def __init__(self, material: str, estado: str):
        self.material = material
        self.estado = estado  # Ej: 'Bueno', 'Deteriorado'

    def __str__(self):
        return f"{self.__class__.__name__} de {self.material} ({self.estado})"

class Portada(ElementoArquitectonico):
    def __init__(self, material: str, estado: str, estilo_artistico: str):
        super().__init__(material, estado)
        self.estilo_artistico = estilo_artistico

class Ventana(ElementoArquitectonico):
    def __init__(self, material: str, estado: str, tipo_vidrio: str):
        super().__init__(material, estado)
        self.tipo_vidrio = tipo_vidrio

class Balcon(ElementoArquitectonico):
    def __init__(self, material: str, estado: str, tiene_reja: bool):
        super().__init__(material, estado)
        self.tiene_reja = tiene_reja

# --- NIVEL 3: EL EDIFICIO (Contenedor de elementos) ---

class Edificio:
    """
    Representa un edificio situado en un espacio.
    Tiene una relación de COMPOSICIÓN con sus elementos arquitectónicos.
    """
    def __init__(self, numero: int, estilo: str):
        self.numero = numero
        self.estilo = estilo
        self.elementos_fachada: List[ElementoArquitectonico] = []

    def agregar_elemento(self, elemento: ElementoArquitectonico):
        self.elementos_fachada.append(elemento)

    def describir_fachada(self):
        print(f"  -> Edificio N.{self.numero} ({self.estilo}):")
        for elem in self.elementos_fachada:
            print(f"      * {elem}")

# --- NIVEL 2: ESPACIOS ABIERTOS (Calles y Plazas) ---

class EspacioAbierto(ABC):
    """Clase abstracta base para lugares donde hay edificios."""
    def __init__(self, nombre: str):
        self.nombre = nombre
        # Relación de AGREGACIÓN con Edificios
        self.edificios: List[Edificio] = []

    def registrar_edificio(self, edificio: Edificio):
        self.edificios.append(edificio)

class Calle(EspacioAbierto):
    def __init__(self, nombre: str, es_peatonal: bool):
        super().__init__(nombre)
        self.es_peatonal = es_peatonal

class Plaza(EspacioAbierto):
    def __init__(self, nombre: str, tiene_fuente: bool):
        super().__init__(nombre)
        self.tiene_fuente = tiene_fuente

# --- NIVEL 1: CIUDAD (El contenedor principal) ---

class Ciudad:
    """
    La ciudad se COMPONE de espacios abiertos.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.espacios: List[EspacioAbierto] = []

    def agregar_espacio(self, espacio: EspacioAbierto):
        self.espacios.append(espacio)

    def informe_riqueza_arquitectonica(self):
        print(f"--- INFORME DE LA CIUDAD: {self.nombre.upper()} ---")
        for espacio in self.espacios:
            tipo = "Peatonal" if isinstance(espacio, Calle) and espacio.es_peatonal else "Tráfico"
            print(f"\n[Espacio: {espacio.nombre} ({tipo})]")
            for edificio in espacio.edificios:
                edificio.describir_fachada()

# --- EJECUCIÓN DEL MODELO ---

if __name__ == "__main__":
    # 1. Crear la Ciudad
    toledo = Ciudad("Toledo")

    # 2. Crear Espacios (Calles/Plazas)
    calle_comercio = Calle("Calle Comercio", es_peatonal=True)
    plaza_zocodover = Plaza("Plaza de Zocodover", tiene_fuente=False)

    # 3. Composición: La ciudad se compone de estos espacios
    toledo.agregar_espacio(calle_comercio)
    toledo.agregar_espacio(plaza_zocodover)

    # 4. Crear un Edificio y sus Elementos (Composición interna)
    palacio = Edificio(10, "Renacentista")
    palacio.agregar_elemento(Portada("Piedra Caliza", "Excelente", "Plateresco"))
    palacio.agregar_elemento(Balcon("Hierro Forjado", "Bueno", tiene_reja=True))
    palacio.agregar_elemento(Ventana("Madera", "Regular", "Sencillo"))

    # 5. Agregación: Situar el edificio en la calle
    calle_comercio.registrar_edificio(palacio)

    # Generar informe
    toledo.informe_riqueza_arquitectonica()