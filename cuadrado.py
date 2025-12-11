class cuadrado:
    def __init__ (self, color, longitud):
        self.color = color
        self.longitud = longitud
    def __str__(self):
        return f"se ha creado un cuadrado con" + " {}".format(self.color) + " y de longitud " + "{}".format(self.longitud)