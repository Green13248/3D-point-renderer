import pygame
bgcolor = (0, 0, 0) 
screen = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption('3D cube') 
screen.fill(bgcolor) 
cube = []
def render(x, y, z):
    FL = 75
    Px = (500/2) + (x*FL) / (FL+z)
    Py = (500/2) + (y*FL) / (FL+z)
    cube.append(Px)
    cube.append(Py)
    print(cube)
    pygame.draw.line(screen, (255, 255, 255), 
                 [Px, Py], 
                 [Px + 1, Py + 1], 5)
    pygame.display.flip()
render(10, 10, 10)
render(100, 10, 10)
render(100, 100, 10)
render(10, 100, 10)
render(10, 10, 100)
render(100, 10, 100)
render(100, 100, 100)
render(10, 100, 100)

