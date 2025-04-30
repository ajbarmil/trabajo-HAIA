import random

class AgenteRandom:
    def hacer_jugada(self, tablero):
        return random.randint(1, len(tablero))