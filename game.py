import pygame;
import sys;

WIDTH = 600
ROWS = 25
pygame.init()
window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")

#Frame rate controls
clock = pygame.time.Clock();
FPS = 60;

# Colors
WHITE = (255, 255, 255) #Some colors for the grid
BLACK = (0, 0, 0) 
GREY = (128, 128, 128)
GREEN = (0, 255, 0)   # starting point
RED = (255, 0, 0)     # ending point
BLUE = (0, 0, 255)    # path visited


#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    window.fill(WHITE)  

    pygame.display.flip()


    clock.tick(FPS) #60 FPS make sure
pygame.quit()
sys.exit()