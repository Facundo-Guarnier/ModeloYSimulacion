import copy, random
from matplotlib import pyplot as plt
from Calentador_agua.clases.Calentador import Calentador
from Calentador_agua.clases.Liquido import Liquido
from Calentador_agua.clases.Material import Material
from Calentador_agua.clases.Recipiente import Recipiente


class App:
    def __init__(self, liquido: Liquido, material:Material, recipiente: Recipiente, calentador: Calentador ) -> None:
        """
        Clase que representa la aplicación principal.
        """
        self.liquido = liquido
        self.material = material
        self.recipiente = recipiente
        self.calentador = calentador
    
    
    def tp1_a(self) -> None:
        """
        Calcular la potencia, corriente y resistencia del calentador.
        """
        
        print(
            f"Tp1 A:"+
            f"\nPotencia: {self.calentador.potencia:.2f} W" +
            f"\nCorriente: {self.calentador.potencia/self.calentador.tension:.2f} A"+ 
            f"\nResistencia: {self.calentador.resistencia:.2f} Ω" +
            f"\nCalor necesario: {self.calentador.cantidad_calor_necesaria():.2f} J"
        )
    
    
    def tp1_b(self) -> None:
        """
        Calcular el aumento de temperatura luego de 1s de conectar la alimentación, suponiendo que no existe pérdida de calor.
        """
        
        cantidad_calor = self.calentador.potencia * 1
        
        print(
            f"Tp1 B:"+
            f"\nAumento de temperatura luego de 1s: {self.calentador.cambio_temperatura_por_segundo_sin_perdida(cantidad_calor=cantidad_calor):.2f} °C"
        )
    
    
    def tp2(self) -> None:
        """
        Graficar el aumento de temperatura del agua en el recipiente sin perdida de calor (lineal).
        """
        
        print(f"Tp2:\nGráfico de aumento de temperatura del agua en el recipiente sin perdida de calor.")
        
        plt.plot(range(self.calentador.tiempo_objetivo), self.calentador.aumento_temperatura_sin_perdida())
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("TP2: Aumento de temperatura del agua en el recipiente \nsin perdida de calor")
        plt.grid()
        plt.show()
    
    
    def tp3(self) -> None:
        """
        Calcular la pérdida de calor de nuestro dispositivo, según las especificaciones de diseño. 
        """
        
        print(f"Tp3:\nPerdida de calor: {self.calentador.cantidad_calor_perdido_total():.2f} J")
    
    
    def tp4(self) -> None:
        """
        Graficar la temperatura del fluido dentro del calentador sin pérdidas y con pérdidas para cada tick de tiempo, 
        hasta llegar al tiempo deseado para que el dispositivo cumpla su tarea.

        Para realizar el gráfico con pérdidas, se debe considerar los vatios efectivos entregados al fluido restando al 
        calor producido por la resistencia, el calor perdido por las paredes del recipiente. Con este calor efectivo se
        calcula la variación de temperatura del fluido para cada tick de tiempo.
        """
        
        print(f"Tp4:\nGráfico de aumento de temperatura del agua en el recipiente con/sin perdida de calor.")
        
        max_temp = max(self.calentador.aumento_temperatura_con_perdida())
        
        plt.plot(range(self.calentador.tiempo_objetivo), self.calentador.aumento_temperatura_sin_perdida(), label="Temperatura sin perdida", linestyle="-")
        plt.plot(range(self.calentador.tiempo_objetivo), self.calentador.aumento_temperatura_con_perdida(), label="Temperatura con perdida" , linestyle="-")
        plt.axhline(y=max_temp, color='#00FF00', linestyle='--', label=f"Temperatura maxima ({max_temp:.2f})") 
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("TP4: Aumento de temperatura del agua en el\nrecipiente con/sin perdida de calor")
        plt.grid()
        plt.legend()
        plt.show()
    
    
    def tp5_a(self) -> None:
        """
        Generar familias de curvas con distribuciones normales y uniformes con:
        - Distribución uniforme de 5 valores próximos de resistencias
        """
        
        print("Tp5 A:\nGráfico de variacion de resistencia en el calentador.")
        
        calentador_temporal = copy.deepcopy(self.calentador)
        
        resistencia_original = calentador_temporal.resistencia
        resistencias = [ resistencia_original * (1 + random.uniform(-0.1, 0.1)) for _ in range(5)]
        
        for resistencia in resistencias:
            calentador_temporal.resistencia = resistencia
            calentador_temporal.potencia = calentador_temporal.tension**2 / resistencia
            plt.plot(range(calentador_temporal.tiempo_objetivo), calentador_temporal.aumento_temperatura_con_perdida(), label=f"{resistencia:.2f} Ω" , linestyle="-")
        
        calentador_temporal.resistencia = resistencia_original
        
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("TP5 A: Variacion de resistencia en el calentador")
        plt.grid()
        plt.legend()
        plt.show()
    
    
    def tp5_b(self) -> None:
        """
        Generar familias de curvas con distribuciones normales y uniformes con:
        - Distribución normal de 5 temperaturas iniciales del agua. Media 10, desvío standard=5
        """
        
        print("Tp5 B:\nGráfico de variacion de temperatura inicial del agua.")
        
        calentador_temporal = copy.deepcopy(self.calentador)
        
        temperatura_inicial_original = calentador_temporal.temperatura_liquido_inicial
        temperaturas_iniciales = [random.normalvariate(10, 5) for _ in range(5)]
        
        for temperatura_inicial in temperaturas_iniciales:
            calentador_temporal.temperatura_liquido_inicial = temperatura_inicial
            plt.plot(range(calentador_temporal.tiempo_objetivo), calentador_temporal.aumento_temperatura_con_perdida(), label=f"{temperatura_inicial:.2f} °C" , linestyle="-")
            
        calentador_temporal.temperatura_liquido_inicial = temperatura_inicial_original
        
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("TP5 B: Variacion de temperatura inicial del agua")
        plt.grid()
        plt.legend()
        plt.show()
    
    
    def tp5_c(self) -> None:
        """
        Generar familias de curvas con distribuciones normales y uniformes con:
        - Distribución uniforme de 8 temperaturas iniciales del ambiente, entre -20 y 50 grados.
        """
        
        print("Tp5 C:\nGráfico de variacion de temperatura ambiente.")
        
        calentador_temporal = copy.deepcopy(self.calentador)
        
        temperaturas_ambiente_original = calentador_temporal.temperatura_ambiente
        temperaturas_ambiente = [random.uniform(-20, 50) for _ in range(8)]
        
        for temperatura_ambiente in temperaturas_ambiente:
            calentador_temporal.temperatura_ambiente = temperatura_ambiente
            plt.plot(range(calentador_temporal.tiempo_objetivo), calentador_temporal.aumento_temperatura_con_perdida(), label=f"{temperatura_ambiente:.2f} °C" , linestyle="-")
        
        calentador_temporal.temperatura_ambiente = temperaturas_ambiente_original
        
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("TP5 C: Variacion de temperatura ambiente")
        plt.grid()
        plt.legend()
        plt.show()
    
    
    def tp5_d(self) -> None:
        """
        Generar familias de curvas con distribuciones normales y uniformes con:
        - Distribución normal de 5 valores de tension de alimentación Media 12 SD:4 o Media 220, SD 40.
        """
        
        print("Tp5 D:\nGráfico de variacion de tension de alimentación.")
        
        calentador_temporal = copy.deepcopy(self.calentador)
        
        tension_original = calentador_temporal.tension
        tensiones = [random.normalvariate(220, 40) for _ in range(5)] 

        for tension in tensiones:
            calentador_temporal.tension = tension
            calentador_temporal.potencia = tension**2 / calentador_temporal.resistencia
            plt.plot(range(calentador_temporal.tiempo_objetivo), calentador_temporal.aumento_temperatura_con_perdida(), label=f"{tension:.2f} V" , linestyle="-")
        
        calentador_temporal.tension = tension_original
        
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("TP5 D: Variacion de tension de alimentación")
        plt.grid()
        plt.legend()
        plt.show()
    
    
    def tp5_e(self) -> None:
        """
        Generar familias de curvas con distribuciones normales y uniformes con:
        - Simulaciones que contengan todas las familias de curvas previas.
        """
        
        print("Tp5 E:\nGráfico de variacion de todas las variables.")
        
        calentador_temporal = copy.deepcopy(self.calentador)
        
        #! Tp5 A
        resistencia_original = calentador_temporal.resistencia
        resistencias = [ resistencia_original * (1 + random.uniform(-0.1, 0.1)) for _ in range(5)]
        
        #! Tp5 B
        temperaturas_iniciales = [random.normalvariate(10, 5) for _ in range(5)]
        
        #! Tp5 C
        temperaturas_ambiente = [random.uniform(-20, 50) for _ in range(5)]
        
        #! Tp5 D
        tensiones = [random.normalvariate(220, 40) for _ in range(5)]
        
        #! Gráficos
        for i in range(5):
            calentador_temporal.resistencia = resistencias[i]
            calentador_temporal.temperatura_liquido_inicial = temperaturas_iniciales[i]
            calentador_temporal.temperatura_ambiente = temperaturas_ambiente[i]
            calentador_temporal.tension = tensiones[i]
            calentador_temporal.potencia = tensiones[i]**2 / calentador_temporal.resistencia
            plt.plot(range(calentador_temporal.tiempo_objetivo), calentador_temporal.aumento_temperatura_con_perdida(), label=f"Curva {i+1}" , linestyle="-")
            
            print(
                f"Curva {i+1}:"+
                f"\n - Resistencia: {resistencias[i]:.2f} Ω"+
                f"\n - Temperatura inicial: {temperaturas_iniciales[i]:.2f} °C"+
                f"\n - Temperatura ambiente: {temperaturas_ambiente[i]:.2f} °C"+
                f"\n - Tensión: {tensiones[i]:.2f} V"
            )
        
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("TP5 E: Variacion de todas las variables")
        plt.grid()
        plt.legend()
        plt.show()
    
    
    def tp6(self) -> None:
        """
        Simulación de un fenómeno estocástico que tiene una probabilidad de 
        ocurrencia de 1/300 en cada tick de tiempo. Con variables aleatorias: si el 
        fenómeno tiene lugar, ocurre un descenso de X grados, durante Y segundos. 
        Variación máxima 50 grados en descenso. Rehacer el gráfico de temperaturas del TP 4.
        """
        
        print(
            "Tp6"+
            "\nEvento estocástico de reducción de la temperatura ambiente:"+
            "\n - Probabilidad de ocurrencia: 1/300"+
            "\n - Rango de reducción: [20, 50]"+
            "\n - Rango de duración: [20, 120]"
        )
        
        temperaturas, tiempos_evento, datos_evento = self.calentador.aumento_temperatura_estocástico(
            probabilidad=1/300,
            rango_reduccion=[20, 50],
            rango_duracion=[45, 180],
        )
        max_temp = max(temperaturas)
        min_temp = min(temperaturas)
        
        plt.plot(range(self.calentador.tiempo_objetivo), temperaturas, label="Temperatura del agua" , linestyle="-")
        plt.axhline(y=max_temp, color='#00FF00', linestyle='--', label=f"Temperatura maxima ({max_temp:.2f})") 
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("TP6: Aumento de temperatura del agua con evento estocástico\n(Cambio de la temperatura ambiente)")
        
        colores_evento = ['#FF0000', '#FFFF00', '#00FFFF', '#808080']
        #! Líneas verticales para cada tiempo en tiempos_evento
        for i in range(len(datos_evento)):
            plt.axvline(x=tiempos_evento[i*2], color=colores_evento[i%4], linestyle='--') 
            plt.axvline(x=tiempos_evento[i*2+1], color=colores_evento[i%4], linestyle='--') 
            plt.fill_betweenx(y=[min_temp, max_temp], x1=tiempos_evento[i*2], x2=tiempos_evento[i*2+1],  color=colores_evento[i%4], alpha=0.3, label=f"Evento {i+1} (Temp. ambiente {datos_evento[i][1]}C° durante {datos_evento[i][0]}s)")
            print(
                f"Evento {i+1}:"+
                f"\n  Temperatura ambiente de {datos_evento[i][1]}°C durante {datos_evento[i][0]}s (Inicio: {tiempos_evento[i*2]}s, Fin: {tiempos_evento[i*2+1]}s)")
        
        plt.grid()
        plt.legend()
        plt.show()
    
    
    def main(self) -> None:
        self.tp1_a()
        print("-"*15)
        self.tp1_b()
        print("-"*15)
        self.tp2()
        print("-"*15)
        self.tp3()
        print("-"*15)
        self.tp4()
        print("-"*15)
        self.tp5_a()
        print("-"*15)
        self.tp5_b()
        print("-"*15)
        self.tp5_c()
        print("-"*15)
        self.tp5_d()
        print("-"*15)
        self.tp5_e()
        print("-"*15)
        self.tp6()