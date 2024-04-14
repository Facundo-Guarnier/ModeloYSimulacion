# import matplotlib.pyplot as plt

# class CalentadorAgua:
#     def __init__(self, resistencia:float, potencia:float, tiempo:int, voltaje:float, temperatura_inicial:float, temperatura_final:float, temperatura_ambiente:float, recipiente):
#         self.resistencia = resistencia  # en ohms
#         self.potencia = potencia  # en watts
#         self.tiempo = tiempo  # en minutos
#         self.voltaje = voltaje  # en voltios
#         self.temperatura_inicial = temperatura_inicial  # en °C
#         self.temperatura_final = temperatura_final
#         self.temperatura_ambiente = temperatura_ambiente  # en °C
#         self.recipiente:Recipiente = recipiente



#     def graficar_aumento_temperatura(self, perder_calor: bool) -> None:
#         temperaturas = []
#         temperatura_agua = self.temperatura_inicial
#         for segundo in range(self.tiempo):
#             cantidad_calor = self.potencia
#             masa_agua = self.recipiente.calcular_capacidad()
#             calor_especifico_agua = 4.18
#             cambio_temperatura = cantidad_calor / (masa_agua * calor_especifico_agua)
            
#             if perder_calor:
#                 if temperatura_agua > self.temperatura_ambiente:
#                                  #!               dt                                       A                                        k
#                     perdida_calor = (temperatura_agua - self.temperatura_ambiente) * self.recipiente.calcular_area() * self.recipiente.coeficiente_termico
#                     cambio_temperatura -= perdida_calor / (masa_agua * calor_especifico_agua)   #! Q
            
#             temperatura_agua += cambio_temperatura
#             temperaturas.append(temperatura_agua)

#         tiempo_segundos = range(self.tiempo)
#         plt.plot(tiempo_segundos, temperaturas)
#         plt.title('Aumento de temperatura del agua')
#         plt.xlabel('Tiempo (segundos)')
#         plt.ylabel('Temperatura del agua (°C)')
#         plt.ylim(0, 100)
#         plt.grid(True)
#         plt.show()



# class Recipiente:
#     def __init__(self, altura:float, diametro:float, coeficiente_termico: float) -> None:
#         self.altura = altura
#         self.diametro = diametro
#         self.coeficiente_termico = coeficiente_termico
        

#     def calcular_capacidad(self) -> float:
#         """
#         Calcular la capacidad del recipiente en base a sus dimensiones
#         """ 
#         radio = self.diametro / 2
#         capacidad = 3.14159 * (radio ** 2) * self.altura  # Volumen de un cilindro
#         return capacidad

#     def calcular_area(self) -> float:
#         """
#         Calcular el área superficial del recipiente
#         """
#         return 2 * 3.14 * (self.calcular_capacidad() ** 0.5) * (self.calcular_capacidad() ** 0.5 + 1)


# if __name__ == '__main__':
#     recipiente = Recipiente(
#         altura=12.73,
#         diametro=10,
#         coeficiente_termico=0.035
#     )
    
#     calentadorAgua = CalentadorAgua(
#         resistencia=99.25,
#         potencia=487.7,
#         tiempo=300,
#         voltaje=220,
#         temperatura_inicial=30,
#         temperatura_final=100,
#         temperatura_ambiente=20,
#         recipiente=recipiente
#     )

#     calentadorAgua.graficar_aumento_temperatura(perder_calor=False)
#     calentadorAgua.graficar_aumento_temperatura(perder_calor=True)