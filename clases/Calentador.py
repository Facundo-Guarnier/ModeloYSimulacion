from clases.Recipiente import Recipiente
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
            f"Cantidad de calor (Q): {cantidad_calor:.2f} J\n" +
            f"Potencia: {self.potencia:.2f} W\n" +
            f"Corriente: {self.potencia/self.tension:.2f} A\n" +
            f"Resistencia: {self.resistencia:.2f} Ω"
        )

    def tp1_b(self) -> str:
        """
        Calcular el aumento de temperatura luego de 1s de conectar la alimentación, suponiendo que no existe pérdida de calor.
        """
        cantidad_calor = self.potencia*1
        cambio_temperatura = cantidad_calor / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
        
        return (
            f"Tp1: B\n" +
            f"Aumento de temperatura luego de 1s: {cambio_temperatura:.2f} °C"
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
        Calcular la pérdida de calor de nuestro dispositivo, según las especificaciones de diseño. 
        Calor perdido en Watts/grado Kelvin = Coeficiente de Conductividad Térmica W/m grado Kelvin * Sup/Esp/m
        """
        
        cantidad_calor_perdido =  self.recipiente.material.conductividad_térmica * (self.recipiente.superficie/self.recipiente.espesor_aislante)/self.recipiente.masa_liquido

        return (
            f"Tp3\n" +
            f"Cantidad de calor perdido: {cantidad_calor_perdido:.2f} W"
        )
    
    def tp4(self) -> str:
        """
        Graficar la temperatura del fluido dentro del calentador sin pérdidas y con pérdidas para cada tick de tiempo, 
        hasta llegar al tiempo deseado para que el dispositivo cumpla su tarea.

        Para realizar el gráfico con pérdidas, se debe considerar los vatios efectivos entregados al fluido restando al 
        calor producido por la resistencia, el calor perdido por las paredes del recipiente. Con este calor efectivo se
        calcula la variación de temperatura del fluido para cada tick de tiempo.
        """
        
        temperaturas_sin_perdida = []
        temperaturas_con_perdida = []
        
        for segundo in range(self.tiempo_objetivo):
        
            #! Sin perdida
            cambio_temperatura_sin_perdida = (self.potencia * segundo) / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
            temperatura_agua_sin_perdida = self.temperatura_liquido_inicial + cambio_temperatura_sin_perdida
            temperaturas_sin_perdida.append(temperatura_agua_sin_perdida)
        
            #! Con perdida
            calor_perdido =  self.recipiente.material.conductividad_térmica * (self.recipiente.superficie/self.recipiente.espesor_aislante)/self.recipiente.masa_liquido
        
            calor_perdido_total = calor_perdido * (temperatura_agua_sin_perdida - self.temperatura_ambiente) * segundo
            cantidad_calor_efectivo = (self.potencia * segundo) - calor_perdido_total
            
            delta_T_efectivo = cantidad_calor_efectivo / (self.recipiente.masa_liquido * self.recipiente.liquido.calor_especifico)
            temperaturas_con_perdida.append(self.temperatura_liquido_inicial + delta_T_efectivo)

        
        plt.plot(range(self.tiempo_objetivo), temperaturas_sin_perdida, label="Sin perdida", linestyle="-")
        plt.plot(range(self.tiempo_objetivo), temperaturas_con_perdida, label="Con perdida" , linestyle="-")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("Aumento de temperatura del agua en el\nrecipiente con/sin perdida de calor.")
        plt.grid()
        plt.legend()
        plt.show()
        return (
            "Tp4 \n" +
            "Gráfica realizada con éxito.\n" + 
            f"Tempera maxima con pedida de calor: {temperaturas_con_perdida[-1]:.2f}°C\n"
        )