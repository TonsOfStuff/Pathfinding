import pygame
from colors import WHITE, BLACK, GREY, GREEN, RED, BLUE

class Tile:
    def __init__(self, row, col, width, totalRows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.totalRows = totalRows
        self.isGrowing = False
        self.growSize = 0        
        self.growSpeed = 6

    def getPos(self):
        return self.row, self.col

    def isBarrier(self):
        return self.color == BLACK

    def startBarrierGrowth(self, color=BLACK):
        self.color = color
        self.isGrowing = True
        self.growSize = 0

    def makeBarrier(self): #No animation version just in case I need it
        self.color = BLACK
        self.isGrowing = False
        self.growSize = self.width

    def reset(self):
        self.color = WHITE
        self.isGrowing = False
        self.growSize = 0

    def updateAnimation(self):
        if self.isGrowing:
            self.growSize += self.growSpeed
            if self.growSize >= self.width:
                self.growSize = self.width
                self.isGrowing = False

    def draw(self, win):
        if self.isGrowing:
            #Centered square that'll grow
            offset = (self.width - self.growSize) // 2
            pygame.draw.rect(
                win, self.color,
                (self.x + offset, self.y + offset, self.growSize, self.growSize)
            )
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def updateNeighbors(self, grid):
        self.neighbors = []
        # Down, Up, Right, Left — skip barriers
        if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].isBarrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].isBarrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].isBarrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].isBarrier():
            self.neighbors.append(grid[self.row][self.col - 1])