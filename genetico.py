from dataclasses import dataclass, field
import random
import numpy as np
from csv import writer
from time import time
from argparse import ArgumentParser


@dataclass
class Hiperparametros:
    partidas: int = 10
    tamaño: int = 100
    mutate_prob: float = 0.2
    mutate_var: float = 0.2
    seleccion_m: int = 30
    seleccion_n: int = 30


def simular(individuo):
    return np.random.random()


@dataclass
class AlgoritmoGenetico:
    hiperparametros: Hiperparametros = field(default_factory=Hiperparametros)
    poblacion: list = field(init=False)

    # TODO:
    def crear_individuo(self):
        return np.random.random(10)

    def crear_poblacion(self):
        self.poblacion = []
        for _ in range(self.hiperparametros.tamaño):
            individuo = self.crear_individuo()
            self.poblacion.append((self.fitness(individuo), individuo))

    def __post_init__(self):
        self.crear_poblacion()

    # TODO:
    def fitness(self, individuo):
        return sum(simular(individuo) for _ in range(self.hiperparametros.partidas)) / self.hiperparametros.partidas

    # TODO:
    def mutate(self, individuo):
        return individuo

    # TODO:
    def crossover(self, individuo1, individuo2):
        return individuo1, individuo2

    def seleccion(self):
        muestra = random.sample(self.poblacion, self.hiperparametros.seleccion_m)
        muestra = sorted(muestra, key=lambda x: x[0])
        muestra = list(map(lambda x: x[1], muestra))
        return muestra[: self.hiperparametros.seleccion_n]

    def criba(self):
        self.poblacion = sorted(self.poblacion, key=lambda x: x[0])[: self.hiperparametros.tamaño]

    def iterar(self):
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
