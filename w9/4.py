import pygame

#Initializing pygame module
pygame.init()

SCREEN_WIDHT, SCREEN_HEIGHT = 500, 500

# Will be retered Surface object (Creating window)
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('My First Game')

# Red Green Blue   ---> [0-255]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


clock = pygame.time.Clock()
# Frames Per Second
FPS = 60

PI = 3.14

running = True

flag = True
color = RED
x, y = SCREEN_WIDHT / 2, SCREEN_HEIGHT / 2

# Main program loop
while running:
  # Even loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        running = False
      elif event.key == pygame.K_SPACE:
        flag = not flag
      elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        x -= 5
      elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        x += 5
      elif event.key == pygame.K_UP or event.key == pygame.K_w:
        y -= 5
      elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        y += 5


  color = RED if flag else BLUE

  screen.fill(WHITE)

  pygame.draw.rect(screen, color, (x, y, 100, 100))

  # Apply changes on the window
  pygame.display.flip()

  clock.tick(FPS)


# Exiting from pygame program
pygame.quit()
