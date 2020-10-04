import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.rect.top, self.rect.left = (0, 0)

    def mover(self, vx, vy):
        self.rect.move_ip(vx, vy)

    def update(self, superficie):
        superficie.blit(self.imagen, self.rect)


def main():
    pygame.init()
    pantalla = pygame.display.set_mode([800, 800])
    pygame.display.set_caption("Laberinto mamadisimo")
    salir = False
    imagen1 = pygame.image.load("man.jpeg")
    sprite1 = Player(imagen1)
    vx = 0
    vy = 0
    velocidad = 10
    contador = 0
    fuente1=pygame.font.SysFont("Arial",20,True,False)
    renglon1=fuente1.render("LA CIUDAD FUE INVADIDA",0,(255, 255, 255))
    renglon2=fuente1.render("POR ZOMBIES",0,(255, 255, 255))
    renglon3=fuente1.render("Y SOLO TÚ",0,(255, 255, 255))
    renglon4=fuente1.render("PUEDES ESCAPAR",0,(255, 255, 255))

    reloj1 = pygame.time.Clock()

    # colores
    blanco = (255, 255, 255)
    celeste = (100, 210, 230)
    verde = (76, 145, 65)
    negro = (0, 0, 0)

    # marco de pantalla
    rizq = pygame.Rect(-1, -1, 1, 801)
    rder = pygame.Rect(801, -1, 1, 801)
    rarriba = pygame.Rect(-1, -1, 801, 1)
    rabajo = pygame.Rect(-1, 801, 801, 1)

    # lineas horizontales
    r3 = pygame.Rect(60, 260, 200, 30)
    r5 = pygame.Rect(60, 350, 410, 30)
    r6 = pygame.Rect(60, 710, 350, 30)
    r11 = pygame.Rect(290, 60, 120, 30)
    r12 = pygame.Rect(500, 290, 300, 30)
    r13 = pygame.Rect(500, 200, 240, 30)
    r16 = pygame.Rect(500, 580, 150, 30)
    r18 = pygame.Rect(500, 490, 150, 30)
    r20 = pygame.Rect(560, 60, 150, 30)

    # lineas verticales
    r1 = pygame.Rect(60, 0, 30, 260)
    r2 = pygame.Rect(60, 350, 30, 390)
    r4 = pygame.Rect(260, 60, 30, 230)
    r7 = pygame.Rect(290, 350, 30, 290)
    r8 = pygame.Rect(470, 0, 30, 230)
    r9 = pygame.Rect(470, 290, 30, 230)
    r10 = pygame.Rect(470, 580, 30, 220)
    r14 = pygame.Rect(710, 60, 30, 170)
    r15 = pygame.Rect(710, 380, 30, 480)
    r17 = pygame.Rect(620, 610, 30, 190)
    r19 = pygame.Rect(620, 380, 30, 140)

    listrect = [rizq, rder, rarriba, rabajo, r1, r2, r3, r4, r5, r6,
                r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

    rfinal = pygame.Rect(740, 740, 60, 60)

    # loop principal
    while salir != True:

        (xant, yant) = (sprite1.rect.left, sprite1.rect.top)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    vy = velocidad
                if event.key == pygame.K_RIGHT:
                    vx = velocidad
                if event.key == pygame.K_UP:
                    vy = -velocidad
                if event.key == pygame.K_LEFT:
                    vx = -velocidad

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    vy = 0
                if event.key == pygame.K_RIGHT:
                    vx = 0
                if event.key == pygame.K_UP:
                    vy = 0
                if event.key == pygame.K_LEFT:
                    vx = 0

        while contador<7000:
            pantalla.fill(negro)
            pantalla.blit(renglon1, (0, 0))
            pantalla.blit(renglon2, (0, 30))
            contador=pygame.time.get_ticks()
            pygame.display.update()

        while contador<10000:
            pantalla.fill(negro)
            pantalla.blit(renglon3, (0, 0))
            pantalla.blit(renglon4, (0, 30))
            contador=pygame.time.get_ticks()
            pygame.display.update()

        reloj1.tick(20)
        pantalla.fill(verde)

        for i in range(0, len(listrect)):
            pygame.draw.rect(pantalla, negro, listrect[i])

        sprite1.update(pantalla)
        pygame.draw.rect(pantalla, celeste, rfinal)

        sprite1.mover(vx, vy)
        for i in range(0, len(listrect)):
            if sprite1.rect.colliderect(listrect[i]):
                (sprite1.rect.left, sprite1.rect.top) = (xant, yant)

        if sprite1.rect.colliderect(rfinal):
            salir = True

        pygame.display.update()

    pygame.quit()


main()
