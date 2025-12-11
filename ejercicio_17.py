from datetime import date, timedelta
from typing import List, Optional, Dict

# --- CLASES DE ORGANIZACIÓN FÍSICA ---

class Estanteria:
    """Modela una estantería en una planta, con capacidad límite."""
    def __init__(self, identificador: str, capacidad_maxima: int):
        self.identificador = identificador
        self.capacidad_maxima = capacidad_maxima
        self.ejemplares_albergados: List['Ejemplar'] = []

    def __str__(self):
        return f"Estantería {self.identificador} (Capacidad: {len(self.ejemplares_albergados)}/{self.capacidad_maxima})"

class Planta:
    """Modela una planta de la biblioteca."""
    def __init__(self, numero: int):
        self.numero = numero
        self.estanterias: Dict[str, Estanteria] = {}

    def add_estanteria(self, estanteria: Estanteria):
        self.estanterias[estanteria.identificador] = estanteria

    def get_capacidad_total(self) -> int:
        return sum(est.capacidad_maxima for est in self.estanterias.values())

# --- CLASES DE INVENTARIO ---

class Libro:
    """Representa el título genérico (la obra)."""
    def __init__(self, ISBN: str, titulo: str, autor: str, tema: str):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.tema = tema
        self.ejemplares: List[Ejemplar] = []

    def __str__(self):
        return f"Libro: '{self.titulo}' de {self.autor} (ISBN: {self.ISBN})"

class Ejemplar:
    """Representa una copia física específica del libro."""
    def __init__(self, id_unico: int, libro_maestro: Libro):
        self.id_unico = id_unico
        self.libro_maestro = libro_maestro
        self.esta_prestado = False
        
        # Asocia el ejemplar a su libro maestro (Relación 1 a 1..*)
        libro_maestro.ejemplares.append(self)

    def __str__(self):
        return f"Ejemplar #{self.id_unico} de '{self.libro_maestro.titulo}'"

# --- CLASES DE USUARIO (HERENCIA) ---

class Lector:
    """Clase base para todos los usuarios."""
    def __init__(self, num_identificacion: int, nombre: str, direccion_postal: str):
        self.num_identificacion = num_identificacion
        self.nombre = nombre
        self.direccion_postal = direccion_postal
        self.penalizado = False
        self.dias_prestamo_maximo = 30 # Regla general
    
    def __str__(self):
        return f"Lector: {self.nombre} (ID: {self.num_identificacion})"

class UsuarioConvencional(Lector):
    """Lector estándar con plazo máximo de 30 días."""
    def __init__(self, num_identificacion: int, nombre: str, direccion_postal: str):
        super().__init__(num_identificacion, nombre, direccion_postal)
        self.tipo = "Convencional"
        
class Empleado(Lector):
    """Lector con privilegio de plazo mayor."""
    def __init__(self, num_identificacion: int, nombre: str, direccion_postal: str, id_empleado: int):
        super().__init__(num_identificacion, nombre, direccion_postal)
        self.id_empleado = id_empleado
        self.tipo = "Empleado"
        self.dias_prestamo_maximo = 45 # Plazo mayor para empleados

# --- CLASES DE TRANSACCIÓN ---

class Prestamo:
    """Modela la transacción de préstamo (Asociación con Lector y Ejemplar)."""
    def __init__(self, lector: Lector, ejemplar: Ejemplar):
        self.lector = lector
        self.ejemplar = ejemplar
        self.fecha_prestamo = date.today()
        
        # Calcula la fecha límite basada en el tipo de Lector
        self.fecha_entrega_limite = self.fecha_prestamo + timedelta(days=lector.dias_prestamo_maximo)
        
        self.fecha_entrega_real: Optional[date] = None
        self.penalizacion: Optional[Penalizacion] = None
        
        # Actualiza el estado del ejemplar
        ejemplar.esta_prestado = True

    def registrar_devolucion(self, fecha_devolucion: date):
        """Registra la devolución"""