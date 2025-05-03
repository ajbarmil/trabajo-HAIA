class PartidaConecta4:
    MAXIMO_COLUMNAS = 6

    def __init__(self, agente0, agente1):
        self.agente0 = agente0
        self.agente1 = agente1
        self.turno_actual = 0  # si es 0, le toca al agente0; si es 1, le toca al agente 1
        self.tablero = {}
        self.estado = 2  # códigos: 0 si ha ganado el agente0, 1 si ha ganado el agente1, 2 si la partida sigue, 3 si hay un empate

        for i in range(7):
            self.tablero[i + 1] = []  # 0 para el agente0, 1 para el agente1

    def siguiente_turno(self):
        if self.estado == 2:  # si nadie ha ganado aún...
            # elegir agente que va a jugar
            if self.turno_actual == 0:
                agente_elegido = self.agente0
            else:
                agente_elegido = self.agente1

            # hacer que el agente haga una jugada
            jugada_invalida = True
            i = 0
            while jugada_invalida:
                jugada = agente_elegido.hacer_jugada(self.tablero)
                if len(self.tablero[jugada]) < self.MAXIMO_COLUMNAS:
                    self.tablero[jugada].append(self.turno_actual)  # "inserta" la ficha
                    jugada_invalida = False

            # comprobar si ha ganado alguien
            columna_jugada = jugada
            fila_jugada = len(self.tablero[jugada]) - 1
            if self.comprobar_victoria(fila_jugada, columna_jugada, self.turno_actual):
                self.estado = self.turno_actual

            # comprobar si ha empatado alguien
            if self.estado not in (0, 1):
                tablero_completo = True
                for i in self.tablero:
                    if len(self.tablero[i]) < self.MAXIMO_COLUMNAS:
                        tablero_completo = False
                        break
                if tablero_completo:
                    self.estado = 3

            # nuevo turno
            self.turno_actual = (self.turno_actual + 1) % 2

        return self.estado

    def comprobar_victoria(self, fila, columna, jugador):
        direcciones = [(0, 1), (1, 0), (1, 1), (1, -1)]  # horiz, vert, diag abajo derecha, diag arriba derecha
        for dx, dy in direcciones:
            conteo = 1
            for sentido in [1, -1]:
                x, y = fila, columna
                while True:
                    x += dx * sentido
                    y += dy * sentido
                    if 1 <= y <= 7 and 0 <= x < len(self.tablero[y]):
                        if self.tablero[y][x] == jugador:
                            conteo += 1
                        else:
                            break
                    else:
                        break
            if conteo >= 4:
                return True
        return False

    def dibujar_tablero(self):
        filas = []
        for fila in reversed(range(self.MAXIMO_COLUMNAS)):
            linea = ""
            for columna in range(1, 8):
                if fila < len(self.tablero[columna]):
                    ficha = str(self.tablero[columna][fila])
                else:
                    ficha = "·"
                linea += ficha
            filas.append(linea)
        return "\n".join(filas)


def simular_partida(agente0, agente1):
    p = PartidaConecta4(agente0, agente1)

    while p.estado == 2:
        p.siguiente_turno()

    return p.estado

