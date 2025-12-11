from abc import ABC

class Forma(ABC):
    def __init__(self, color):
        self.color = color
    
    def describir(self):
        return f"Soy una forma de color {self.color}"

class Cuadrilatero(Forma):
    def __init__(self, color, longitud):
        super().__init__(color)
        self.longitud = longitud

class Conica(Forma):
    def __init__(self, color):
        super().__init__(color)

class Rectangulo(Cuadrilatero):
    def __init__(self, color, longitud, anchura):
        super().__init__(color, longitud)
        self.anchura = anchura
        
    def describir(self):
        return f"Rectángulo {self.color} (Alto: {self.longitud}, Ancho: {self.anchura})"

class Cuadrado(Cuadrilatero):
    def __init__(self, color, lado):
        super().__init__(color, lado)

    def describir(self):
        return f"Cuadrado {self.color} (Lado: {self.longitud})"

class Circulo(Conica):
    def __init__(self, color, diametro):
        super().__init__(color)
        self.diametro = diametro

    def describir(self):
        return f"Círculo {self.color} (Diámetro: {self.diametro})"

class Elipse(Conica):
    def __init__(self, color, eje_mayor, eje_menor):
        super().__init__(color)
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

    def describir(self):
        return f"Elipse {self.color} (Eje Mayor: {self.eje_mayor}, Eje Menor: {self.eje_menor})"

if __name__ == "__main__":
    figura_azul = Cuadrado(color="Azul", lado=10.5)
    figura_naranja = Rectangulo(color="Naranja", longitud=5.0, anchura=8.0)
    figura_gris = Circulo(color="Gris", diametro=4.2)
    figura_amarilla = Elipse(color="Amarillo", eje_mayor=10, eje_menor=5)

    print(figura_azul.describir())
    print(figura_naranja.describir())
    print(figura_gris.describir())
    print(figura_amarilla.describir())