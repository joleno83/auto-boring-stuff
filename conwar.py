#! python3

# Conwayś Game of Life

import random, time, copy

WIDTH = 60
HEIGHT = 20

# Crie uma lista de listas oara as células:

nextCells = []

for x in range(WIDTH):
    column = []     #   Crie uma coluna nova.
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('H') #   Adicione uma célula viva.
        else:
            column.append('')  #   Add a dead cell.
        nextCells.append(column)    #   nextCells é uma lista de listas de colunas.
        
while True:     #   Loop principal do programa.
    print('\n\n\n\n\n')     #   Separe cada passo com linhas novas
    currentCells = copy.deepcopy(nextCells)
    
# Imprima currentCells na tela:

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') #    Imprime # ou espaço.
        print() #   Imprime linha nova no final da linha.
        
#   Calcula o próximo passo da célula baseado no passos atuais da célula:

    for x in range(WIDTH):
        for y in range(HEIGHT):
            #   Pega as coordenadas dos vizinhos:
            #   'WIDTH' garante leftCoord está sempre entre 0 e WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            
            # Conta o numero de celulas vivas vizinhas:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#' :
                numNeighbors += 1 # Vizinho do topo-esquerdo está vivo.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.
            
            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or
                numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.