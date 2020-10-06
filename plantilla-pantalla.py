import pygame

def main():
    pygame.init()
    pygame.mixer.init()
    pantalla = pygame.display.set_mode([800, 800])
    pygame.display.set_caption("Laberinto mamadisimo")
    salir = False
    reloj1 = pygame.time.Clock()
    blanco=(255,255,255)

    fuente1=pygame.font.SysFont("calibri",16,True,False)
    fuente2=pygame.font.SysFont("Timesnewroman",36,True,True)

    presentacion=fuente2.render("MERLINO PRODUCTIONS",0,blanco)
    presentacion1=fuente2.render("PRESENTS",0,blanco)
    presentacion2=fuente2.render("ZOMBIE ENVOLU 2",0,blanco)

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

        reloj1.tick(20)
        pantalla.fill((0,0,0))
        pantalla.blit(presentacion2,(220,275))
        pygame.display.update()

    pygame.quit()

main()