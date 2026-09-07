from turtle import width
from algs import *
import pygame;
import sys, time;
from tile import Tile;
from colors import WHITE, BLACK, GREY, GREEN, RED, BLUE;

WIDTH = 600
ROWS = 25
pygame.init()
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")

#Frame rate controls
clock = pygame.time.Clock();
FPS = 60;

#Special tiles
start = None
end = None

#Grid making logic
def makeGrid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            tile = Tile(i, j, gap, rows)
            grid[i].append(tile)
    return grid

def drawGridLines(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for tile in row:
            tile.draw(win)
    drawGridLines(win, rows, width)
    pygame.display.update()

def getClickedPos(pos, rows, width): #Translates where I've clicked to the closest grid tile
    gap = width // rows
    y, x = pos
    return y // gap, x // gap  

def updateAllAnimations(grid):
    for row in grid:
        for tile in row:
            tile.updateAnimation()

def updateNeighborsForAll(grid):
    for row in grid:
        for tile in row:
            tile.updateNeighbors(grid)

#Game loop
grid = makeGrid(ROWS, WIDTH)
updateNeighborsForAll(grid)
running = True
while running:
    #Event getting in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = getClickedPos(pos, ROWS, WIDTH)
        tile = grid[row][col]
        if not start and tile != end:
            start = tile
            tile.startBarrierGrowth(GREEN)
        elif not end and tile != start:
            end = tile
            tile.startBarrierGrowth(RED)
        elif tile != start and tile != end and not tile.isBarrier():
            tile.startBarrierGrowth()
            grid[row - 1][col].updateNeighbors(grid)
            grid[row + 1][col].updateNeighbors(grid)
            grid[row][col - 1].updateNeighbors(grid)
            grid[row][col + 1].updateNeighbors(grid)

    elif pygame.mouse.get_pressed()[2]:
        pos = pygame.mouse.get_pos()
        row, col = getClickedPos(pos, ROWS, WIDTH)
        tile = grid[row][col]
        tile.reset()
        if tile == start:
            start = None
        elif tile == end:
            end = None
        grid[row - 1][col].updateNeighbors(grid)
        grid[row + 1][col].updateNeighbors(grid)
        grid[row][col - 1].updateNeighbors(grid)
        grid[row][col + 1].updateNeighbors(grid)

    elif pygame.key.get_pressed()[pygame.K_SPACE]:
        if start and end:
            visited = dfs(start, end)
            for tile in visited:
                if tile != start and tile != end:
                    tile.startBarrierGrowth(BLUE)

            

    #Draw grids out
    updateAllAnimations(grid)
    draw(win, grid, ROWS, WIDTH)
    
    pygame.display.flip()


    clock.tick(FPS) #60 FPS make sure
pygame.quit()
sys.exit()