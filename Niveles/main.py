import pygame
import player
import nivel
import ventana

# Constantes
verde = (76, 145, 65)
negro = (0, 0, 0)
rojo = (255, 0, 0)
violeta = (80, 36, 115)


def main(cont_nivel):

    pygame.init()
    pantalla = pygame.display.set_mode([600, 600])
    pygame.display.set_caption("Laberinto del terror")
    mapa = nivel.Nivel() # La clase nivel contiene los niveles
    ven = ventana.Ventana() # La clase ventana contiene los atributos a dibujar

    mapa.seleccion(ven, cont_nivel) # Selecciona, lee y carga el nivel correspondiente

    jugador = player.Personaje([0, 0])
    clock = pygame.time.Clock() # Dentro del loop principal, el clock determina la velocidad del jugador

    salir = False
    continuar = True
    llave = False

    # loop principal
    while continuar and not salir:

        pantalla.fill(violeta)  # Color de fondo
        ven.dibujarNivel(pantalla, llave)  # Metodo que dibuja el nivel, recibe el estado de la llave

        (xant, yant) = (jugador.rect.left, jugador.rect.top)

        #  Evento de salida/pausa
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                     salir = ven.pausa(pantalla)

        jugador.handle_event(event)
        pantalla.blit(jugador.image, jugador.rect)

        # Colision con paredes, limitan los movimientos del juegador
        for i in range(0, len(ven.lstparedes)):
            if jugador.rect.colliderect(ven.lstparedes[i]):
                (jugador.rect.left, jugador.rect.top) = (xant, yant)

        # Colision con casa, no se activa si la llave esta en false
        if jugador.rect.colliderect(ven.rLlegada) and llave:
            continuar = False

        # Colision con llave
        if jugador.rect.colliderect(ven.key):
            llave = True

        pygame.display.update()
        clock.tick(40)

    # Al finalizar el bucle, se evalua si continuar al siguiente nivel o no
    if cont_nivel < 2 and not salir:
        cont_nivel += 1
        main(cont_nivel)  # al main se le pasa el nivel

    pygame.quit()


main(0)
