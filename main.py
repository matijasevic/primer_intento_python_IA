from random import randint
from posiciones import getPosRandom
from distorcionador import distorsionar

#Rangos de distorcion de entre 1 y 30 % de distorsion
iniDist = 1
finDist = 30

matriz_B = [
           [0, 0, 0,0, 0, 0,0, 0, 0,0], 
           [0, 0, 1,0, 0, 0,0, 0, 0,0],  
           [0, 0, 1,0, 0, 0,0, 0, 0,0], 
           [0, 0, 1,0, 0, 0,0, 0, 0,0], 
           [0, 0, 1,1, 1, 1,1, 0, 0,0],  
           [0, 0, 1,0, 0, 0,0, 1, 0,0],
           [0, 0, 1,0, 0, 0,0, 1, 0,0],
           [0, 0, 1,0, 0, 0,0, 1, 0,0], 
           [0, 0, 1,1, 1, 1,1, 0, 0,0],  
           [0, 0, 0,0, 0, 0,0, 0, 0,0]
           ]

#To print the matrix
print(matriz_B)

randomDistorsion = randint(iniDist,finDist)
print(randomDistorsion)

matriz_pos_random = getPosRandom(randomDistorsion)
print(matriz_pos_random)

matriz_distorsionada = distorsionar(matriz_pos_random,matriz_B)
print(matriz_distorsionada)

    
    

