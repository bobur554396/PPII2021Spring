import pygame
import os

pygame.init()
screen = pygame.display.set_mode((600, 600))
done = False

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


_image_library = {}
def get_image(path):
  global _image_library
  image = _image_library.get(path)
  if image == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    image = pygame.image.load(canonicalized_path)
    _image_library[path] = image
  return image


while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == EVENT_OWN:
      pass

  print(_image_library)

  screen.fill(WHITE)

  screen.blit(get_image('jet.png'), (20, 20))

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
