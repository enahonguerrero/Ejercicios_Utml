# Describe las características de los proyectos en los que habitualmente participas, según tu experiencia y
# profesión, utilizando tantas clases como sea necesario. Para facilitar la comprensión de tu modelo, incluye la
# definición textual de las clases.

class proyecto:
    def __init__ (self, nombre, asignatura, tiempo_de_duración):
        self.nombre = nombre
        self.asignatura = asignatura
        self.tiempo_de_duración = tiempo_de_duración
    def __str__ (self):
        return "El nombre del proyecto es {}, lo hacemos en {} y ha durado {} horas".format(self.nombre, self.asignatura, self.tiempo_de_duración)
class compañero:
    def __init__ (self, compañero):
        self.compañero = compañero
    def __str__ (self):
        return "Lo he hecho con mi compañero {}".format(self.compañero) 
class lugar:
    def __init__ (self, lugar):
        self.lugar = lugar
    def __str__ (self):
        return "Y lo hacemos en {}".format(self.lugar)
p = proyecto("Catapulta mata rumanos", "Fisica", 2)
c = compañero("Pablo de lucas")
l = lugar("Facultad de ciencias Ceu San Pablo Monteprincipe")
print(p,"\n", c, "\n", l)