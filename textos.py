import pygame

def main():
    pygame.init()
    pantalla = pygame.display.set_mode([800, 800])
    pygame.display.set_caption("Laberinto mamadisimo")
    salir = False
    reloj1 = pygame.time.Clock()
    imagen1=pygame.image.load("man running.jpg")
    contador=0
    rep=1

    # colores
    blanco = (255, 255, 255)
    celeste = (100, 210, 230)
    verde = (76, 145, 65)
    negro = (0, 0, 0)

    fuente2=pygame.font.SysFont("Timesnewroman",36,True,True)
    
    renglon1=fuente2.render("'CREO QUE LOS PERDÍ...'",0,blanco)
    renglon2=fuente2.render("'¿DE DONDE SALIERON ESTAS COSAS?'",0,blanco)

    corriendo=pygame.mixer.Sound("corriendo.wav")
    agitado=pygame.mixer.Sound("agitado.wav")

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

        reloj1.tick(20)
        pantalla.fill(negro)
        contador=pygame.time.get_ticks()
        if contador>4000 and contador<10000:
            pantalla.blit(imagen1,(-112,100))
            if rep==1:
                corriendo.play()
                rep=2
            if contador>7500 and rep ==2:
                agitado.play()
                rep=3
            if contador>9000:
                corriendo.stop()

        if contador>10000 and contador<12000:
            pantalla.blit(renglon1,(0,0))
        if contador>12000 and contador<15000:
            pantalla.blit(renglon2,(0,60))
            agitado.fadeout(750)


        pygame.display.update()

    pygame.quit()

main()