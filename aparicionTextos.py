import pygame

def main():
    pygame.init()
    pantalla = pygame.display.set_mode([800, 800])
    pygame.display.set_caption("Laberinto mamadisimo")
    salir = False
    reloj1 = pygame.time.Clock()
    contador=0
    rep=0
    maquina=pygame.mixer.Sound("Maquina.wav")
    pygame.mixer.music.load("sacrifice.wav")

    # colores
    blanco = (255, 255, 255)
    celeste = (100, 210, 230)
    verde = (76, 145, 65)
    negro = (0, 0, 0)

    fuente1=pygame.font.SysFont("calibri",16,True,False)
    fuente2=pygame.font.SysFont("Timesnewroman",36,True,True)
    
    rFecha=fuente1.render("Miér",0,blanco)
    rFecha1=fuente1.render("Miérco",0,blanco)
    rFecha2=fuente1.render("Miércoles",0,blanco)
    rFecha3=fuente1.render("Miércoles, 17",0,blanco)
    rFecha4=fuente1.render("Miércoles, 17 de febrero",0,blanco)
    renglonFecha=fuente1.render("Miércoles, 17 de febrero de 2021",0,blanco)
    renglon1=fuente1.render("Mon",0,blanco)
    renglon2=fuente1.render("Monte",0,blanco)
    renglon3=fuente1.render("Monte Chin",0,blanco)
    renglon4=fuente1.render("Monte Chingolo",0,blanco)
    renglon5=fuente1.render("Monte Chingolo, Buenos",0,blanco)
    renglon6=fuente1.render("Monte Chingolo, Buenos Aires",0,blanco)
    presentacion=fuente2.render("MERLINO PRODUCTIONS",0,blanco)
    presentacion1=fuente2.render("PRESENTS",0,blanco)
    presentacion2=fuente2.render("ZOMBIE ENVOLU 2",0,blanco)

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

        reloj1.tick(20)
        pantalla.fill(negro)
        contador=pygame.time.get_ticks()

        #aparición de la fecha: cada medio segundo se agrega una silaba hasta completar la fecha. Luego de unos segundos desaparece
        if contador>=6000 and contador<15000:
            if rep==0:
                maquina.play()
                rep=1
            pantalla.blit(rFecha, (10, 10))
            if contador>6500 and contador<7000:
                pantalla.blit(rFecha1, (10, 10))
                pygame.display.update()
            if contador>7000 and contador<7500:
                pantalla.blit(rFecha2, (10, 10))
                pygame.display.update()
            if contador>7500 and contador<8000:
                pantalla.blit(rFecha3, (10, 10))
                pygame.display.update()
            if contador>8000 and contador<8500:
                pantalla.blit(rFecha4, (10, 10))
                pygame.display.update()
            if contador>8500:
                pantalla.blit(renglonFecha, (10, 10))
                pygame.display.update()
            if contador>9000 and contador<9500:
                pantalla.blit(renglon1, (575, 10))
            if contador>9500 and contador<10000:
                pantalla.blit(renglon2, (575, 10))
            if contador>10000 and contador<10500:
                pantalla.blit(renglon3, (575, 10))
            if contador>10500 and contador<11000:
                pantalla.blit(renglon4, (575, 10))
            if contador>11000 and contador<11500:
                pantalla.blit(renglon5, (575, 10))
            if contador>11500:
                pantalla.blit(renglon6, (575, 10))

            if contador>13500 and rep==1:
                pygame.mixer.music.play()
                rep=2

        if contador>17000 and contador<19500:
            pantalla.blit(presentacion,(200,250))
            pantalla.blit(presentacion1,(310,300))
        if contador >21000:
            pantalla.blit(presentacion2,(215,275))


            pygame.display.update()

        #aparición de texto de la historia: cada 3 segundos una oracion va llenando el cuadro hasta formar el parrafo
        


        pygame.display.update()

    pygame.quit()

main()