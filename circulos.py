class circulo:
    def __init__ (self, color, diametro):
        self.color = color
        self.diametro = diametro
    def __str__ (self):
        return f"Se ha creado un circulo de color " +  "{} ".format(self.color) + "y con diametro" + " {}".format(self.diametro) 
    

