from enum import Enum
from typing import List

class Tecnica(Enum):
    OLEO = "Óleo sobre panel"

class EstadoConservacion(Enum):
    BUENO = "Buen estado con restauraciones menores"
    EXCELENTE = "Excelente, casi intacto"
    DELICADO = "Delicado, con deformaciones y oscurecimiento"

class PinturaRenacentista:
    def __init__(self, nombre: str, representado: str, pintor: str, lugar_pintado: str,
                 copias: List[str], tecnica: Tecnica, material_soporte: str,
                 ubicacion_actual: str, conservacion: EstadoConservacion):
        self.nombre = nombre
        self.representado = representado
        self.pintor = pintor
        self.lugar_pintado = lugar_pintado
        self.copias = copias 
        self.tecnica = tecnica
        self.material_soporte = material_soporte
        self.ubicacion_actual = ubicacion_actual
        self.conservacion = conservacion
    
    def descripcion(self) -> str:
        return f"{self.nombre}: Retrato de {self.representado} por {self.pintor}, pintado en {self.lugar_pintado}. Técnica: {self.tecnica.value}. Soporte: {self.material_soporte}. Ubicación actual: {self.ubicacion_actual}. Conservación: {self.conservacion.value}."

# Instancia de la clase para La Mona Lisa
mona_lisa = PinturaRenacentista(
    nombre="La Mona Lisa",
    representado="Lisa Gherardini",
    pintor="Leonardo da Vinci",
    lugar_pintado="Florencia, Italia (1503-1519)",
    copias=[
        "Copia del Museo del Prado (Madrid, ~1503-1516)",
        "Isleworth Mona Lisa (versión temprana)",
        "Versión del Louvre (Bacchus, siglo XVI)"
    ],
    tecnica=Tecnica.OLEO,
    material_soporte="Panel de madera de álamo",
    ubicacion_actual="Museo del Louvre, París, Francia",
    conservacion=EstadoConservacion.DELICADO
)

print(mona_lisa.descripcion())