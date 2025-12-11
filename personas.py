from ejercicio_2 import persona

if __name__ == "__personas__":
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
    print(kate)
    print(guillermo)
    print(carlos)
    print(diana)
