class rectangulo:
    def __init__ (self, color, longitud, anchura):
        self.color = color
        self.longitud = longitud
        self.anchura = anchura
    def __str__ (self):
        return f"Se ha creado un rectangulo de color " + "{}".format(self.color) + " una longitud de " + "{}".format(self.longitud) + " y una anchura de " + "{}".format(self.anchura)

