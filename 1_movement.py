#Workshop Pygame Mauricio Castillo
import pygame

pygame.init()

#Dimensiones de la ventana
widthWindows = 648
heightWindows = 480
windows = pygame.display.set_mode((widthWindows, heightWindows))
pygame.display.set_caption('Movimientos INPUT')

# defeinicion de color de fondo
colorFondo = pygame.Color(254, 254, 254)
#definicion de variables
x = 10
y = 10
width = 40
height = 40
speed = 5
run = True
while run:
    pygame.time.delay(50)
    windows.fill(colorFondo)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed

    if keys[pygame.K_RIGHT] and x < widthWindows - speed - width:
        x += speed

    if keys[pygame.K_UP] and y > speed:
        y -= speed

    if keys[pygame.K_DOWN] and y < heightWindows - speed - height:
        y += speed

    pygame.draw.rect(windows, (250, 35, 90), (x, y, width, height))
    pygame.display.update()

pygame.quit()


