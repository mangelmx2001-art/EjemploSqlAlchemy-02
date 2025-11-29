class ColiseoDeportivo:
    def __init__(self, nombre, ciudad, capacidad, deporte):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad
        self.deporte = deporte

    def __str__(self):
        return f"Coliseo: {self.nombre} | Ciudad: {self.ciudad} | Aforo: {self.capacidad}"s