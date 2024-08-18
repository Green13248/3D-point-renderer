import pygame
import numpy

bgcolor = (0, 0, 0) 
  
screen = pygame.display.set_mode((500, 500)) 

pygame.display.set_caption('3D cube') 

screen.fill(bgcolor) 

pygame.display.flip()

FOV = 70
cube = []

def render(x, y, z):
    projectedx = x * FOV/FOV + z
    projectedy = y * FOV/FOV + z
    cube.append(x)
    cube.append(y)
    cube.append(z)
    print(cube)
    pygame.draw.line(screen, (255, 255, 255), 
                 [projectedx, projectedy], 
                 [projectedx + 1, projectedy + 1], 5)
    pygame.display.flip()

render(10, 10, 10)
render(100, 10, 10)
render(100, 100, 10)
render(10, 100, 10)
render(10, 10, 100)
render(100, 10, 100)
render(100, 100, 100)
render(10, 100, 100)
    
