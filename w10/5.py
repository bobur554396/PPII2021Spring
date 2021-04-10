import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
done = False

clock = pygame.time.Clock()

# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Ball:
  def __init__(self, *args, **kwargs):
    self.radius = 20
    self.x = random.randint(1, 580)
    self.y = random.randint(1, 580)
    self.dx = random.randint(-5, 5)
    self.dy = random.randint(-5, 5)
    self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  
  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.x > 600 or self.x < 0:
      self.dx *= -1
    if self.y > 600 or self.y < 0:
      self.dy *= -1


  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


balls = [
  Ball()
]

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        balls.append(Ball())

  for ball in balls:
    ball.move()

  screen.fill(WHITE)
  
  for ball in balls:
    ball.draw(screen)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
