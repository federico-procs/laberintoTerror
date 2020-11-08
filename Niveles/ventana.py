import pygame

negro = (0, 0, 0)

class Ventana:
    def __init__(self):
        self.cont = 0
        self.lstparedes = []
        self.lstcamino = []
        self.pared_x = 0
        self.pared_y = 0
        self.rSalida = pygame.Rect(0, 0, 40, 40)
        self.rLlegada = pygame.Rect(520, 520, 80, 80)
        self.key = pygame.Rect(0, 0, 0, 0)

    def cargarFondo(self, matriz):
        # Bordes
        self.lstparedes.append(pygame.Rect(-1, -1, 1, 601))
        self.lstparedes.append(pygame.Rect(601, -1, 1, 601))
        self.lstparedes.append(pygame.Rect(-1, -1, 601, 1))
        self.lstparedes.append(pygame.Rect(1, 601, 601, 1))
        # Paredes y camino
        for fila in range(15):
            for columna in range(15):
                if matriz[fila][columna] == "1":
                    self.lstparedes.append(pygame.Rect(self.pared_x, self.pared_y, 40, 40))
                    self.pared_x += 40
                else:
                    self.lstcamino.append(pygame.Rect(self.pared_x, self.pared_y, 40, 40))
                    self.pared_x += 40
                    if matriz[fila][columna] == "2":
                        self.key = self.lstcamino[len(self.lstcamino)-1]
            self.pared_x = 0
            self.pared_y += 40

    def dibujarNivel(self, pantalla, llave):
        arbol1 = pygame.image.load("Tree.png")
        camino = pygame.image.load("Road.png")
        casa = pygame.image.load("House.png")
        key = pygame.image.load("Key.png")

        # Camino
        for i in range(len(self.lstcamino)):
            pantalla.blit(camino, self.lstcamino[i])
        for i in range(4, len(self.lstparedes)):
            pantalla.blit(arbol1, self.lstparedes[i])

        if not llave:
            pantalla.blit(key, self.key)
        pantalla.blit(casa, self.rLlegada)

    def pausa(self, pantalla):
        pausa = True
        iPausa = pygame.image.load("Pausa.png")
        pantalla.blit(iPausa, self.lstcamino[0])
        pygame.display.update()
        salir = False
        while pausa and not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        pausa = False
        return salir