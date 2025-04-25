import random
import numpy as np

TAMAÑO = (42, 20, 7)


class Red:
    def __init__(self):
        self.pesos = [2 * np.random.random((c1, c2)) - 1 for c1, c2 in zip(TAMAÑO[:-1], TAMAÑO[1:])]
        self.sesgos = [2 * np.random.random(c1) - 1 for c1 in TAMAÑO[1:]]

    def predict(self, x):
        result = x
        for i, (peso, sesgo) in enumerate(zip(self.pesos, self.sesgos)):
            result = result @ peso + sesgo

            if i != len(self.pesos) - 1:
                result = np.maximum(result, 0)
            else:
                exps = np.exp(result)
                result = exps / exps.sum()
        return result


class Agente:
    def __init__(self):
        self.red = Red

    def hacer_jugada(self, tablero):
        probabilidades = self.red.predict(tablero)
        # insertar elección sobre el vector [del 0 al 7]
        return None
