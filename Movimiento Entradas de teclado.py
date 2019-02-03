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
    pygame.time.delay(100)
    ventana.fill(colorFondo)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= velocida

    if keys[pygame.K_RIGHT]:
        if x < widthVentana:
            x += velocida

    if keys[pygame.K_UP]:
        if y > 0:
            y -= velocida

    if keys[pygame.K_DOWN]:
        if y < heightVentana:
            y += velocida

    pygame.draw.rect(ventana, (250, 35, 90), (x, y, width, height))
    pygame.display.update()

pygame.quit()


