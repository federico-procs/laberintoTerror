import pygame

# Constantes
alto = 35
ancho = 24


class Personaje(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('Jugador_sheet.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 24, 35))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.down_states = {0: (0, 0, ancho, alto), 1: (ancho, 0, ancho, alto), 2: (ancho*3, 0, ancho, alto)}
        self.left_states = {0: (0, alto, ancho, alto), 1: (ancho, alto, ancho, alto), 2: (ancho*3, alto, ancho, alto)}
        self.right_states = {0: (0, alto*2, ancho, alto), 1: (ancho, alto*2, ancho, alto), 2: (ancho*3, alto*2, ancho, alto)}
        self.up_states = {0: (0, alto*3, ancho, alto), 1: (ancho, alto*3, ancho, alto), 2: (ancho*3, alto*3, ancho, alto)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')


#  class Player(pygame.sprite.Sprite):
#    def __init__(self, imagen):
#        self.imagen = imagen
#        self.rect = self.imagen.get_rect()
#        self.rect.top, self.rect.left = (0, 0)

#   def mover(self, vx, vy):
#       self.rect.move_ip(vx, vy)

#    def update(self, superficie):
#        superficie.blit(self.imagen, self.rect)