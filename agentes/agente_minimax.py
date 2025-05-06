import copy
import math
import random

class AgenteMinimax:
    def __init__(self, profundidad=4, jugador=1):
        self.profundidad = profundidad
        self.jugador = jugador

    def hacer_jugada(self, tablero):
        mejor_valor = -math.inf
        mejor_jugada = None

        for col in range(1, 8):
            if len(tablero[col]) < 6:
                nuevo_tablero = copy.deepcopy(tablero)
                self.insertar_ficha(nuevo_tablero, col, self.jugador)
                valor = self.minimax(nuevo_tablero, self.profundidad - 1, False, self.jugador)
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_jugada = col

        return mejor_jugada if mejor_jugada is not None else random.randint(1, 7)

    def minimax(self, tablero, profundidad, es_maximizador, jugador_actual):
        if self.es_estado_terminal(tablero) or profundidad == 0:
            return self.evaluar_tablero(tablero, self.jugador)

        if es_maximizador:
            mejor_valor = -math.inf
            for col in range(1, 8):
                if len(tablero[col]) < 6:
                    nuevo_tablero = copy.deepcopy(tablero)
                    self.insertar_ficha(nuevo_tablero, col, jugador_actual)
                    valor = self.minimax(nuevo_tablero, profundidad - 1, False, 3 - jugador_actual)
                    mejor_valor = max(mejor_valor, valor)
            return mejor_valor
        else:
            peor_valor = math.inf
            for col in range(1, 8):
                if len(tablero[col]) < 6:
                    nuevo_tablero = copy.deepcopy(tablero)
                    self.insertar_ficha(nuevo_tablero, col, jugador_actual)
                    valor = self.minimax(nuevo_tablero, profundidad - 1, True, 3 - jugador_actual)
                    peor_valor = min(peor_valor, valor)
            return peor_valor

    def insertar_ficha(self, tablero, col, jugador):
        tablero[col].append(jugador)

    def es_estado_terminal(self, tablero):
        return self.hay_ganador(tablero, 1) or self.hay_ganador(tablero, 2) or all(len(tablero[c]) == 6 for c in tablero)

    def evaluar_tablero(self, tablero, jugador):
        if self.hay_ganador(tablero, jugador):
            return 100
        elif self.hay_ganador(tablero, 3 - jugador):
            return -100
        else:
            return self.contar_ventajas(tablero, jugador) - self.contar_ventajas(tablero, 3 - jugador)

    def hay_ganador(self, tablero, jugador):
        matriz = [[0 for _ in range(7)] for _ in range(6)]
        for c in range(1, 8):
            for f in range(len(tablero[c])):
                matriz[f][c - 1] = tablero[c][f]

        for f in range(6):
            for c in range(7):
                if c <= 3 and all(matriz[f][c + i] == jugador for i in range(4)):
                    return True
                if f <= 2 and all(matriz[f + i][c] == jugador for i in range(4)):
                    return True
                if c <= 3 and f <= 2 and all(matriz[f + i][c + i] == jugador for i in range(4)):
                    return True
                if c >= 3 and f <= 2 and all(matriz[f + i][c - i] == jugador for i in range(4)):
                    return True
        return False

    def contar_ventajas(self, tablero, jugador):
        score = 0
        matriz = [[0 for _ in range(7)] for _ in range(6)]
        for c in range(1, 8):
            for f in range(len(tablero[c])):
                matriz[f][c - 1] = tablero[c][f]

        for f in range(6):
            for c in range(7):
                lineas = [
                    [matriz[f][c + i] if c + i < 7 else 0 for i in range(4)],
                    [matriz[f + i][c] if f + i < 6 else 0 for i in range(4)],
                    [matriz[f + i][c + i] if f + i < 6 and c + i < 7 else 0 for i in range(4)],
                    [matriz[f + i][c - i] if f + i < 6 and c - i >= 0 else 0 for i in range(4)]
                ]
                for linea in lineas:
                    if linea.count(jugador) == 3 and linea.count(0) == 1:
                        score += 5
                    elif linea.count(jugador) == 2 and linea.count(0) == 2:
                        score += 2
        return score
