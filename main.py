from agentes.agente_random import AgenteRandom
from agentes.agente_minimax import AgenteMinimax
from agentes.agente_generico import Agente
from conecta4 import PartidaConecta4
from tqdm import tqdm
import pickle

if __name__ == "__main__":
    f = open("agentes/individuo.pkl", "rb")
    ag1 = pickle.load(f) # el agente 1 representa el mejor individuo genético
    f.close()

    ag2 = AgenteMinimax()

    estados_turno_ag1 = []

    for i in tqdm(range(500)):
        p = PartidaConecta4(ag1, ag2)

        while p.estado == 2:
            p.siguiente_turno()

        estados_turno_ag1.append(p.estado)

    estados_turno_ag2 = []

    for i in tqdm(range(500)):
        p = PartidaConecta4(ag2, ag1)

        while p.estado == 2:
            p.siguiente_turno()

        estados_turno_ag2.append(p.estado)


    # victorias de agente 1 en su turno
    # empates en turno de agente 1
    # victorias de agente 2 en su turno
    # empates en turno de agente 2
    # victorias totales de agente 1
    # empates totales

    vict_ag1_primer = estados_turno_ag1.count(0)
    empates_primer = estados_turno_ag1.count(3)
    vict_ag2_segun = estados_turno_ag2.count(0)
    empates_segun = estados_turno_ag2.count(3)

    print(f"Victorias con agente 1 siendo el primero: {vict_ag1_primer}")
    print(f"Empates con agente 1 siendo el primero: {empates_primer}")
    print(f"Victorias con agente 2 siendo el primero: {vict_ag2_segun}")
    print(f"Empates con agente 2 siendo el primero: {empates_segun}")

    print(f"Victorias totales de agente 1: {vict_ag1_primer + (500 - vict_ag2_segun - empates_segun)}")
    print(f"Empates totales: {empates_primer + empates_segun}")



    """
    if p.estado == 0:
        print("¡Ha ganado el primer agente!")
    elif p.estado == 1:
        print("¡Ha ganado el segundo agente!")
    else:
        print("¡Ha sido un empate!")

    print("\nDibujo del tablero:")
    print(p.dibujar_tablero())
    """