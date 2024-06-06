from Particulas.clases.Simulacion import Simulacion

class App:
    def __init__(self):
        pass
    
    
    def main(self):
        #TODO:
        # 5) Cuando se encuentran suficientemente próximas, con cierta tolerancia, a otras partículas, previamente adheridas al conducto, también deben permanecer adheridas.
        # 6) La simulación se detiene cuando el crecimiento de las partículas alcanza una cierta distancia al centro, establecida previamente.
        # Se debe animar la simulación, con diversas escalas de tiempo.
        
        forma_conducto = input("Ingrese la forma del conducto (circular, cuadrada, rectangular): ")
        
        if forma_conducto not in ["circular", "cuadrada", "rectangular"]:
            raise ValueError("La forma del conducto debe ser circular, cuadrada o rectangular")
        
        if forma_conducto == "circular":
            dimensiones_conducto = [int(input("Ingrese el radio del conducto (entre 1 y 1000 mm): "))]
        elif forma_conducto == "cuadrada":
            dimensiones_conducto = [int(input("Ingrese el lado del conducto (entre 1 y 1000 mm): "))] * 2
        elif forma_conducto == "rectangular":
            dimensiones_conducto = [int(x) for x in input("Ingrese las dimensiones del conducto separadas por coma (entre 1 y 1000 mm). Ej: <10,25>: ").split(",")]
        
        lado_particula = int(input("Ingrese el lado de la partícula (entre 1 y 10 mm): "))
        
        tolerancia = int(input("Ingrese la tolerancia de adherencia (en mm): "))
        
        distancia_final = int(input("Ingrese la distancia final al centro (en mm): "))
        
        forma_conducto = "circular"
        dimensiones_conducto = [100]
        lado_particula = 5
        distancia_final = 100

        simulacion = Simulacion(forma_conducto, dimensiones_conducto, lado_particula, distancia_final)
        simulacion.ejecutar()