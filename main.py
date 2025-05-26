import pygame

# ideias
#
# talvez um state machine que indique o que tem em cada espaço do grid ex
# digamos um ENUM, só pra exemplificar
# enum GRID_STATE {EMPTY,PLAYER,WALL,BOMB}
#
# if grid[x][y] = GRID_STATE(0): branco
# if grid[x][y] = GRID_STATE(1): playersprite
# if grid[x][y] = GRID_STATE(2): wallsprite
# if grid[x][y] = GRID_STATE(3): bombsprite, bomb_logic()
#
# pseudo pra caralho, pode ser uma ideia muito burra
# talvez em python possa ser usado um dict, dict { 1: vazio, 2: player, etc}
#
# fiz um sistema de grid olhando uns exemplos na internet, no momento funciona pro clique
#
# se acharem que não dá pra usar, mudem tudo


pygame.init()
screen = pygame.display.set_mode((510, 510), vsync=True)
clock = pygame.time.Clock()
running = True

# tudo aqui deveria ser em caps pq sao constantes, mas eu ja escrevi tudo em minusculo... que problemão.
box_width = 40
box_height = 40
margin = 9

# constantes de cores
white = (255, 255, 255)
green = (0, 255, 0)

columns = list(range(11))
rows = list(range(11))

grid = [[0 for x in range(11)] for y in range(11)] # criando grid, se aumentar colums/rows tem que mudar aqui
grid[1][5] = 1 # teste pra colorir 1/5

pygame.display.set_caption("Grid com valores")

# main loop de render
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # .QUIT = X da janela
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # pega o clique
            x,y = pygame.mouse.get_pos()
            colclick = x // (box_width + margin)
            rowclick = y // (box_height + margin) # calcula em qual row/coluna foi clicado
            print(f"Click: {x},{y} Col: {colclick} Row: {rowclick} GridValue: {grid[rowclick][colclick]}")
            if grid[rowclick][colclick] == 0: # muda o valor no grid onde teve o clique
                grid[rowclick][colclick] = 1
            else: grid[rowclick][colclick] = 0

    for row in rows:
        for column in columns:
            x = margin + column * (box_width + 5)
            y = margin + row * (box_height + 5) # posicao, vai mudando em toda iteracao
            if grid[row][column] == 1:
                pygame.draw.rect(screen, green, (x, y, box_width, box_height)) # reacao ao clique
                continue
            pygame.draw.rect(screen, white, (x, y, box_width, box_height))
    # esse jeito de desenhar o grid acaba se peidando quando o tamanho do grid é muito grande.
    # pygame meio que te força a fazer esses códigos que ficam se repetindo a fu

    clock.tick(60) # limita em 60 fps

    pygame.display.flip() # isso é o que atualiza a tela, se tirar vai ficar tudo preto.

pygame.quit()