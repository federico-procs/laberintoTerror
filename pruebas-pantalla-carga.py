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
    reloj1 = pygame.time.Clock()
    contador=0

    # colores
    blanco = (255, 255, 255)
    celeste = (100, 210, 230)
    verde = (76, 145, 65)
    negro = (0, 0, 0)

    imagen1=pygame.image.load("zombie menu 2.png")

    fuente1=pygame.font.SysFont("Arial",30,True,False)
    fuente2=pygame.font.SysFont("Timesnewroman",20,True,False)
    cargando=fuente1.render("CARGANDO...",0,blanco)
    renglon1=fuente2.render("LA CIUDAD FUE INVADIDA",0,blanco)
    renglon2=fuente2.render("POR ZOMBIES",0,blanco)
    renglon3=fuente2.render("Y SOLO TÚ",0,blanco)
    renglon4=fuente2.render("PUEDES ESCAPAR",0,blanco)

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
        
        reloj1.tick(20)
        contador=pygame.time.get_ticks()
        pantalla.fill(negro)
        if contador<10000:
            pantalla.blit(cargando, (10, 750))
            if contador>6000:
                pantalla.blit(imagen1,(20,20))

        if contador>13000:
            pantalla.blit(renglon1, (375, 200))
            pantalla.blit(renglon2, (425, 250))
            if contador>16000:
                pantalla.fill(negro)
                pantalla.blit(renglon3, (375, 200))
                pantalla.blit(renglon4, (425, 250))

        pygame.display.update()
    pygame.quit()

main()