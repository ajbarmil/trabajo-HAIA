from agentes.agente_random import AgenteRandom
from agentes.agente_minimax import AgenteMinimax
from conecta4 import PartidaConecta4

if __name__ == "__main__":
    ag1 = AgenteRandom()
    ag2 = AgenteMinimax()

    p = PartidaConecta4(ag1, ag2)

    while p.estado == 2:
        p.siguiente_turno()

    if p.estado == 0:
        print("¡Ha ganado el primer agente!")
    elif p.estado == 1:
        print("¡Ha ganado el segundo agente!")
    else:
        print("¡Ha sido un empate!")

    print("\nDibujo del tablero:")
    print(p.dibujar_tablero())