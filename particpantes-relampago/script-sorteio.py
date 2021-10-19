import os
import random
from time import sleep

inscritos = [
]

print("###INSCRITOS##")
novos_inscritos=[]
for index,item in enumerate(inscritos):
    i = f"{index+1}:{item}"
    print(i)
    novos_inscritos.append(i)
clear = lambda: os.system('clear')

input("\nPressione enter para sortear")
clear()

input("\nAjustando index...")
random.shuffle(novos_inscritos)
clear()

input("Refatorando orde index..")
random.shuffle(novos_inscritos)
clear()


for index,item in enumerate(novos_inscritos):
    print(item)
    if index==:print('############')
