import pygame
import numpy
import scipy
from sys import exit

pygame.init()

width = 1920
height = 1080
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("physics demo")
clock = pygame.time.Clock()
running  = True

#initialization
def gridLines(startPos,endPos):
    pygame.draw.line(screen,"grey75",startPos,endPos,2)

gridSpacing = 100
gridSize = [width,height]

def grid():
    for x in range(int(cameraOffset.x) % gridSpacing,gridSize[0],gridSpacing):
        gridLines((x,0),(x,gridSize[1])) 

    for y in range(int(cameraOffset.y) % gridSpacing,gridSize[1],gridSpacing):
        gridLines((0,y),(gridSize[0],y)) 

cameraOffset = pygame.Vector2(0,0)
isDragging = False
previousCameraPos = pygame.Vector2(0,0)
velocity = pygame.Vector2(0,0)
friction = 0.799

#text
textFont = pygame.font.SysFont("Arial",20,True)
commandSymbol = pygame.font.SysFont("Arial",50,True)
def drawText(text,font,colour,pos):
      img = font.render(text,True,colour)
      screen.blit(img,pos)

def drawCommandBar():
      pygame.draw.rect(screen,"gray9",(width-275,height-75,250,55))
     # pygame.draw.rect(screen,"grey80",(width-262.5,height-72.5,225,45))
      drawText(">/",commandSymbol,"gray9",(width-325,height-73.5))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                isDragging = True
                previousCameraPos = pygame.Vector2(event.pos)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                isDragging = False

        if event.type == pygame.MOUSEMOTION and isDragging:
                mousePos = pygame.Vector2(event.pos)
                velocity = mousePos - previousCameraPos
                cameraOffset += velocity
                previousCameraPos = mousePos
        if not isDragging:
              velocity *= friction
        if velocity.length() < 0.1:
                    velocity = pygame.Vector2(0,0)

        cameraOffset += velocity
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mousePos = pygame.mouse.get_pos()

    screen.fill("grey87")
    grid()
    drawCommandBar()
    drawText(str(mouse_x) + " , " + str(mouse_y),textFont,"gray9",(width-125,height-105))

    pygame.display.update()
    dt = clock.tick(60)