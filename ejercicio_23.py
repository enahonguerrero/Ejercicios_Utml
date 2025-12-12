from abc import ABC, abstractmethod
from typing import List

# --- 1. COMPONENT (La Interfaz Común) ---
class ElementoConstructivo(ABC):
    """
    Define la interfaz común para objetos simples y complejos.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def calcular_superficie(self) -> float:
        pass

    @abstractmethod
    def mostrar_detalle(self, nivel=0):
        pass

# --- 2. LEAF (La Hoja - El Edificio Individual) ---
class Edificio(ElementoConstructivo):
    """
    Representa un objeto indivisible. Realiza el trabajo real.
    """
    def __init__(self, nombre: str, superficie: float):
        super().__init__(nombre)
        self.superficie = superficie

    def calcular_superficie(self) -> float:
        return self.superficie

    def mostrar_detalle(self, nivel=0):
        indent = "  " * nivel
        print(f"{indent}- Edificio: {self.nombre} ({self.superficie} m2)")

# --- 3. COMPOSITE (El Contenedor - Conjunto Construido) ---
class ConjuntoConstruido(ElementoConstructivo):
    """
    Almacena componentes hijos (Edificios u otros Conjuntos).
    Delega las operaciones a sus hijos.
    """
    def __init__(self, nombre: str):
        super().__init__(nombre)
        # Aquí está la magia: Una lista de 'ElementoConstructivo', no solo de Edificios.
        self._hijos: List[ElementoConstructivo] = []

    def agregar(self, elemento: ElementoConstructivo):
        self._hijos.append(elemento)

    def eliminar(self, elemento: ElementoConstructivo):
        self._hijos.remove(elemento)

    def calcular_superficie(self) -> float:
        """
        Itera sobre sus hijos y suma sus resultados, sin importar si son
        edificios simples o sub-conjuntos complejos.
        """
        total = 0.0
        for hijo in self._hijos:
            total += hijo.calcular_superficie()
        return total

    def mostrar_detalle(self, nivel=0):
        indent = "  " * nivel
        print(f"{indent}+ Conjunto: {self.nombre}")
        for hijo in self._hijos:
            hijo.mostrar_detalle(nivel + 1)

# --- EJEMPLO DE USO ---

if __name__ == "__main__":
    # 1. Crear Hojas (Edificios simples)
    ed_biblioteca = Edificio("Biblioteca Central", 1200)
    ed_aulas = Edificio("Aulario Norte", 800)
    ed_gimnasio = Edificio("Gimnasio", 1500)
    ed_cafeteria = Edificio("Cafetería", 300)

    # 2. Crear un Composite (Sub-conjunto: Zona Deportiva)
    zona_deportiva = ConjuntoConstruido("Zona Deportiva")
    zona_deportiva.agregar(ed_gimnasio)
    zona_deportiva.agregar(ed_cafeteria) 
    # (Imagina que la cafetería está dentro del complejo deportivo)

    # 3. Crear el Composite Principal (Campus Universitario)
    campus = ConjuntoConstruido("Campus Universitario")
    
    # Agregamos edificios sueltos
    campus.agregar(ed_biblioteca)
    campus.agregar(ed_aulas)
    
    # Agregamos el otro conjunto complejo (Nidación)
    campus.agregar(zona_deportiva)

    #