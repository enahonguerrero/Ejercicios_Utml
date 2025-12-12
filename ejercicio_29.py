from datetime import date, datetime
from typing import List, Optional

# --- CLASE AUXILIAR PARA GESTIÓN DE TIEMPO ---

class ElementoTemporal:
    """Clase base para cualquier dato que tenga validez en un periodo."""
    def __init__(self, fecha_inicio: date, fecha_fin: Optional[date] = None):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin  # None significa "actualmente" o "hasta siempre"

    def es_valido_en(self, fecha_consultada: date) -> bool:
        if self.fecha_fin:
            return self.fecha_inicio <= fecha_consultada <= self.fecha_fin
        return self.fecha_inicio <= fecha_consultada

# --- ENTIDADES BÁSICAS ---

class Lugar:
    def __init__(self, nombre: str, pais: str):
        self.nombre = nombre
        self.pais = pais

class Ocupacion:
    def __init__(self, nombre: str):
        self.nombre = nombre

# --- CLASES DE ASOCIACIÓN TEMPORAL ---

class IdentidadTemporal(ElementoTemporal):
    """
    Representa el nombre y título de una persona en un periodo concreto.
    Ej: De 1990 a 2000 fue "Príncipe Felipe", de 2014 en adelante "Rey Felipe VI".
    """
    def __init__(self, nombre: str, apellidos: str, titulo: str, fecha_inicio: date, fecha_fin: date = None):
        super().__init__(fecha_inicio, fecha_fin)
        self.nombre = nombre
        self.apellidos = apellidos
        self.titulo = titulo

    def __repr__(self):
        return f"{self.titulo} {self.nombre} {self.apellidos}"

class DesempenoLaboral(ElementoTemporal):
    """Vincula Persona con Ocupación en un tiempo dado."""
    def __init__(self, ocupacion: Ocupacion, fecha_inicio: date, fecha_fin: date = None):
        super().__init__(fecha_inicio, fecha_fin)
        self.ocupacion = ocupacion

class Estancia(ElementoTemporal):
    """Vincula Persona con Lugar en un tiempo dado."""
    def __init__(self, lugar: Lugar, fecha_inicio: date, fecha_fin: date = None):
        super().__init__(fecha_inicio, fecha_fin)
        self.lugar = lugar

# --- LA PERSONA (AGREGADOR DE TEMPORALIDAD) ---

class Persona:
    def __init__(self, fecha_nacimiento: date, lugar_nacimiento: Lugar):
        # Datos estáticos (Invariantes biológicos)
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.fecha_fallecimiento: Optional[date] = None
        
        # Historiales (Listas de objetos temporales)
        self._historial_identidad: List[IdentidadTemporal] = []
        self._historial_ocupaciones: List[DesempenoLaboral] = []
        self._historial_viajes: List[Estancia] = []
        self._contactos: List['RelacionPersonal'] = [] # Se definiría similar

    def definir_identidad(self, identidad: IdentidadTemporal):
        self._historial_identidad.append(identidad)

    def agregar_ocupacion(self, ocupacion: Ocupacion, inicio: date, fin: date = None):
        desempeno = DesempenoLaboral(ocupacion, inicio, fin)
        self._historial_ocupaciones.append(desempeno)

    def viajar_a(self, lugar: Lugar, inicio: date, fin: date):
        viaje = Estancia(lugar, inicio, fin)
        self._historial_viajes.append(viaje)

    # --- MÉTODO CLAVE DEL MODELO ---
    def obtener_perfil_en_fecha(self, fecha_consulta: date):
        """
        Reconstruye el estado de la persona en una fecha específica del pasado.
        """
        print(f"\n--- BIOGRAFÍA A FECHA: {fecha_consulta} ---")
        
        # 1. Buscar nombre activo
        identidad_activa = next((i for i in self._historial_identidad if i.es_valido_en(fecha_consulta)), None)
        if identidad_activa:
            print(f"Nombre: {identidad_activa}")
        else:
            print("Nombre: (Desconocido o no nacido en esta fecha)")

        # 2. Buscar ocupaciones activas
        ocupaciones = [o for o in self._historial_ocupaciones if o.es_valido_en(fecha_consulta)]
        if ocupaciones:
            print("Ocupaciones activas:")
            for oc in ocupaciones:
                print(f" - {oc.ocupacion.nombre}")
        
        # 3. Buscar ubicación
        ubicacion = next((v for v in self._historial_viajes if v.es_valido_en(fecha_consulta)), None)
        if ubicacion:
            print(f"Ubicación: De visita en {ubicacion.lugar.nombre}, {ubicacion.lugar.pais}")
        else:
            print("Ubicación: Residencia habitual (no hay viaje registrado)")

# --- EJEMPLO DE USO ---

if __name__ == "__main__":
    # 1. Nace la persona
    madrid = Lugar("Madrid", "España")
    paris = Lugar("París", "Francia")
    
    p = Persona(date(1980, 1, 1), madrid)

    # 2. Evolución del Nombre/Título
    # De 1980 a 2005 fue "Sr. Juan García"
    p.definir_identidad(IdentidadTemporal("Juan", "García", "Sr.", date(1980, 1, 1), date(2005, 5, 20)))
    # En 2005 consigue un doctorado y cambia su tratamiento
    p.definir_identidad(IdentidadTemporal("Juan", "García", "Dr.", date(2005, 5, 21)))

    # 3. Evolución Profesional
    p.agregar_ocupacion(Ocupacion("Estudiante"), date(1998, 9, 1), date(2005, 5, 20))
    p.agregar_ocupacion(Ocupacion("Arqueólogo"), date(2005, 6, 1)) # Hasta hoy

    # 4. Viajes
    p.viajar_a(paris, date(2004, 1, 1), date(2004, 6, 1)) # Erasmus

    # --- CONSULTAS TEMPORALES ---
    
    # Consulta 1: Año 2000 (Estudiante)
    p.obtener_perfil_en_fecha(date(2000, 3, 15))
    
    # Consulta 2: Año 2004 (En París)
    p.obtener_perfil_en_fecha(date(2004, 2, 14))

    # Consulta 3: Año 2010 (Doctor y Arqueólogo)
    p.obtener_perfil_en_fecha(date(2010, 1, 1))