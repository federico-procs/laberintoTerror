import pygame

# Constantes
verde = (76, 145, 65)
negro = (0, 0, 0)
rojo = (255, 0, 0)


class Ventana:
    def __init__(self):
        self.cont = 0
        self.listarec = []
        self.pared_x = 0
        self.pared_y = 0
        self.rSalida = pygame.Rect(0, 0, 40, 40)
        self.rLlegada = pygame.Rect(560, 560, 40, 40)

    def cargarFondo(self, matriz):
        for fila in range(15):
            for columna in range(15):
                if matriz[fila][columna] == 1:
                    self.listarec.append(pygame.Rect(self.pared_x, self.pared_y, 40, 40))
                    self.pared_x += 40
                else:
                    self.pared_x += 40
            self.pared_x = 0
            self.pared_y += 40
        # Bordes
        self.listarec.append(pygame.Rect(-1, -1, 1, 601))
        self.listarec.append(pygame.Rect(601, -1, 1, 601))
        self.listarec.append(pygame.Rect(-1, -1, 601, 1))
        self.listarec.append(pygame.Rect(1, 601, 601, 1))

    def dibujarNivel(self, pantalla, color):
        for i in range(len(self.listarec)):
            pygame.draw.rect(pantalla, color, self.listarec[i])
        pygame.draw.rect(pantalla, verde, self.rSalida)
        pygame.draw.rect(pantalla, rojo, self.rLlegada)


class Nivel:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.nivel1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.nivel2 = [[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                       [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                       [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0]]

        self.nivel3 = [[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                       [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                       [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0]]

    def seleccion(self, ven, cont):
        if cont == 0:
            ven.cargarFondo(self.nivel1)
        if cont == 1:
            ven.cargarFondo(self.nivel2)
        if cont == 2:
            ven.cargarFondo(self.nivel3)


class Player(pygame.sprite.Sprite):
    def __init__(self, imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.rect.top, self.rect.left = (0, 0)

    def mover(self, vx, vy):
        self.rect.move_ip(vx, vy)

    def update(self, superficie):
        superficie.blit(self.imagen, self.rect)


def main(cont_nivel):
    pygame.init()
    pantalla = pygame.display.set_mode([600, 600])
    pygame.display.set_caption("Laberinto")
    salir = False
    continuar = True
    nivel = Nivel(pantalla) # La clase nivel contiene la pantalla del juego y los niveles
    ven = Ventana() # La clase ventana contiene la lista de rect's a dibujar, salida y llagada

    nivel.seleccion(ven, cont_nivel) #Se selecciona el nivel mediante este metodo que lo carga en la ventana

    imagen1 = pygame.image.load("man.jpeg")
    sprite1 = Player(imagen1)
    vx = 0
    vy = 0
    velocidad = 1

    # loop principal
    while continuar and not salir:

        pantalla.fill(verde)  # Color de fondo
        ven.dibujarNivel(pantalla, negro)  # Metodo que dibuja el nivel, se le pasa la pantalla y el color a pintar

        (xant, yant) = (sprite1.rect.left, sprite1.rect.top)

        # Capturador de eventos
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

        # Mover personaje segun el evento
        sprite1.mover(vx, vy)
        for i in range(0, len(ven.listarec)):
            if sprite1.rect.colliderect(ven.listarec[i]):
                (sprite1.rect.left, sprite1.rect.top) = (xant, yant)
        sprite1.update(pantalla)

        if sprite1.rect.colliderect(ven.rLlegada):
            continuar = False

        pygame.display.update()

    # Al finalizar el bucle, se evalua si continuar al siguiente nivel o no
    if cont_nivel < 2 and not salir:
        cont_nivel += 1
        main(cont_nivel)  # al main se le pasa el nivel

    pygame.quit()


main(0)
