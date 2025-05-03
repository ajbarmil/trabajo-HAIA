from dataclasses import dataclass, field
import random
import numpy as np
from conecta4 import simular_partida
from agentes.agente_generico import Agente


@dataclass
class Hiperparametros:
    partidas: int = 5
    tamaño: int = 20
    mutate_prob: float = 0.2
    mutate_var: float = 0.2
    seleccion_m: int = 5
    seleccion_n: int = 5


@dataclass
class AlgoritmoGenetico:
    hiperparametros: Hiperparametros = field(default_factory=Hiperparametros)
    poblacion: list = field(default_factory=list)

    def crear_individuo(self):
        return Agente()

    def crear_poblacion(self):
        self.poblacion = []
        for _ in range(self.hiperparametros.tamaño):
            self.poblacion.append((0, self.crear_individuo()))

        for _, individuo in self.poblacion:
            self.poblacion.append((self.fitness(individuo), individuo))

    def __post_init__(self):
        self.crear_poblacion()

    def fitness(self, individuo):
        puntuacion = 0
        for _ in range(self.hiperparametros.partidas):
            _, rival = random.choice(self.poblacion)
            puntuacion += simular_partida(individuo, rival)
        return puntuacion / self.hiperparametros.partidas

    def mutate(self, individuo):
        for i, (pesos, sesgos) in enumerate(zip(individuo.red.pesos, individuo.red.sesgos)):
            probabilidad_mutacion = np.random.random(pesos.shape)
            mutacion = np.random.normal(0, 0.2, size=pesos.shape)
            individuo.red.pesos[i] = pesos + (probabilidad_mutacion < self.hiperparametros.mutate_prob) * mutacion

            probabilidad_mutacion = np.random.random(sesgos.shape)
            mutacion = np.random.normal(0, 0.2, size=sesgos.shape)
            individuo.red.sesgos[i] = sesgos + (probabilidad_mutacion < self.hiperparametros.mutate_prob) * mutacion

        return individuo

    def crossover(self, individuo1, individuo2):
        hijos = []

        for _ in range(2):
            factor = np.random.random()
            for i in range(len(individuo1.red.pesos)):
                hijo = Agente(init_red=False)
                hijo.red.pesos.append(factor * individuo1.red.pesos[i] + (1 - factor) * individuo2.red.pesos[i])
                hijo.red.sesgos.append(factor * individuo1.red.sesgos[i] + (1 - factor) * individuo2.red.sesgos[i])

                hijos.append(hijo)

        return hijos

    def seleccion(self):
        muestra = random.sample(self.poblacion, self.hiperparametros.seleccion_m)
        muestra = sorted(muestra, key=lambda x: x[0])
        muestra = list(map(lambda x: x[1], muestra))
        return muestra[: self.hiperparametros.seleccion_n]

    def criba(self):
        self.poblacion = sorted(self.poblacion, key=lambda x: x[0])[: self.hiperparametros.tamaño]

    def iterar(self):
        if not self.poblacion:
            self.crear_poblacion()
            mejor_fitness, _ = min(self.poblacion, key=lambda x: x[0])
            return mejor_fitness

        padres = self.seleccion()
        random.shuffle(padres)

        hijos = []
        i = 0
        while i < len(padres) - 1:
            padre1, padre2 = padres[i : i + 2]
            hijo1, hijo2 = self.crossover(padre1, padre2)

            hijo1 = self.mutate(hijo1)
            hijos.append((self.fitness(hijo1), hijo1))

            hijo2 = self.mutate(hijo2)
            hijos.append((self.fitness(hijo2), hijo2))

            i += 2

        self.poblacion.extend(hijos)
        self.criba()

        mejor_fitness, _ = min(self.poblacion, key=lambda x: x[0])
        return mejor_fitness


# if __name__ == "__main__":
#     parser = ArgumentParser()
#
#     parser.add_argument("--partidas", type=int, default=10)
#     parser.add_argument("--tamaño", type=int, default=100)
#     parser.add_argument("--mutate_prob", type=float, default=0.2)
#     parser.add_argument("--mutate_var", type=float, default=0.2)
#     parser.add_argument("--seleccion_m", type=int, default=30)
#     parser.add_argument("--seleccion_n", type=int, default=30)
#
#     args, _ = parser.parse_known_args()
#
#     t0 = time()
#     print(algoritmo_genetico(20, self.hiperparametros=Hiperparametros(**dict(args._get_kwargs()))))
#     print(f"{(time() - t0) / 60:.2f} minutos")
