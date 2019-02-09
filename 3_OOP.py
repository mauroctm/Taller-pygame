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
run = True


class Player(object):
    '''
    Declaracion de un objeto player
    '''
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5

    def draw(self, windows):
        # Cambio de cubo rojo A una imagen
        windows.blit(character, (self.x, self.y, self.width, self.height))




#mainloop
tank = Player(50, 50, 64, 64)

def game_windows():

    pygame.time.delay(50)
    # Cambio de fondo por una imagen
    windows.blit(backgroun, (0, 0))
    # Llamo a la funcionalidad de pintar el objeto player
    tank.draw(windows)

    # Esta funcionalidad acutaliza constatemente los elementos en pantalla
    pygame.display.update()


while run:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and tank.x > tank.speed:
        tank.x -= tank.speed

    if keys[pygame.K_RIGHT] and tank.x < widthWindows - tank.speed - tank.width:
        tank.x += tank.speed

    if keys[pygame.K_UP] and tank.y > tank.speed:
        tank.y -= tank.speed

    if keys[pygame.K_DOWN] and tank.y < heightWindows - tank.speed - tank.height:
        tank.y += tank.speed

    game_windows()


pygame.quit()


