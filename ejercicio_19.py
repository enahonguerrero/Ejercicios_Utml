from enum import Enum, auto
from datetime import datetime, date
from abc import ABC

class Lugar(Enum):
    MADRID = auto()
    BARCELONA = auto()
    SEVILLA = auto()
    VALENCIA = auto()

class Estado(Enum):
    BUENO = auto()
    REGULAR = auto()
    MALO = auto()
    EN_RESTAURACION = auto()

class Tematica(Enum):
    ARTE = auto()
    HISTORIA = auto()
    CIENCIA = auto()

class TecnicaRestauracion(Enum):
    LIMPIEZA = auto()
    CONSOLIDACION = auto()
    REINTEGRACION = auto()

class Ubicacion(ABC):
    def __init__(self, codigo):
        self.codigo = codigo

class Almacen(Ubicacion):
    def __init__(self, codigo, nombre):
        super().__init__(codigo)
        self.nombre = nombre

class Sala(Ubicacion):
    def __init__(self, codigo, nombre, abierta_al_publico):
        super().__init__(codigo)
        self.nombre = nombre
        self.abierta_al_publico = abierta_al_publico

class Planta:
    def __init__(self, numero):
        self.numero = numero
        self.salas = []

    def agregar_sala(self, sala):
        self.salas.append(sala)

class Edificio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.plantas = []

    def agregar_planta(self, planta):
        self.plantas.append(planta)

class Coleccion:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetos = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

class ColeccionTemporal(Coleccion):
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin):
        super().__init__(nombre, descripcion)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class Objeto:
    def __init__(self, codigo, nombre, autor, fecha_creacion, descripcion, origen, estado, tematica, ubicacion):
        self.codigo = codigo
        self.nombre = nombre
        self.autor = autor
        self.fecha_creacion = fecha_creacion
        self.descripcion = descripcion
        self.origen = origen
        self.estado = estado
        self.tematica = tematica
        self.ubicacion = ubicacion
        self.coleccion = None

    def asignar_coleccion(self, coleccion):
        self.coleccion = coleccion
        coleccion.agregar_objeto(self)

class Restauracion:
    def __init__(self, fecha, descripcion, tecnica, objetos):
        self.fecha = fecha
        self.descripcion = descripcion
        self.tecnica = tecnica
        self.objetos = objetos

if __name__ == "__main__":
    edificio_central = Edificio("Museo del Prado", "Paseo del Prado")
    planta_baja = Planta(0)
    edificio_central.agregar_planta(planta_baja)

    sala_goya = Sala("S01", "Sala Goya", True)
    planta_baja.agregar_sala(sala_goya)
    
    almacen_norte = Almacen("A01", "Almacén Norte")

    coleccion_real = Coleccion("Colección Real", "Obras de los reyes")
    coleccion_verano = ColeccionTemporal("Verano 2024", "Exposición temporal", date(2024, 6, 1), date(2024, 9, 30))

    cuadro = Objeto(
        codigo="OBJ-001",
        nombre="Las Meninas",
        autor="Velázquez",
        fecha_creacion=date(1656, 1, 1),
        descripcion="Obra maestra del barroco",
        origen=Lugar.MADRID,
        estado=Estado.BUENO,
        tematica=Tematica.ARTE,
        ubicacion=sala_goya
    )
    cuadro.asignar_coleccion(coleccion_real)

    jarron = Objeto(
        codigo="OBJ-002",
        nombre="Jarrón Ming",
        autor="Desconocido",
        fecha_creacion=date(1400, 1, 1),
        descripcion="Porcelana antigua",
        origen=Lugar.VALENCIA,
        estado=Estado.EN_RESTAURACION,
        tematica=Tematica.HISTORIA,
        ubicacion=almacen_norte
    )

    restauracion_jarron = Restauracion(
        fecha=date(2023, 10, 15),
        descripcion="Reparación de grieta en la base",
        tecnica=TecnicaRestauracion.CONSOLIDACION,
        objetos=[jarron]
    )

    print(f"Objeto: {cuadro.nombre}, Ubicación: {cuadro.ubicacion.nombre}")
    print(f"Objeto en restauración: {restauracion_jarron.objetos[0].nombre}, Técnica: {restauracion_jarron.tecnica.name}")