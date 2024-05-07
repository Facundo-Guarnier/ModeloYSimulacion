import copy, random
from clases.Recipiente import Recipiente


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
        Calcula la cantidad de calor necesaria para elevar la temperatura del agua en el recipiente hasta la temperatura objetivo, sin considerar la perdía de calor.
        
        Returns:
            float: Cantidad de calor necesaria para elevar la temperatura del agua en el recipiente: Q = m * c * ΔT -> J
        """
        return float(self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico * (self.temperatura_liquido_final - self.temperatura_liquido_inicial))
    
    
    def cambio_temperatura_por_segundo_sin_perdida(self, *, cantidad_calor:float) -> float:
        """
        Calcular el cambio de temperatura del agua en el recipiente en un segundo sin considerar la perdía de calor.
        
        Args:
            cantidad_calor (float): Cantidad de calor entregada al agua en el recipiente.
        
        Returns:
            float: Cambio de temperatura del agua en el recipiente: ΔT = Q / (m * c) -> C°
        """
        return cantidad_calor / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
    
    
    def cambio_temperatura_por_segundo_con_perdida(self, temperatura_actual:float) -> float:
        """
        Calcular el cambio de temperatura del agua en el recipiente en un segundo considerando la perdía de calor.

        Args:
            temperatura_actual (float): Temperatura actual del agua en el recipiente.

        Returns:
            float: Cambio de temperatura del agua en el recipiente: ΔT = (Q_ganado - Q_perdido) / (m * c) -> C°
        """
        
        cantidad_calor_ganado = self.potencia 
        cantidad_calor_perdido = self.recipiente.material.conductividad_térmica * (self.recipiente.superficie / self.recipiente.espesor_aislante) * (temperatura_actual - self.temperatura_ambiente) / self.recipiente.masa_liquido
        cantidad_calor_efectivo = cantidad_calor_ganado - cantidad_calor_perdido
        return cantidad_calor_efectivo / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
    
    
    def cantidad_calor_perdido_total(self) -> float:
        """
        Calcular la cantidad de calor perdido total por el recipiente.
        
        Returns:
            float: Cantidad de calor perdido total por el recipiente: Q = k * A * (ΔT) / (d * m) -> J
        """
        
        total_calor_perdido = 0.0
        temperatura_actual = self.temperatura_liquido_inicial
        
        for segundo in range(self.tiempo_objetivo):
            cantidad_calor_ganado = self.potencia 
            cantidad_calor_perdido = self.recipiente.material.conductividad_térmica * (self.recipiente.superficie / self.recipiente.espesor_aislante) * (temperatura_actual - self.temperatura_ambiente) / self.recipiente.masa_liquido
            total_calor_perdido += cantidad_calor_perdido
            cantidad_calor_efectivo = cantidad_calor_ganado - cantidad_calor_perdido
            temperatura_actual += cantidad_calor_efectivo / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
        
        return total_calor_perdido
    
    
    def aumento_temperatura_sin_perdida(self) -> list[float]:
        """
        Calcular el aumento de temperatura del agua en el recipiente sin perdida de
        calor durante todo el periodo de tiempo.
        
        Returns:
            list[float]: Lista con las temperaturas del agua en el recipiente por cada segundo.
        """
        
        temperatura_actual = self.temperatura_liquido_inicial
        temperaturas = []
        for segundo in range(self.tiempo_objetivo):
            temperatura_actual += self.cambio_temperatura_por_segundo_sin_perdida(cantidad_calor=self.potencia)
            temperaturas.append(temperatura_actual)
        
        return temperaturas
    
    
    def aumento_temperatura_con_perdida(self) -> list[float]:
        """
        Calcular el aumento de temperatura del agua en el recipiente con perdida de calor durante todo el periodo de tiempo.
        
        Returns:
            list[float]: Lista con las temperaturas del agua en el recipiente por cada segundo.
        """
        temperaturas_con_perdida = []
        temperatura_actual = self.temperatura_liquido_inicial

        for segundo in range(self.tiempo_objetivo):
            temperatura_actual += self.cambio_temperatura_por_segundo_con_perdida(temperatura_actual)
            temperaturas_con_perdida.append(temperatura_actual)
        
        return temperaturas_con_perdida
    
    
    def aumento_temperatura_estocástico(self, probabilidad:float, rango_duracion:list[int], rango_reduccion:list[int]) -> tuple[list[float], list[int], list[tuple[int, float]]]:
        """
        Calcular el aumento de temperatura del agua en el recipiente con perdida de calor durante todo el periodo de tiempo.
        Sucederá un evento estocástico con una probabilidad de 1/300 en cada segundo. El evento consiste en 
        un descenso de temperatura ambiente de X durante Y segundos.
        
        Returns:
            tuple[list[float]: Lista con la temperatura del agua en el recipiente en cada segundo.
            list[int]: Lista con los tiempos de inicio y fin de los eventos.
            list[tuple[int, float]]]: Lista con los datos de los eventos (tiempo evento, temperatura ambiente).
        """
        
        temperatura_ambiente_original = copy.copy(self.temperatura_ambiente)
        temperaturas_con_perdida:list[float] = []
        tiempos_evento:list[int] = []
        tiempo_restante_evento:int = 0
        datos_evento:list[tuple[int, float]] = [] #! [(tiempo evento, temperatura_ambiente)]
        
        temperatura_actual = self.temperatura_liquido_inicial
        
        for segundo in range(self.tiempo_objetivo):
            
            #! Evento estocástico
            if random.random() <= probabilidad and tiempo_restante_evento == 0:
                self.temperatura_ambiente -= random.randint(rango_reduccion[0], rango_reduccion[1])
                tiempo_restante_evento = random.randint(rango_duracion[0], rango_duracion[1])
                tiempos_evento.append(segundo)  #! Tiempo en el que inicia el evento
                datos_evento.append((tiempo_restante_evento, self.temperatura_ambiente))
            
            #! Calcular temperatura ganada y temperatura perdida
            temperatura_actual += self.cambio_temperatura_por_segundo_con_perdida(temperatura_actual)
            temperaturas_con_perdida.append(temperatura_actual)
            
            #! Reducir tiempo del evento
            if tiempo_restante_evento != 0:
                tiempo_restante_evento -= 1
                
                #! Fin del evento
                if tiempo_restante_evento == 0:
                    self.temperatura_ambiente = temperatura_ambiente_original
                    tiempos_evento.append(segundo)  #! Tiempo en el que termina el evento
            
            #! Fin de la simulación y finalizar evento
            if segundo == (self.tiempo_objetivo-1) and tiempo_restante_evento != 0:  
                tiempos_evento.append(segundo)
                datos_evento[-1] = (tiempos_evento[-1]-tiempos_evento[-2], self.temperatura_ambiente)
                self.temperatura_ambiente = temperatura_ambiente_original
        
        return temperaturas_con_perdida, tiempos_evento, datos_evento
    
    
    def __str__(self) -> str:
        return f"Temperatura inicial: {self.temperatura_liquido_inicial}°C\nTemperatura final: {self.temperatura_liquido_final}°C\nTemperatura ambiente: {self.temperatura_ambiente}°C\nTiempo objetivo: {self.tiempo_objetivo} segundos\nPotencia: {self.potencia:.2f} W\nResistencia: {self.resistencia:.2f}"