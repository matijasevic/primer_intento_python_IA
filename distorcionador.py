

def distorsionar(matriz_pos_random,matriz):
  #matriz_pos_random es una matriz con las posiciones a reemplazar
  #matriz es la matriz con 0 y 1 
  
  for e in matriz_pos_random:
    elemento = matriz[e[0]][e[1]]
    
    if elemento == 0:
      matriz[e[0]][e[1]] = 1
    elif elemento == 1:
      matriz[e[0]][e[1]] = 0

  return matriz