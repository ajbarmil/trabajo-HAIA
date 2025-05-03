from copy import Error
import numpy as np

TAMAÑO = (56, 20, 7)


class Red:
    pesos: list[np.ndarray]
    sesgos: list[np.ndarray]

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
    def __init__(self, init_red=True):
        self.red = Red()
        if init_red:
            self.red.pesos = [2 * np.random.random((c1, c2)) - 1 for c1, c2 in zip(TAMAÑO[:-1], TAMAÑO[1:])]
            self.red.sesgos = [2 * np.random.random(c1) - 1 for c1 in TAMAÑO[1:]]
        else:
            self.red.pesos = []
            self.red.sesgos = []

    def hacer_jugada(self, tablero):
        array = np.zeros((8, len(tablero))) + 0.5
        for j, columna in enumerate(tablero):
            array[columna, j] = columna

        odds = self.red.predict(np.ravel(array) - 0.5)
        odds = odds * (np.asarray(list(len(columna) for columna in tablero.values())) < 5)
        exps = np.exp(odds)
        probabilidades = exps / exps.sum()
        return np.random.choice(len(tablero), p=probabilidades) + 1
