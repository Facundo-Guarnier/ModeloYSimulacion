class Material: 
    """
    Clase que representa un material aislante.  
    - Nombre del material (str)
    - Coeficiente termico (W/m°C)
    """
    
    def __init__(self, nombre:str, conductividad_térmica:float) -> None:
        self.nombre = nombre
        self.conductividad_térmica = conductividad_térmica
    
    def __str__(self) -> str:
        return f"Material: {self.nombre}\nCoeficiente termico (W/m°C): {self.conductividad_térmica:.3f}"