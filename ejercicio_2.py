class persona:
    def __init__ (self, nombre, apellido_nacimiento = None, apellido_actual = None):
        self.nombre = nombre
        self.apellido_nacimiento = apellido_nacimiento
        self.apellido_actual = apellido_actual
        self.pareja = None
        self.padres = []
    def casar_con(self, otra_persona):
        self.pareja = otra_persona
        otra_persona.pareja = self

    def agregar_padre(self, padre):
        self.padres.append(padre)
kate = persona(
    nombre="Kate",
    apellido_nacimiento="Middleton",
    apellido_actual="Windsor"
)

guillermo = persona(
    nombre="Guillermo",
    apellido_actual="Windsor"
)

carlos = persona(
    nombre="Carlos",
    apellido_actual="Windsor"
)

diana = persona(
    nombre="Diana",
    apellido_nacimiento="Spencer",
    apellido_actual="de Gales"
)

# Relaciones
guillermo.agregar_padre(carlos)
guillermo.agregar_padre(diana)

kate.casar_con(guillermo)
def imprimir_persona(p):
    print(f"Persona: {p.nombre}")
    print(f"  Apellido de nacimiento: {p.apellido_nacimiento}")
    print(f"  Apellido actual: {p.apellido_actual}")
    if p.pareja:
        print(f"  Pareja: {p.pareja.nombre}")
    if p.padres:
        print("  Padres:")
        for padre in p.padres:
            print(f"    - {padre.nombre}")
    print()


imprimir_persona(kate)
imprimir_persona(guillermo)
imprimir_persona(carlos)
imprimir_persona(diana)
