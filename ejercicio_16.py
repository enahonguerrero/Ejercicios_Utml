from typing import List, Optional

class Persona:
    """
    Clase que representa a una persona e implementa las asociaciones 
    recursivas para modelar relaciones familiares.
    """
    def __init__(self, nombre: str, apellido_1: str, apellido_2: str, 
                 fecha_de_nacimiento: str, sexo: str, numero_de_identificacion: int):
        
        # Atributos básicos de la persona
        self.nombre = nombre
        self.apellido_1 = apellido_1
        self.apellido_2 = apellido_2
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.sexo = sexo
        self.numero_de_identificacion = numero_de_identificacion
        
        # Atributos para modelar Asociaciones (Roles y Cardinalidades)
        # 0..1 (Pareja): Se usa None o una sola referencia
        self.pareja: Optional['Persona'] = None 
        
        # 0..* / 1..* (Hijos y Progenitores): Se usan listas
        self.hijos: List['Persona'] = []       # Role: progenitor -> 0..*
        self.progenitores: List['Persona'] = [] # Role: hijo_a -> 1..* (se asume que se completará)
        self.hermanos: List['Persona'] = []    # Role: hermano_a -> 0..*
        
    def __str__(self) -> str:
        """Representación legible del objeto."""
        return (f"ID {self.numero_de_identificacion}: {self.nombre} {self.apellido_1} {self.apellido_2} "
                f"({self.fecha_de_nacimiento}, {self.sexo}).")

    # --- MÉTODOS PARA GESTIONAR ASOCIACIONES (ROLES) ---

    def establecer_pareja(self, otra_persona: 'Persona'):
        """Establece la relación de Pareja (0..1). Implementación bidireccional."""
        if self.pareja is not None and self.pareja != otra_persona:
            # Opción estricta: si ya tiene pareja, no puede tener otra (cumple 0..1)
            print(f"[{self.nombre}]: ¡Error! Ya tiene pareja ({self.pareja.nombre}).")
            return

        # Establecer el enlace en ambas direcciones
        self.pareja = otra_persona
        if otra_persona.pareja != self:
            otra_persona.establecer_pareja(self)
        print(f"[{self.nombre} y {otra_persona.nombre}] ahora son pareja.")

    def add_hijo(self, hijo_obj: 'Persona'):
        """Añade un hijo/a a la lista (0..*). Implementación bidireccional."""
        if hijo_obj not in self.hijos:
            self.hijos.append(hijo_obj)
            print(f"[{self.nombre}]: Añadido {hijo_obj.nombre} a la lista de hijos.")
            
        # Establecer el enlace en la dirección opuesta (Filiación)
        if self not in hijo_obj.progenitores:
            hijo_obj.progenitores.append(self)
            
    def add_hermano(self, hermano_obj: 'Persona'):
        """Añade un hermano/a a la lista (0..*). Implementación bidireccional simple."""
        if hermano_obj not in self.hermanos:
            self.hermanos.append(hermano_obj)
        
        # Establecer el enlace en la dirección opuesta
        if self not in hermano_obj.hermanos:
            hermano_obj.hermanos.append(self)


# --- EJEMPLO DE USO Y MODELADO FAMILIAR ---

# 1. Crear las instancias de Persona
p_padre = Persona("Luis", "Garcia", "Sanz", "1970/01/15", "M", 12345678)
p_madre = Persona("Ana", "Perez", "Vela", "1972/06/20", "F", 87654321)
p_hijo1 = Persona("Carlos", "Garcia", "Perez", "2000/03/10", "M", 90123456)
p_hijo2 = Persona("Marta", "Garcia", "Perez", "2005/11/25", "F", 65432109)

print("--- INSTANCIAS ---")
print(p_padre)
print(p_hijo1)
print("-" * 20)

# 2. Modelar la relación de PAREJA (Asociación 0..1)
p_padre.establecer_pareja(p_madre)
print(f"¿Son pareja? -> {p_madre.pareja.nombre} y {p_padre.pareja.nombre}")
print("-" * 20)

# 3. Modelar la relación de PATERNIDAD/FILIACIÓN (Asociación 0..* a 1..*)
p_padre.add_hijo(p_hijo1)
p_madre.add_hijo(p_hijo1)
p_padre.add_hijo(p_hijo2)
p_madre.add_hijo(p_hijo2)
print("-" * 20)

# 4. Modelar la relación de HERMANOS (Asociación 0..*)
p_hijo1.add_hermano(p_hijo2)
print(f"¿Hijos de Luis? -> {[h.nombre for h in p_padre.hijos]}")
print(f"¿Progenitores de Carlos? -> {[p.nombre for p in p_hijo1.progenitores]}")
print(f"¿Hermanos de Carlos? -> {[h.nombre for h in p_hijo1.hermanos]}")
print(f"¿Hermanos de Marta? -> {[h.nombre for h in p_hijo2.hermanos]}")