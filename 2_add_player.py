#Workshop Pygame Mauricio Castillo
import pygame
pygame.init()
#Dimensiones de la ventana
widthWindows = 648
heightWindows = 480
windows = pygame.display.set_mode((widthWindows, heightWindows))
pygame.display.set_caption('Estetica INPUT')
character = pygame.image.load("player.png")
backgroun = pygame.image.load("bg.jpg")
# defeinicion de color de fonso
colorFondo = pygame.Color(254, 254, 254)

#definicion de variables
x = 10
y = 10
width = 40
height = 40
speed = 5
run = True


def game_windows():

    pygame.time.delay(50)
    # Cambio de fondo por una imagen
    windows.blit(backgroun, (0, 0))
    #
    # Cambio de cubo rojo A una imagen
    windows.blit(character, (x, y, width, height))

    # Esta funcionalidad acutaliza constatemente los elementos en pantalla
    pygame.display.update()


while run:
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

    game_windows()


pygame.quit()


