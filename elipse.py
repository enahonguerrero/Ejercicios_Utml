class elipse:
    def __init__ (self, color, eje_menor, eje_mayor):
        self.color = color
        self.eje_menor = eje_menor
        self.eje_mayor = eje_mayor
    def __str__ (self):
        return f"se ha creado una elipse de color " + "{}".format(self.color) + " cuyo eje menor es de " + "{}".format(self.eje_menor) + " metros " + "y su eje mayor consta de " + "{}".format(self.eje_mayor) + " metros."
    
    