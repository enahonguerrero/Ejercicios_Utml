from abc import ABC, abstractmethod
from typing import List, Optional

# --- BLOQUE DE SUBJETIVIDAD (Interpretaciones) ---

class Datacion:
    """Representa una opinión sobre la antigüedad."""
    def __init__(self, periodo: str, autor: str):
        self.periodo = periodo
        self.autor = autor # Quién opina esto

    def __repr__(self):
        return f"Datación: {self.periodo} (según {self.autor})"

class UsoProbable:
    """Representa una hipótesis sobre para qué servía el objeto."""
    def __init__(self, funcion: str):
        self.funcion = funcion

    def __repr__(self):
        return f"Uso posible: {self.funcion}"

class Similitud:
    """
    Clase que vincula dos objetos basada en una opinión subjetiva.
    """
    def __init__(self, objeto_a, objeto_b, motivo: str):
        self.objeto_a = objeto_a
        self.objeto_b = objeto_b
        self.motivo = motivo

    def __repr__(self):
        return f"Similitud observada entre {self.objeto_a.codigo} y {self.objeto_b.codigo}: {self.motivo}"

# --- ESTRUCTURA FÍSICA Y CONTEXTO ---

class SitioArqueologico:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Excavacion:
    def __init__(self, nombre: str, sitio: SitioArqueologico):
        self.nombre = nombre
        self.sitio = sitio
        self.objetos_encontrados: List['ObjetoArqueologico'] = []

    def registrar_hallazgo(self, objeto):
        self.objetos_encontrados.append(objeto)

# --- JERARQUÍA DE OBJETOS ---

class ObjetoArqueologico(ABC):
    """
    Clase base con los atributos FÍSICOS (Objetivos).
    """
    def __init__(self, codigo: str, material: str, dimensiones: str, descripcion: str):
        # Datos Objetivos (Hechos)
        self.codigo = codigo
        self.material = material
        self.dimensiones = dimensiones
        self.descripcion = descripcion
        
        # Datos Subjetivos (Interpretaciones agregadas)
        self.dataciones: List[Datacion] = []
        self.similitudes: List[Similitud] = []

    def agregar_datacion(self, datacion: Datacion):
        self.dataciones.append(datacion)

    def registrar_similitud(self, otro_objeto, motivo: str):
        # Creamos el vínculo de similitud
        sim = Similitud(self, otro_objeto, motivo)
        self.similitudes.append(sim)
        # Opcional: registrarlo también en el otro objeto bidireccionalmente
        otro_objeto.similitudes.append(sim)

    def __str__(self):
        return f"[{self.codigo}] {self.material}"

class Fragmento(ObjetoArqueologico):
    pass

class ObjetoCompleto(ObjetoArqueologico):
    def __init__(self, codigo: str, material: str, dimensiones: str, descripcion: str):
        super().__init__(codigo, material, dimensiones, descripcion)
        self.usos_probables: List[UsoProbable] = []
        # Patrón Composite: Un objeto completo puede tener partes
        self.partes: List[ObjetoArqueologico] = []

    def agregar_uso(self, uso: UsoProbable):
        self.usos_probables.append(uso)

    def agregar_parte(self, parte: ObjetoArqueologico):
        self.partes.append(parte)

    def mostrar_ficha_completa(self):
        print(f"FICHA OBJETO: {self.codigo} ({self.material})")
        print(f"  - Descripción: {self.descripcion}")
        
        print("  - Partes componentes:")
        for parte in self.partes:
            print(f"    * {parte.codigo} ({type(parte).__name__})")
            
        print("  - Interpretaciones (Subjetivas):")
        for d in self.dataciones: print(f"    * {d}")
        for u in self.usos_probables: print(f"    * {u}")
        for s in self.similitudes: 
            other = s.objeto_b if s.objeto_a == self else s.objeto_a
            print(f"    * Similar a {other.codigo}: {s.motivo}")

# --- EJECUCIÓN ---

if __name__ == "__main__":
    # Contexto
    sitio = SitioArqueologico("Pompeya")
    excavacion = Excavacion("Campaña 2024", sitio)

    # 1. Hallazgo de fragmentos (Hechos físicos)
    frag_asa = Fragmento("F-001", "Cerámica", "10cm", "Asa de vasija")
    frag_cuerpo = Fragmento("F-002", "Cerámica", "30cm", "Cuerpo curvado")

    # 2. Reconstrucción de un objeto completo (Composite)
    anfora = ObjetoCompleto("OBJ-100", "Cerámica", "100cm", "Ánfora reconstruida")
    anfora.agregar_parte(frag_asa)
    anfora.agregar_parte(frag_cuerpo)

    # 3. Añadiendo Subjetividad (Interpretaciones)
    
    # Datación (Puede haber conflicto de opiniones)
    anfora.agregar_datacion(Datacion("Siglo I d.C.", "Dr. Jones"))
    anfora.agregar_datacion(Datacion("Finales s. I a.C.", "Dra. Croft"))
    
    # Uso (Solo para completos)
    anfora.agregar_uso(UsoProbable("Transporte de aceite"))
    
    # Similitud (Comparación con otro objeto)
    otro_objeto = ObjetoCompleto("OBJ-999", "Cerámica", "90cm", "Ánfora Museo")
    anfora.registrar_similitud(otro_objeto, "Mismo sello de alfarero")

    # Resultado
    anfora.mostrar_ficha_completa()