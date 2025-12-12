from typing import List, Literal

class Hoja:
    """Representa la unidad básica 'hoja' mencionada en la definición."""
    def __init__(self, contenido: str):
        # Invariante: La definición especifica "hojas de papel".
        # No es una variable, es una constante del concepto definido.
        self.material = "papel" 
        self.contenido = contenido

class Libro:
    """
    Definición: Conjunto de hojas de papel manuscritas o impresas que,
    cosidas o encuadernadas, forman un volumen.
    """
    def __init__(
        self, 
        hojas: List[Hoja], 
        tipo_escritura: Literal['manuscrita', 'impresa'],
        tipo_union: Literal['cosida', 'encuadernada']
    ):
        # 1. Validación de Invariantes de Material
        for h in hojas:
            if h.material != "papel":
                raise ValueError("Un libro debe estar compuesto por hojas de papel.")
        
        # 2. Validación de Invariantes de Estructura (Formar un volumen)
        if not hojas:
            raise ValueError("El conjunto de hojas no puede estar vacío para formar un volumen.")

        # Asignación de Variables
        self._hojas = hojas  # El "Conjunto"
        self.tipo_escritura = tipo_escritura
        self.tipo_union = tipo_union
        
        # Estado implícito: Al crearse con unión válida, 'forman un volumen' es True.
        self.es_volumen = True 

    def __repr__(self):
        return (f"Libro({len(self._hojas)} hojas de {self._hojas[0].material}, "
                f"{self.tipo_escritura}, {self.tipo_union})")

# Ejemplo de uso
hojas_papel = [Hoja("Texto 1"), Hoja("Texto 2")]
mi_libro = Libro(hojas_papel, "impresa", "encuadernada")
print(mi_libro)