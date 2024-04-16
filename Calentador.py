from Recipiente import Recipiente
import matplotlib.pyplot as plt


class Calentador:
    """
    Clase que representa un calentador de agua teniendo en cuenta todos los factores que intervienen en el proceso.
    - Temperatura ambiente
    - Temperatura inicial
    - Temperatura final

    - Tiempo objetivo

    - Tipo de recipiente

    - Tension
    - Resistencia
    - Potencia
    """
    
    def __init__(self, recipiente:Recipiente, tension:float, temperatura_liquido_inicial:float, temperatura_liquido_final:float, temperatura_ambiente:float, tiempo_objetivo:int) -> None:
        self.temperatura_liquido_inicial = temperatura_liquido_inicial
        self.temperatura_liquido_final = temperatura_liquido_final
        self.temperatura_ambiente = temperatura_ambiente
        
        self.tiempo_objetivo = tiempo_objetivo
        
        self.recipiente = recipiente
        
        self.tension = tension
        self.resistencia = 0.0
        self.potencia = 0.0
    
    def tp1_a(self) -> str:     
        """
        Calcular la potencia, corriente y resistencia del calentador.
        """
        cantidad_calor = self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico * (self.temperatura_liquido_final - self.temperatura_liquido_inicial)
        
        self.potencia = cantidad_calor / self.tiempo_objetivo
        self.resistencia = self.tension / (self.potencia / self.tension)
        
        return (
            f"Tp1: A\n" +
            f"Cantidad de calor (Q): {cantidad_calor:.3f} J\n" +
            f"Potencia: {self.potencia:.3f} W\n" +
            f"Corriente: {self.potencia/self.tension:.3f} A\n" +
            f"Resistencia: {self.resistencia:.3f} Ω"
        )

    def tp1_b(self) -> str:
        """
        Calcular el aumento de temperatura luego de 1s de conectar la alimentación, suponiendo que no existe pérdida de calor.
        """
        cantidad_calor = self.potencia*1
        cambio_temperatura = cantidad_calor / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
        
        return (
            f"Tp1: B\n" +
            f"Aumento de temperatura luego de 1s: {cambio_temperatura:.3f} °C"
        )
    
    def tp2(self) -> str:
        """
        Graficar el aumento de temperatura del agua en el recipiente sin perdida de calor (lineal).
        """
        temperaturas = []
        temperatura_agua = self.temperatura_liquido_inicial
        for segundo in range(self.tiempo_objetivo):
            cantidad_calor = self.potencia
            masa_agua = self.recipiente.masa_liquido
            calor_especifico_agua = self.recipiente.liquido.calor_especifico
            cambio_temperatura = cantidad_calor / (masa_agua * calor_especifico_agua)
            
            temperatura_agua += cambio_temperatura
            temperaturas.append(temperatura_agua)
        
        
        plt.plot(range(self.tiempo_objetivo), temperaturas)
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("Aumento de temperatura del agua en el recipiente \nsin perdida de calor")
        plt.grid()
        plt.show()
        return (
            "Tp2 \n" +
            "Gráfica realizada con éxito."
        )
        
    def tp3(self) -> str:
        """
        Graficar el aumento de temperatura del agua. Tener en cuenta:
        - Perdida de calor.
        - Usar la potencia original.
        - Temperatura ambiente.
        - Superficie del recipiente.
        - Conductividad térmica del material del recipiente.
        - Espesor del aislante.
        """
        
        temperaturas = []
        temperatura_agua = self.temperatura_liquido_inicial
        for segundo in range(self.tiempo_objetivo):
            cantidad_calor = self.potencia
            # cantidad_calor = 2638.370
            masa_agua = self.recipiente.masa_liquido
            calor_especifico_agua = self.recipiente.liquido.calor_especifico
            cambio_temperatura = cantidad_calor / (masa_agua * calor_especifico_agua)
            
            if temperatura_agua > self.temperatura_ambiente:
                perdida_calor = (temperatura_agua - self.temperatura_ambiente) * self.recipiente.superficie * self.recipiente.material.conductividad_térmica
                cambio_temperatura -= perdida_calor / (masa_agua * calor_especifico_agua)
            
            temperatura_agua += cambio_temperatura
            temperaturas.append(temperatura_agua)
        
        plt.plot(range(self.tiempo_objetivo), temperaturas)
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title(f"TP2: Aumento de temperatura del agua \nTemperatura maxima {temperatura_agua:.3f}")
        plt.grid()
        plt.show()
        return (
            "Tp3 \n" +
            "Gráfica realizada con éxito."
        )
    
    def tp4_a(self) -> str:
        """
        Calcular la potencia neceesaria (constante) para alcanzar la temperatura final en el tiempo esperado y con perdida de calor.
        """
        #! Intento 1: CREO que da un resultado grande 2938.370 W
        # cantidad_calor = self.recipiente.superficie * self.recipiente.material.conductividad_térmica * (self.temperatura_liquido_final - self.temperatura_ambiente)
        # potencia_necesaria =  ((self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico * (self.temperatura_liquido_final - self.temperatura_liquido_inicial)) / self.tiempo_objetivo) + cantidad_calor
        
        #! Intento 2:
        resistencia_termina = self.recipiente.espesor_aislante / self.recipiente.material.conductividad_térmica
        diferencia_temperatura = self.temperatura_liquido_final - self.temperatura_ambiente
        cantidad_calor_perdido = diferencia_temperatura / resistencia_termina
        potencia_necesaria = ((self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico * (self.temperatura_liquido_final - self.temperatura_liquido_inicial)) / self.tiempo_objetivo) + cantidad_calor_perdido
        
        
        return (
            f"Tp4: A\n" +
            f"Potencia necesaria: {potencia_necesaria:.3f} W"
        )
    
    def tp4_b(self) -> str:
        """
        Graficar el aumento de temperatura del agua en el recipiente con perdida de calor y con la potencia necesaria para llegar a la temperatura destino.
        """
        return (    
            "Tp4: B\n" +
            "Gráfica no realizada con éxito."
        )