from abc import ABC
from typing import List, Optional

# 1. Definición de las entidades base (Proyecto y Actuación)
class Actuacion:
    """Representa una actuación concreta dentro de un proyecto."""
    def __init__(self, descripcion: str):
        self.descripcion = descripcion

class Proyecto:
    """
    El Proyecto se compone de múltiples actuaciones.
    Relación de Composición (Todo/Parte).
    """
    def __init__(self, nombre: str):
        self.nombre = nombre
        # Un proyecto 'tiene' actuaciones
        self.actuaciones: List[Actuacion] = []

    def agregar_actuacion(self, actuacion: Actuacion):
        self.actuaciones.append(actuacion)

# 2. Definición de la estructura de Roles (Patrón Rol)
class Rol(ABC):
    """
    Clase abstracta base para cualquier rol.
    Permite polimorfismo si quisieramos añadir lógica común.
    """
    pass

class Responsable(Rol):
    """
    El rol de Responsable dirige proyectos.
    """
    def __init__(self):
        # Un responsable puede dirigir múltiples proyectos
        self.proyectos_dirigidos: List[Proyecto] = []

    def asignar_direccion(self, proyecto: Proyecto):
        self.proyectos_dirigidos.append(proyecto)

class Tecnico(Rol):
    """
    El rol de Técnico participa en proyectos y actuaciones.
    """
    def __init__(self):
        self.proyectos_participados: List[Proyecto] = []
        self.actuaciones_participadas: List[Actuacion] = []

    def asignar_a_proyecto(self, proyecto: Proyecto):
        self.proyectos_participados.append(proyecto)

    def asignar_a_actuacion(self, actuacion: Actuacion):
        self.actuaciones_participadas.append(actuacion)

# 3. La Persona (Contenedor de Roles)
class Persona:
    """
    La Persona puede tener múltiples roles simultáneamente.
    Relación de Agregación.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre
        # Aquí está la clave: Una lista de roles, no herencia simple
        self.roles: List[Rol] = []

    def agregar_rol(self, rol: Rol):
        self.roles.append(rol)

# --- Ejemplo de uso para verificar la estructura ---

if __name__ == "__main__":
    # Crear Proyectos y Actuaciones
    proy_excavacion = Proyecto("Excavación Romana")
    act_limpieza = Actuacion("Limpieza de superficie")
    act_catalogacion = Actuacion("Catalogación de hallazgos")
    
    # Composición: El proyecto es dueño de las actuaciones
    proy_excavacion.agregar_actuacion(act_limpieza)
    proy_excavacion.agregar_actuacion(act_catalogacion)

    # Crear una Persona
    laura = Persona("Laura Garcia")

    # Laura es Responsable de este proyecto
    rol_manager = Responsable()
    rol_manager.asignar_direccion(proy_excavacion)
    laura.agregar_rol(rol_manager)

    # Laura TAMBIÉN es Técnico en una actuación concreta (multirole)
    rol_tech = Tecnico()
    rol_tech.asignar_a_actuacion(act_limpieza)
    laura.agregar_rol(rol_tech)

    print(f"{laura.nombre} tiene {len(laura.roles)} roles activos.")