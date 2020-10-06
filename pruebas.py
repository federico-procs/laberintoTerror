import pygame

def main():
    pygame.init()
    pantalla = pygame.display.set_mode([800, 800])
    pygame.display.set_caption("Laberinto mamadisimo")
    salir = False
    reloj1 = pygame.time.Clock()
    contador=0
    reproductor=0
    maquina=pygame.mixer.Sound("Maquina 2.wav")
    pygame.mixer.music.load("sacrifice.wav")

    # colores
    blanco = (255, 255, 255)
    celeste = (100, 210, 230)
    verde = (76, 145, 65)
    negro = (0, 0, 0)

    #textos
    fuente1=pygame.font.SysFont("calibri",16,True,False)
    fuente2=pygame.font.SysFont("Timesnewroman",36,True,True)
    fuente3=pygame.font.SysFont("arial",30,True,False)
    
    cargando1=fuente3.render("CARGANDO...",0,blanco)
    rFecha=fuente1.render("Miér",0,blanco)
    rFecha1=fuente1.render("Miérco",0,blanco)
    rFecha2=fuente1.render("Miércoles",0,blanco)
    rFecha3=fuente1.render("Miércoles, 17",0,blanco)
    rFecha4=fuente1.render("Miércoles, 17 de febrero",0,blanco)
    renglonFecha=fuente1.render("Miércoles, 17 de febrero de 2021",0,blanco)
    renglon1=fuente2.render("MONTE CHINGOLO FUE INVADIDO",0,blanco)
    renglon2=fuente2.render("POR ZOMBIES",0,blanco)
    renglon3=fuente2.render("Y SOLO TÚ",0,blanco)
    renglon4=fuente2.render("PUDISTE SOBREVIVIR",0,blanco)
    renglon5=fuente2.render("EVITA SER ATRAPADO",0,blanco)
    renglon6=fuente2.render("Y ENCUENTRA LA SALIDA",0,blanco)
    imagen1=pygame.image.load("zombie menu 2.png")

    def cargando():
        contador=0
        while contador<10000:
            contador=pygame.time.get_ticks()
            pantalla.fill((0,0,0))
            pantalla.blit(cargando1, (10, 750))
            if contador>6000:
                pantalla.blit(imagen1,(20,20))
            pygame.display.update()

    def inicio():
        contador=0
        reproductor=0
        while contador<28000:
            pantalla.fill(negro)
            contador=pygame.time.get_ticks()

            #aparición de la fecha: cada medio segundo se agrega una silaba hasta completar la fecha. Luego de unos segundos desaparece
            if contador>=12000 and contador<18000:
                if reproductor==0:
                    maquina.play()
                    reproductor=1
                pantalla.blit(rFecha, (10, 10))
                if contador>12500 and contador<13000:
                    pantalla.blit(rFecha1, (10, 10))
                    pygame.display.update()
                if contador>13000 and contador<13500:
                    pantalla.blit(rFecha2, (10, 10))
                    pygame.display.update()
                if contador>13500 and contador<14000:
                    pantalla.blit(rFecha3, (10, 10))
                    pygame.display.update()
                if contador>14000 and contador<14500:
                    pantalla.blit(rFecha4, (10, 10))
                    pygame.display.update()
                if contador>14500:
                    pantalla.blit(renglonFecha, (10, 10))
                    pygame.display.update()
                pygame.display.update()

            #aparición de texto de la historia: cada 3 segundos una oracion va llenando el cuadro hasta formar el parrafo
            if contador>16000 and reproductor ==1:
                pygame.mixer.music.play()
                reproductor=2
            if contador>19000 and contador<28000:
                pantalla.blit(renglon1, (100, 150))
                pantalla.blit(renglon2, (275, 200))
                if contador>22000:
                    pantalla.blit(renglon3, (305, 275))
                    pantalla.blit(renglon4, (200, 325))
                    if contador>25000:
                        pantalla.blit(renglon5, (200, 450))
                        pantalla.blit(renglon6, (180, 500))


            pygame.display.update()

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

        reloj1.tick(20)
        contador=pygame.time.get_ticks()
        if contador<10000:
            cargando()
        
        if contador>10000 and contador<12000:
            inicio()
        
        
        pantalla.fill((0,0,0))
        pygame.display.update()

    pygame.quit()

main()