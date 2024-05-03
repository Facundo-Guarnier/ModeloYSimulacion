import random
from matplotlib import pyplot as plt
from clases.Calentador import Calentador
from clases.Liquido import Liquido
from clases.Material import Material
from clases.Recipiente import Recipiente


class App:
    def __init__(self) -> None:
        """
        Clase que representa la aplicación principal.
        """
        pass
    
    def setLiquido(self, liquido:Liquido) -> None:
        self.liquido = liquido

    def setMaterial(self, materia:Material) -> None:
        self.material = materia

    def setRecipiente(self, recipiente:Recipiente) -> None:
        self.recipiente = recipiente
    
    def setCalentador(self, calentador:Calentador) -> None:
        self.calentador = calentador
    
    def tp1_a(self) -> None:
        """
        Calcular la potencia, corriente y resistencia del calentador.
        """
        print(f"Tp1 A:\nPotencia: {self.calentador.potencia:.2f} W\nCorriente: {self.calentador.potencia/self.calentador.tension:.2f} A\nResistencia: {self.calentador.resistencia:.2f} Ω\nCalor necesario: {self.calentador.cantidad_calor_necesaria():.2f} J")
    
    
    def tp1_b(self) -> None:
        """
        Calcular el aumento de temperatura luego de 1s de conectar la alimentación, suponiendo que no existe pérdida de calor.
        """
        
        cantidad_calor = self.calentador.potencia * 1
        
        print(
            f"Tp1 B:\nAumento de temperatura luego de 1s: {self.calentador.cambio_temperatura_por_segundo(cantidad_calor):.2f} °C"
        )
    
    
    def tp2(self) -> None:
        """
        Graficar el aumento de temperatura del agua en el recipiente sin perdida de calor (lineal).
        """
        
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
        
        max_temp = max(self.calentador.aumento_temperatura_con_perdida())
        
        plt.plot(range(self.calentador.tiempo_objetivo), self.calentador.aumento_temperatura_sin_perdida(), label="Sin perdida", linestyle="-")
        plt.plot(range(self.calentador.tiempo_objetivo), self.calentador.aumento_temperatura_con_perdida(), label="Con perdida" , linestyle="-")
        plt.axhline(y=max_temp, color='g', linestyle='--', label="Temperatura final") 
        plt.text(0.5, max_temp, f'{max_temp:.2f}', color='g', fontsize=10, ha='center')
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
        resistencia_original = self.calentador.resistencia
        resistencias = [ resistencia_original * (1 + random.uniform(-0.1, 0.1)) for _ in range(5)]
        
        for resistencia in resistencias:
            self.calentador.resistencia = resistencia
            self.calentador.potencia = self.calentador.tension**2 / resistencia
            plt.plot(range(self.calentador.tiempo_objetivo), self.calentador.aumento_temperatura_con_perdida(), label=f"{resistencia:.2f} Ω" , linestyle="-")
        
        self.calentador.resistencia = resistencia_original
        
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
        temperatura_inicial_original = self.calentador.temperatura_liquido_inicial
        temperaturas_iniciales = [random.normalvariate(10, 5) for _ in range(5)]
        
        for temperatura_inicial in temperaturas_iniciales:
            self.calentador.temperatura_liquido_inicial = temperatura_inicial
            plt.plot(range(self.calentador.tiempo_objetivo), self.calentador.aumento_temperatura_con_perdida(), label=f"{temperatura_inicial:.2f} °C" , linestyle="-")
            
        self.calentador.temperatura_liquido_inicial = temperatura_inicial_original
        
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
        temperaturas_ambiente_original = self.calentador.temperatura_ambiente
        temperaturas_ambiente = [random.uniform(-20, 50) for _ in range(8)]
        
        for temperatura_ambiente in temperaturas_ambiente:
            self.calentador.temperatura_ambiente = temperatura_ambiente
            plt.plot(range(self.calentador.tiempo_objetivo), self.calentador.aumento_temperatura_con_perdida(), label=f"{temperatura_ambiente:.2f} °C" , linestyle="-")
        
        self.calentador.temperatura_ambiente = temperaturas_ambiente_original
        
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
        tension_original = self.calentador.tension
        tensiones = [random.normalvariate(220, 40) for _ in range(5)] 

        for tension in tensiones:
            self.calentador.tension = tension
            self.calentador.potencia = tension**2 / self.calentador.resistencia
            plt.plot(range(self.calentador.tiempo_objetivo), self.calentador.aumento_temperatura_con_perdida(), label=f"{tension:.2f} V" , linestyle="-")
        
        self.calentador.tension = tension_original
        
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
        raise NotImplementedError("Tp5 E")

    def tp6(self) -> None:
        """
        """
        raise NotImplementedError("Tp6")


if __name__ == '__main__':
    a = App()
    
    agua = Liquido(
        nombre="Agua",
        densidad=1, 
        calor_especifico=4.186,
    )
    print(agua)
    a.setLiquido(agua)
    
    print("-"*10)
    
    telgopor = Material(
        nombre="Telgopor",
        conductividad_térmica=0.035,
    )
    print(telgopor)
    a.setMaterial(telgopor)
    
    print("-"*10)
    
    cilindro = Recipiente(
        altura=6.36619, 
        diametro=10, 
        material=telgopor, 
        espesor_aislante=0.01, 
        liquido=agua
    )
    print(cilindro)
    a.setRecipiente(cilindro)
    
    print("-"*10)
    
    calentador = Calentador(
        temperatura_liquido_inicial=30,
        temperatura_liquido_final=100,
        temperatura_ambiente=30,
        tiempo_objetivo=300,
        recipiente=cilindro,
        tension=220,
    )
    calentador.tension
    a.setCalentador(calentador)
    print(calentador)
    
    print("+"*10)
    print("+"*10)
    
    
    a.tp1_a()
    print("-"*10)
    a.tp1_b()
    print("-"*10)
    a.tp2()
    print("-"*10)
    a.tp3()
    a.tp4()
    a.tp5_a()
    a.tp5_b()
    a.tp5_c()
    a.tp5_d()
    
    a.tp5_e()
    a.tp6()