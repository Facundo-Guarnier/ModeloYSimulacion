from Calentador_agua.clases.Liquido import Liquido
from Calentador_agua.clases.Material import Material


class Recipiente:
    """
    Clase que representa un recipiente cilíndrico que contiene un liquido.
    - Altura (cm)
    - Diámetro (cm)
    - Espesor del aislante (cm)
    - Material del recipiente (Material)
    - Liquido (Liquido)
    - Volumen/Capacidad (cm^3)
    - Area total/Superficie (cm^2)
    - Masa del liquido (g)
    - Nombre (str)
    """
    
    def __init__(self, altura:float, diametro:float, material:Material, espesor_aislante:float, liquido:Liquido) -> None:
        self.altura = altura
        self.diametro = diametro
        self.espesor_aislante = espesor_aislante
        
        self.material = material
        self.liquido = liquido
        
        self.volumen = self.__setVolumen()
        self.superficie = self.__setSuperficie()
        self.masa_liquido = self.volumen * liquido.densidad
        
        self.nombre = "Cilindro"
    
    
    def __setVolumen(self) -> float:
        """
        Calcular el volumen de la superficie del recipiente.
        - πr^2h
        """
        return 3.1416 * (self.diametro/2)**2 * self.altura
    
    
    def __setSuperficie(self) -> float:
        """
        Calcular la superficie total del recipiente.
        - 2πrr + 2πrh 
        """
        return 2 * 3.1416 * (self.diametro/2)**2 + 2 * 3.1416 * (self.diametro/2) * self.altura
    
    
    def __str__(self) -> str:
        return f"Recipiente: {self.nombre}\nVolumen (cm^3) : {self.volumen:.2f}\nMasa del liquido (g): {self.masa_liquido:.2f}\nSuperficie (cm^2): {self.superficie:.2f}\nEspesor del aislante (cm): {self.espesor_aislante}"