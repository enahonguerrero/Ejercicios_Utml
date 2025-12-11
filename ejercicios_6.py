# Una persona tiene un nombre, dos apellidos, una fecha de nacimiento, un sexo y un número de identificación.
# Define las clases y los atributos correspondientes.
class persona_2:
    def __init__(self, nombre, apellido_1, apellido_2, fecha_de_nacimiento, sexo, número_de_identificación):
        self.nombre = nombre
        self.apellido_1 = apellido_1
        self.apellido_2 = apellido_2
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.sexo = sexo
        self.número_de_identificación = número_de_identificación
    def __str__ (self):
        return "Me llammo {} {} {}".format(self.nombre, self.apellido_1, self.apellido_2) + " he nacido el {}".format(self.fecha_de_nacimiento) + " soy de género {}".format(self.sexo) + " y mi número de id es {}".format(self.número_de_identificación)
    
p2 = persona_2("Eduardo", "Nahon", "Guerrero", "16 de Mayo de 2007", "masculino", 51503707 )
print(p2)
         