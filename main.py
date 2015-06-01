import pygame
from pygame.locals import *
import os
import sys
import random

SCR_RECT = Rect(0, 0, 640, 480)

def main():
  pygame.init()
  screen = pygame.display.set_mode(SCR_RECT.size)
  all = pygame.sprite.RenderUpdates()
  Tech.containers = all
  Tech.image = load_image("tech.png", 1)
  
  clock = pygame.time.Clock()
  while True:
    clock.tick(60)
    screen.fill((255, 255, 255))
    all.update()
    all.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
        if event.key == K_SPACE:
          Tech((random.uniform(0,640), 0))

class Tech(pygame.sprite.Sprite):
  speed = -5
  def __init__(self, pos):
    pygame.sprite.Sprite.__init__(self, self.containers)
    self.rect = self.image.get_rect()
    self.rect.center = pos
  def update(self):
    self.rect.move_ip(0, -self.speed)
    if self.rect.bottom < 0:
      self.kill()


def load_image(filename, colorkey=None):
    filename = os.path.join("data", filename)
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        print "Cannot load image:", filename
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

def load_sound(filename):
    filename = os.path.join("data", filename)
    return pygame.mixer.Sound(filename)

if __name__ == "__main__":
    main()
