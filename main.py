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
  all = pygame.sprite.RenderUpdates()
  Tech1.containers = all
  Tech2.containers = all
  p1point = 0
  p2point = 0
  gamestate = 0
  ok1 = 0
  ok2 = 0
  wait = 3.00
  play = 15.00
  Tech1.image = pygame.image.load("data/tech1.png").convert_alpha()
  Tech2.image = pygame.image.load("data/tech2.png").convert_alpha()
  startImg = pygame.image.load("data/start.png").convert_alpha()
  setImg = pygame.image.load("data/set.png").convert_alpha()
  endImg = pygame.image.load("data/end.png").convert_alpha()

  clock = pygame.time.Clock()
  while True:
    clock.tick(60)
    sysfont = pygame.font.SysFont(None, 80)
    score1 = sysfont.render(str(p1point), False, (200,0,0))
    score2 = sysfont.render(str(p2point), False, (0,0,255))
    waitcount = sysfont.render(str(wait), False, (0,0,0))
    playcount = sysfont.render(str(play), False, (0,0,0))
    canplay = sysfont.render("OK", False, (0,0,0))
    pusha = sysfont.render("PUSH A", False, (0,0,0))
    pushl = sysfont.render("PUSH L", False, (0,0,0))
    pushspace = sysfont.render("PUSH SPACE", False, (0,0,0))

    screen.fill((255,255,255))
    all.update()
    all.draw(screen)
    screen.blit(score1, (160,20))
    screen.blit(score2, (480,20))

    if gamestate == 0:
      if ok1 == 0:
        screen.blit(pusha, (80, 320))
      if ok1 == 1:
        screen.blit(canplay, (140, 320))
      if ok2 == 0:
        screen.blit(pushl, (400, 320))
      if ok2 == 1:
        screen.blit(canplay, (460, 320))

    if gamestate == 1:
      screen.blit(playcount, (300, 20))
      play-=0.010
      if play >= 14.50:
        screen.blit(startImg, (250, 120))
      if play <= 0.00:
        play = 15.00
        gamestate = 3

    if gamestate == 2:
      screen.blit(waitcount, (300, 20))
      screen.blit(setImg, (250, 120))
      wait-=0.010
      if wait <= 0.00:
        gamestate = 1
        wait = 3.00

    if gamestate == 3:
      screen.blit(endImg, (220, 120))
      screen.blit(pushspace, (160, 320))

    pygame.display.update()
    if gamestate == 0 and ok1 == 1 and ok2 == 1:
      gamestate = 2
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
        if event.key == K_a:
          if gamestate == 1:
            Tech1((random.uniform(0,320), 0))
            p1point+=1
          if gamestate == 0:
            ok1 = 1
        if event.key == K_l:
          if gamestate == 1:
            Tech2((random.uniform(320,640), 0))
            p2point+=1
          if gamestate == 0:
            ok2 = 1
        if event.key == K_SPACE:
          if gamestate == 3:
            main()

def end():
  pygame.init()
  screen = pygame.display.set_mode(SCR_RECT.size)
  all = pygame.sprite.RenderUpdates()
  Tech.containers = all
  teccount = 0
  red = 0
  blue = 0
  green = 0
  Tech.image = pygame.image.load("data/tech.png").convert_alpha()
  
  clock = pygame.time.Clock()
  while True:
    clock.tick(60)
    sysfont = pygame.font.SysFont(None, 80)
    count = sysfont.render(str(teccount), False, (red, blue, green))
    screen.fill((255, 255, 255))
    all.update()
    all.draw(screen)
    screen.blit(count, (320,20))
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
          teccount+=1
          red = random.randint(0,255)
          blue = random.randint(0,255)
          green = random.randint(0,255)

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

class Tech1(pygame.sprite.Sprite):
  speed = -5
  def __init__(self, pos):
    pygame.sprite.Sprite.__init__(self, self.containers)
    self.rect = self.image.get_rect()
    self.rect.center = pos
  def update(self):
    self.rect.move_ip(0, -self.speed)
    if self.rect.bottom < 0:
      self.kill()

class Tech2(pygame.sprite.Sprite):
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
