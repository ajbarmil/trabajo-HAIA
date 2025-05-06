from genetico import Hiperparametros, AlgoritmoGenetico
import csv
from time import time

with open("resultados/tamaño.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Tamaño", "Mejor", "Media", "Tiempo"])
    for tamaño in [50, 100, 150, 200]:
        for _ in range(5):
            hp = Hiperparametros(tamaño=tamaño, seleccion_n=int(tamaño * 0.2), seleccion_m=int(tamaño * 0.2))
            ag = AlgoritmoGenetico(hp)

            media_mejor, media_media, media_tiempo = 0, 0, 0
            t0 = time()
            for _ in range(50):
                mejor, media = ag.iterar()
            media_mejor += mejor
            media_media += media
            media_tiempo += time() - t0

        writer.writerow([tamaño, round(media_mejor / 5, 3), round(media_media / 5, 3), round(media_tiempo, 2)])

print("Tamaño hecho")

with open("resultados/partidas.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Partidas", "Mejor", "Media", "Tiempo"])
    for partidas in [10, 20, 30]:
        for _ in range(5):
            hp = Hiperparametros(partidas=partidas)
            ag = AlgoritmoGenetico(hp)

            media_mejor, media_media, media_tiempo = 0, 0, 0
            t0 = time()
            for _ in range(50):
                mejor, media = ag.iterar()
            media_mejor += mejor
            media_media += media
            media_tiempo += time() - t0

        writer.writerow([partidas, round(media_mejor / 5, 3), round(media_media / 5, 3), round(media_tiempo, 2)])

print("Partidas hecho")

with open("resultados/mutate_prob.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Mutate_prob", "Mejor", "Media", "Tiempo"])
    for mutate_prob in [0.1, 0.2, 0.3, 0.4]:
        for _ in range(5):
            hp = Hiperparametros(mutate_prob=mutate_prob)
            ag = AlgoritmoGenetico(hp)

            media_mejor, media_media, media_tiempo = 0, 0, 0
            t0 = time()
            for _ in range(50):
                mejor, media = ag.iterar()
            media_mejor += mejor
            media_media += media
            media_tiempo += time() - t0

        writer.writerow([mutate_prob, round(media_mejor / 5, 3), round(media_media / 5, 3), round(media_tiempo, 2)])

print("Prob hecho")

with open("resultados/mutate_var.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Mutate_var", "Mejor", "Media", "Tiempo"])
    for mutate_var in [0.1, 0.2, 0.3, 0.4]:
        for _ in range(5):
            hp = Hiperparametros(mutate_var=mutate_var)
            ag = AlgoritmoGenetico(hp)

            media_mejor, media_media, media_tiempo = 0, 0, 0
            t0 = time()
            for _ in range(50):
                mejor, media = ag.iterar()
            media_mejor += mejor
            media_media += media
            media_tiempo += time() - t0

        writer.writerow([mutate_var, round(media_mejor / 5, 3), round(media_media / 5, 3), round(media_tiempo, 2)])

print("Var hecho")

with open("resultados/seleccion_m.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Seleccion_m", "Mejor", "Media", "Tiempo"])
    for seleccion_m in [10, 20, 30, 40]:
        for _ in range(5):
            hp = Hiperparametros(seleccion_m=seleccion_m)
            ag = AlgoritmoGenetico(hp)

            media_mejor, media_media, media_tiempo = 0, 0, 0
            t0 = time()
            for _ in range(50):
                mejor, media = ag.iterar()
            media_mejor += mejor
            media_media += media
            media_tiempo += time() - t0

        writer.writerow([seleccion_m, round(media_mejor / 5, 3), round(media_media / 5, 3), round(media_tiempo, 2)])

print("M hecho")

with open("resultados/seleccion_n.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Seleccion_n", "Mejor", "Media", "Tiempo"])
    for seleccion_n in [10, 20, 30, 40]:
        for _ in range(5):
            hp = Hiperparametros(seleccion_n=seleccion_n)
            ag = AlgoritmoGenetico(hp)

            media_mejor, media_media, media_tiempo = 0, 0, 0
            t0 = time()
            for _ in range(50):
                mejor, media = ag.iterar()
            media_mejor += mejor
            media_media += media
            media_tiempo += time() - t0

        writer.writerow([seleccion_n, round(media_mejor / 5, 3), round(media_media / 5, 3), round(media_tiempo, 2)])

print("N hecho")
