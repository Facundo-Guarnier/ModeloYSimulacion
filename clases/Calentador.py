import random
from clases.Recipiente import Recipiente
import matplotlib.pyplot as plt


class Calentador:
    def __init__(self, recipiente:Recipiente, tension:float, temperatura_liquido_inicial:float, temperatura_liquido_final:float, temperatura_ambiente:float, tiempo_objetivo:int) -> None:
        """
        Clase que representa un calentador de agua teniendo en cuenta todos los factores que intervienen en el proceso.
        
        Args:
            recipiente (Recipiente): Recipiente que contiene el liquido a calentar.
            tension (float): Voltaje de la fuente de alimentación (V).
            temperatura_liquido_inicial (float): Temperatura inicial del liquido en el recipiente.
            temperatura_liquido_final (float): Temperatura final deseada del liquido en el recipiente.
            temperatura_ambiente (float): Temperatura ambiente.
            tiempo_objetivo (int): Tiempo en segundos que se desea alcanzar la temperatura final.
        """
        self.temperatura_liquido_inicial = temperatura_liquido_inicial
        self.temperatura_liquido_final = temperatura_liquido_final
        self.temperatura_ambiente = temperatura_ambiente
        
        self.tiempo_objetivo = tiempo_objetivo
        self.recipiente = recipiente
        self.tension = tension
        
        self.potencia = self.cantidad_calor_necesaria() / self.tiempo_objetivo
        self.resistencia = self.tension / (self.potencia / self.tension)
    
    
    def cantidad_calor_necesaria(self) -> float:     
        """
        Calcular la cantidad de calor necesaria para elevar la temperatura del agua en el recipiente, sin considerar la perdía de calor.
        
        Returns:
            float: Cantidad de calor necesaria para elevar la temperatura del agua en el recipiente: Q = m * c * ΔT -> J
        """
        return float(self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico * (self.temperatura_liquido_final - self.temperatura_liquido_inicial))
    
    
    def cambio_temperatura_por_segundo(self, cantidad_calor:float) -> float:
        """
        Calcular el cambio de temperatura del agua en el recipiente, dados la cantidad de calor y el tiempo transcurrido, sin considerar la perdía de calor.
        
        Args:
            cantidad_calor (float): Cantidad de calor entregada al agua en el recipiente.
        
        Returns:
            float: Cambio de temperatura del agua en el recipiente: ΔT = Q / (m * c) -> C°
        """
        return cantidad_calor / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
    
    
    def aumento_temperatura_sin_perdida (self) -> list[float]:
        """
        Calcular el aumento de temperatura del agua en el recipiente sin perdida de
        calor durante todo el periodo de tiempo.
        
        Returns:
            list[float]: Lista con el aumento de temperatura del agua en el recipiente en cada segundo.
        """
        temperaturas = []
        for segundo in range(self.tiempo_objetivo):
            cambio_temperatura_sin_perdida = (self.potencia * segundo) / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
            temperatura_agua_sin_perdida = self.temperatura_liquido_inicial + cambio_temperatura_sin_perdida
            temperaturas.append(temperatura_agua_sin_perdida)
        
        return temperaturas
    
    
    def cantidad_calor_perdido_total(self) -> float:
        """
        Calcular la cantidad de calor perdido total por el recipiente.
        
        Returns:
            float: Cantidad de calor perdido total por el recipiente: Q = k * A * ΔT / d -> J
        """
        return self.recipiente.material.conductividad_térmica * (self.recipiente.superficie / self.recipiente.espesor_aislante) * (self.temperatura_liquido_final - self.temperatura_ambiente) / self.recipiente.masa_liquido
    
    
    def aumento_temperatura_con_perdida(self) -> list[float]:
        """
        Calcular el aumento de temperatura del agua en el recipiente con perdida de calor durante todo el periodo de tiempo.
        
        Returns:
            list[float]: Lista con el aumento de temperatura del agua en el recipiente en cada segundo.
        """
        temperaturas_sin_perdida = self.aumento_temperatura_sin_perdida()
        temperaturas_con_perdida = []
        
        for segundo in range(self.tiempo_objetivo):
            # calor_perdido_por_segundo = self.recipiente.material.conductividad_térmica * (self.recipiente.superficie / self.recipiente.espesor_aislante) * (temperatura_agua_sin_perdida - self.temperatura_ambiente) / self.recipiente.masa_liquido
            # calor_total_perdido = calor_perdido_por_segundo * segundo
            # calor_total_entregado = self.potencia * segundo
            # calor_efectivo = calor_total_entregado - calor_total_perdido 
            # delta_T_efectivo = calor_efectivo / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
            # temperaturas_con_perdida.append(self.temperatura_liquido_inicial + delta_T_efectivo)
            
            calor_perdido_por_segundo = self.recipiente.material.conductividad_térmica * (self.recipiente.superficie / self.recipiente.espesor_aislante) * (temperaturas_sin_perdida[segundo] - self.temperatura_ambiente) / self.recipiente.masa_liquido
            calor_total_perdido = calor_perdido_por_segundo * segundo
            calor_total_entregado = self.potencia * segundo
            calor_efectivo = calor_total_entregado - calor_total_perdido 
            delta_T_efectivo = calor_efectivo / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
            temperaturas_con_perdida.append(self.temperatura_liquido_inicial + delta_T_efectivo)
        
        return temperaturas_con_perdida