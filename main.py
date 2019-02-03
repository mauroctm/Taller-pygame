import pygame

pygame.init()
#Dimensiones de la ventana
widthVentana = 648
heightVentana = 480
ventana = pygame.display.set_mode((widthVentana , heightVentana ))
pygame.display.set_caption('Movimientos INPUT')

# Definicion de un colo
colorFondo = pygame.Color(254, 254, 254)
#definicion de variables
x = 10
y = 10
width = 40
height = 40
velocida = 5
run = True
while run:
    pygame.time.delay(50)
    ventana.fill(colorFondo)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > velocida:
        x -= velocida

    if keys[pygame.K_RIGHT] and x < widthVentana - velocida - width:
        x += velocida

    if keys[pygame.K_UP] and y > velocida:
        y -= velocida

    if keys[pygame.K_DOWN] and y < heightVentana - velocida - width:
        y += velocida

    pygame.draw.rect(ventana, (250, 35, 90), (x, y, width, height))
    pygame.display.update()

pygame.quit()


