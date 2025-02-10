import threading
import time
from queue import Queue


class CajaRegistradora(threading.Thread):
    def __init__(self, id_caja, cola_clientes):
        super().__init__()
        self.id_caja = id_caja
        self.cola_clientes = cola_clientes
        self.clientes_atendidos = 0

    def run(self):
        while True:
            cliente = self.cola_clientes.get()  # Obtener un cliente de la cola
            if cliente is None:
                break  # No hay más clientes, la caja se cierra
            tiempo_atencion = cliente['tiempo_atencion']
            time.sleep(tiempo_atencion)  # Simular el tiempo de atención
            self.clientes_atendidos += 1
            print(f"Caja {self.id_caja} atendió a un cliente en {tiempo_atencion:.2f} segundos.")
            self.cola_clientes.task_done()

    def obtener_clientes_atendidos(self):
        return self.clientes_atendidos


def simular_supermercado(num_cajas, clientes):
    # Crear una cola compartida para los clientes
    cola_clientes = Queue()

    # Crear las cajas registradoras (hilos)
    cajas = [CajaRegistradora(i + 1, cola_clientes) for i in range(num_cajas)]

    # Iniciar las cajas
    for caja in cajas:
        caja.start()

    # Agregar los clientes a la cola
    for cliente in clientes:
        cola_clientes.put(cliente)

    # Esperar a que todos los clientes sean atendidos
    cola_clientes.join()

    # Finalizar los hilos de las cajas
    for _ in cajas:
        cola_clientes.put(None)  # Señal para terminar cada hilo

    for caja in cajas:
        caja.join()

    # Mostrar el resumen de la simulación
    total_tiempo = sum(cliente['tiempo_atencion'] for cliente in clientes)
    print(f"\nTiempo total de atención de todos los clientes: {total_tiempo:.2f} segundos.")
    for caja in cajas:
        print(f"Caja {caja.id_caja} atendió a {caja.obtener_clientes_atendidos()} clientes.")


# Simulación con 3 cajas y 10 clientes
clientes = [{'id': i, 'tiempo_atencion': (i % 5 + 1)} for i in range(1, 11)]
simular_supermercado(3, clientes)
