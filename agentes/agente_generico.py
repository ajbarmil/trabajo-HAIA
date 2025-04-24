import random

class Agente:
    def __init__(self):
        vectores = {}  # por iniciar, índices formato "numagenteXnumenemigo"

    def hacer_jugada(self, num_agente, num_enemigo):
        vector = self.vectores[f"{num_agente}X{num_enemigo}"]
        # insertar elección sobre el vector [del 0 al 7]
        return None