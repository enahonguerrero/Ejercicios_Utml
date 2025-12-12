from abc import ABC, abstractmethod
from typing import List, Literal

# --- COMPONENTES ---

class Ventana:
    """
    Representa las ventanas descritas.
    Variables: material de cierre (tela/vidrio), color.
    Invariantes comunes: arco doble, altas>anchas.
    """
    def __init__(self, material_cierre: str, es_vidriera: bool, tiene_color: bool = False):
        self.proporcion = "Más alta que ancha"
        self.tipo_arco = "Doble"
        self.decoracion_exterior = False # Texto: "sin decorar exteriormente" (aplica a las rurales, extendido por defecto)
        
        # Variables dependientes del tipo de iglesia
        self.material_cierre = material_cierre # "Tela encerada", "Vidrio"
        self.es_vidriera = es_vidriera
        self.tiene_color = tiene_color

    def __repr__(self):
        tipo = "Vidriera" if self.es_vidriera else "Tela"
        color = "Coloreada" if self.tiene_color else "Incolora/Blanca"
        return f"[Ventana: {self.proporcion}, {tipo} ({color})]"

class Abside:
    """
    La cabecera de la iglesia.
    Invariante: Forma semicircular.
    """
    def __init__(self, disposicion: str = "Lineal"):
        self.forma = "Semicircular"
        self.disposicion = disposicion # "Frente" o "Corona"
        self.ventanas: List[Ventana] = []

    def instalar_ventanas(self, lista_ventanas: List[Ventana]):
        self.ventanas = lista_ventanas

class Nave:
    """Cuerpo de la iglesia."""
    pass

# --- CLASE BASE ---

class IglesiaRomanica(ABC):
    def __init__(self):
        # Invariante del texto: "siempre mira a oriente"
        self.orientacion_cabecera = "Oriente"
        self.naves: List[Nave] = []
        self.absides: List[Abside] = []

# --- CLASES ESPECÍFICAS ---

class IglesiaRural(IglesiaRomanica):
    """
    Definición: Iglesia menor. Sencilla nave, ábside sin crucero saliente.
    Ventanas cerradas con telas.
    """
    def __init__(self, impregnacion_tela: Literal['cera', 'trementina']):
        super().__init__()
        # Invariante: Sin crucero saliente
        self.tiene_crucero_saliente = False
        
        # Invariante: Una sola nave
        self.naves.append(Nave())
        
        # Invariante: Un solo ábside
        abside_unico = Abside()
        
        # Configuración de ventanas para Rural (Pocas, tela blanca)
        # El texto dice "Las pocas ventanas... cerradas con telas"
        ventana_rural = Ventana(
            material_cierre=f"Tela con {impregnacion_tela}",
            es_vidriera=False,
            tiene_color=False # "Telas blancas"
        )
        abside_unico.instalar_ventanas([ventana_rural]) # Simplificación: 1 o pocas
        self.absides.append(abside_unico)

    def __repr__(self):
        return (f"Iglesia Rural (Naves: {len(self.naves)}, "
                f"Ventana: {self.absides[0].ventanas[0].material_cierre})")

class IglesiaMayor(IglesiaRomanica):
    """
    Definición: Monasterios/Santuarios. Planta basilical. 3 o 5 naves.
    Crucero saliente. 3 o 5 ábsides. Ventanas con vidrieras.
    """
    def __init__(self, num_naves: int, es_suntuosa: bool):
        super().__init__()
        
        # Validación de Invariantes del texto: "tres o cinco naves/ábsides"
        if num_naves not in [3, 5]:
            raise ValueError("Las iglesias mayores deben tener 3 o 5 naves.")
            
        self.tipo_planta = "Basilical Latina"
        self.tiene_crucero_saliente = True
        
        # Construcción de Naves
        for _ in range(num_naves):
            self.naves.append(Nave())
            
        # Construcción de Ábsides (misma cantidad que naves según simetría habitual, o 3-5)
        # El texto dice "tres o cinco ábsides"
        num_absides = num_naves 
        
        for _ in range(num_absides):
            abside = Abside(disposicion="Frente o Corona")