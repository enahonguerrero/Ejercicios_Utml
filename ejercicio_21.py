from typing import List
import math

# 1. Clase Base (Generalización)
class EntidadGeografica:
    """
    Clase padre que contiene los atributos comunes.
    """
    def __init__(self, nombre: str, codigo: str):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"[{self.codigo}] {self.nombre}"

# 2. Clases Específicas

class Punto(EntidadGeografica):
    """
    Un punto se define por sus coordenadas X e Y.
    """
    def __init__(self, nombre: str, codigo: str, x: float, y: float):
        super().__init__(nombre, codigo)
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Linea(EntidadGeografica):
    """
    Una línea se define por una secuencia de puntos.
    Debe tener al menos 2 puntos.
    """
    def __init__(self, nombre: str, codigo: str, puntos: List[Punto]):
        # Validación de la regla de negocio
        if len(puntos) < 2:
            raise ValueError("Una línea debe estar definida por al menos 2 puntos.")
        
        super().__init__(nombre, codigo)
        self.puntos = puntos

class Area(EntidadGeografica):
    """
    Un área (polígono) se define por una secuencia de puntos.
    Debe tener al menos 3 puntos.
    """
    def __init__(self, nombre: str, codigo: str, puntos: List[Punto]):
        # Validación de la regla de negocio
        if len(puntos) < 3:
            raise ValueError("Un área debe estar definida por al menos 3 puntos.")
        
        super().__init__(nombre, codigo)
        self.puntos = puntos

# --- Ejemplo de uso ---

if __name__ == "__main__":
    try:
        # 1. Crear Puntos (Entidades básicas)
        p1 = Punto("Origen", "P001", 0, 0)
        p2 = Punto("Intermedio", "P002", 10, 10)
        p3 = Punto("Final", "P003", 20, 0)

        print(f"Punto creado: {p1} en {p1.x}, {p1.y}")

        # 2. Crear una Línea (Validación: necesita >= 2 puntos)
        # Usamos los objetos Punto creados anteriormente (Agregación)
        ruta = Linea("Ruta Senderismo", "L001", [p1, p2])
        print(f"Línea creada: {ruta} con {len(ruta.puntos)} puntos.")

        # 3. Crear un Área (Validación: necesita >= 3 puntos)
        zona = Area("Zona de Cultivo", "A001", [p1, p2, p3])
        print(f"Área creada: {zona} con {len(zona.puntos)} puntos.")

        # 4. Intentar romper la regla (Esto lanzará un error)
        linea_invalida = Linea("Linea Error", "ERR", [p1]) 

    except ValueError as e:
        print(f"Error de validación: {e}")