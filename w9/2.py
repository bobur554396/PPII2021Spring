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

# Main program loop
while running:
  # Even loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(WHITE)

  pygame.draw.line(screen, GREEN, (10, 10), (200, 10), 1)

  for step in range(20, 50, 10):
    pygame.draw.line(screen, BLUE, (10, step), (200, step), 4)

  pygame.draw.circle(screen, RED, (300, 50), 40)
  pygame.draw.circle(screen, RED, (400, 50), 40, 3)

  pygame.draw.rect(screen, GREEN, (30, 60, 200, 100))
  pygame.draw.rect(screen, GREEN, (30, 170, 200, 100), 3)

  pygame.draw.ellipse(screen, RED, (30, 170, 200, 100), 2)

  pygame.draw.polygon(screen, BLACK, ((450, 170), (400, 250), (500, 250)))
  pygame.draw.polygon(screen, BLACK, ((350, 170), (300, 250), (400, 250)), 3)

  pygame.draw.arc(screen, RED, (50, 300, 150, 150), 0, PI / 2, 3)
  pygame.draw.arc(screen, BLACK, (50, 300, 150, 150), PI / 2, PI, 3)
  pygame.draw.arc(screen, BLUE, (50, 300, 150, 150), PI, 3 * PI / 2, 3)
  pygame.draw.arc(screen, GREEN, (50, 300, 150, 150), 3 * PI / 2, 0, 3)


  font = pygame.font.Font(None, 25)
  text = font.render("KBTU FIT", True, RED)

  screen.blit(text, (300, 300))

  # Apply changes on the window
  pygame.display.flip()

  clock.tick(FPS)


# Exiting from pygame program
pygame.quit()
