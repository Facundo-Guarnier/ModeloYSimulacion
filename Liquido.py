class Liquido:
    """
    Clase que representa un liquido con sus propiedades físicas.
    - Densidad (g/cm^3)
    - Calor especifico (J/g°C)
    - Nombre (str)
    """
    
    def __init__(self, densidad:float, calor_especifico:float, nombre:str) -> None:
        self.densidad = densidad
        self.calor_especifico = calor_especifico
        self.nombre = nombre
    
    def __str__(self) -> str:
        return f"Liquido: {self.nombre}\nDensidad (g/cm^3): {self.densidad:.3f}\nCalor especifico (J/g°C): {self.calor_especifico:.3f}"