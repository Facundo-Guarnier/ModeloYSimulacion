from Particulas.clases.Simulacion import Simulacion

class App:
    def __init__(self):
        pass
    
    
    def main(self) -> None:
        
        #! Forma del conducto
        forma_conducto = input("Ingrese la forma del conducto (circular, cuadrada, rectangular): ")
        if forma_conducto not in ["circular", "cuadrada", "rectangular"]:
            raise ValueError("La forma del conducto debe ser circular, cuadrada o rectangular")
        
        if forma_conducto == "circular":
            dimensiones_conducto = [int(input("Ingrese el diametro del conducto (entre 10 y 1000 mm): "))]
            
        elif forma_conducto == "cuadrada":
            dimensiones_conducto = [int(input("Ingrese el lado del conducto (entre 10 y 1000 mm): "))] * 2
            
        elif forma_conducto == "rectangular":
            dimensiones_conducto = [int(input("Ingrese el primer lado del conducto(entre 10 y 1000 mm): "))]
            dimensiones_conducto.append(int(input("Ingrese el segundo lado del conducto(entre 10 y 1000 mm): ")))
        
        if any([dimension < 10 or dimension > 1000 for dimension in dimensiones_conducto]):
            raise ValueError("Las dimensiones del conducto deben estar entre 10 y 1000 mm")
        
        #! Tamaño de la partícula
        lado_particula = int(input("Ingrese el lado de la partícula (entre 1 y 10 mm): "))
        if lado_particula < 1 or lado_particula > 10:
            raise ValueError("El lado de la partícula debe estar entre 1 y 10 mm")
        
        #! Distancia final al centro
        tolerancia = int(input("Ingrese la tolerancia de adherencia (entre 1 y 10 mm): "))
        if tolerancia < 1 or tolerancia > 10:
            raise ValueError("La tolerancia de adherencia debe estar entre 1 y 10 mm")
        
        #! Distancia final al centro
        distancia_final = int(input("Ingrese la distancia final al centro (entre 10 y 100 mm): "))
        if distancia_final < 10 or distancia_final > 100:
            raise ValueError("La distancia final al centro debe estar entre 1 y 100 mm")
        
        #! Velocidad de la simulacion
        velocidad = int(input("Ingrese la velocidad de la simulación (entre 30 y 1000): "))
        if velocidad < 30 or velocidad > 1000:
            raise ValueError("La velocidad de la simulación debe estar entre 30 y 1000")
        
        # forma_conducto = "cuadrada"
        # # forma_conducto = "circular"
        # dimensiones_conducto = [300]
        # lado_particula = 10
        # distancia_final = 25
        # tolerancia = 0
        # velocidad = 600
        
        simulacion = Simulacion(
            forma=forma_conducto, 
            dimensiones=dimensiones_conducto, 
            lado_particula=lado_particula, 
            distancia_final=distancia_final, 
            tolerancia=tolerancia,
            velocidad=velocidad
        )
        simulacion.ejecutar()