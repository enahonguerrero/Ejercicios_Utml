class ActuacionArqueologica:
    def __init__(self, fecha_inicio, fecha_fin, tipo):

        tipos_validos = ["sondeo", "excavación", "seguimiento"]
        if tipo.lower() not in tipos_validos:
            raise ValueError(f"Tipo inválido. Debe ser uno de: {tipos_validos}")
        
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo.lower()

    def __str__(self):
        return (f"Actuación arqueológica de tipo '{self.tipo}' "
                f"comenzada el {self.fecha_inicio} y finalizada el {self.fecha_fin}.")
a = ActuacionArqueologica("2024-01-15", "2024-02-02", "excavación")
print(a)
