import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
done = False


clock = pygame.time.Clock()

# RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

color = RED

x, y = 30, 30

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        if color == RED: color = GREEN
        else: color = RED

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP]: y -= 3
  if pressed[pygame.K_DOWN]: y += 3
  if pressed[pygame.K_LEFT]: x -= 3
  if pressed[pygame.K_RIGHT]: x += 3

  screen.fill(WHITE)

  pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
