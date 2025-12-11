from typing import List

class Proyecto:
    def __init__(self, nombre: str, asignatura: str, tiempo_de_duracion: int):
        self.nombre = nombre
        self.asignatura = asignatura
        self.tiempo_de_duracion = tiempo_de_duracion
        self.compañeros = []        
        self.lugar = None           

    def agregar_compañero(self, nombre_compañero: str):
        """Permite añadir compañeros uno a uno"""
        self.compañeros.append(nombre_compañero)

    def establecer_lugar(self, lugar: str):
        """Establece dónde se realiza el proyecto"""
        self.lugar = lugar

    def __str__(self):
        compañeros_str = ", ".join(self.compañeros) if self.compañeros else "solo"
        lugar_str = self.lugar if self.lugar else "lugar no especificado"
        
        return (f"El nombre del proyecto es '{self.nombre}', "
                f"lo hacemos en la asignatura de {self.asignatura}, "
                f"ha durado {self.tiempo_de_duracion} horas, "
                f"con los compañeros: {compañeros_str}, "
                f"y lo hacemos en {lugar_str}.")



p = Proyecto("Catapulta mata rumanos", "Física", 2)

p.agregar_compañero("Pablo de Lucas")
p.agregar_compañero("María García")   

p.establecer_lugar("Facultad de Ciencias, CEU San Pablo Montepríncipe")

print(p)