import threading
from time import sleep

def servir_cafe():
    for i in range(5):  # Simula servir café para 5 clientes
        print(f"Camarero: Sirviendo café {i + 1}")
        sleep(1)  # Tiempo necesario para servir un café
    print("Camarero: Terminó de servir todos los cafés")

def poner_tostadas():
    for i in range(5):  # Simula poner tostadas para 5 clientes
        print(f"Camarero: Poniendo tostada {i + 1}")
        sleep(1.5)  # Tiempo necesario para preparar una tostada
    print("Camarero: Terminó de poner todas las tostadas")

def hacer_tortilla():
    for i in range(5):  # Simula hacer tortillas para 5 clientes
        print(f"Camarero: Haciendo tortilla {i + 1}")
        sleep(2)  # Tiempo necesario para hacer una tortilla
    print("Camarero: Terminó de hacer todas las tortillas")

if __name__ == "__main__":
    # Crear los hilos para cada tarea
    hilo_cafe = threading.Thread(target=servir_cafe)
    hilo_tostadas = threading.Thread(target=poner_tostadas)
    hilo_tortilla = threading.Thread(target=hacer_tortilla)
    
    hilo_cafe.start()
    hilo_tostadas.start()
    hilo_tortilla.start()
