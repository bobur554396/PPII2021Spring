import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


class Point:
  def __init__(self, _x: int, _y: int):
    self.x = _x
    self.y = _y
  

class Food:
  def __init__(self, *args, **kwargs):
    self.location = Point(0, 0)
    self.radius = 10
    self.set_random_position()
  
  @staticmethod
  def own_round(value, base = 10):
    return base * round(value / 10)

  def set_random_position(self):
    x = self.own_round(random.randint(0, WINDOW_WIDTH))
    y = self.own_round(random.randint(0, WINDOW_HEIGHT))
    self.location.x = x
    self.location.y = y
  
  def draw(self):
    pygame.draw.circle(screen, BLUE, (self.location.x, self.location.y), self.radius)


class Snake:
  def __init__(self, *args, **kwargs):
    self.radius = 10
    self.body = [Point(100, 100), Point(110, 100)]
    self.block = 15
    self.dx = self.block
    self.dy = 0
  
  def head(self):
    return self.body[0]
  
  def move(self):
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i].x = self.body[i - 1].x
      self.body[i].y = self.body[i - 1].y

    self.head().x += self.dx
    self.head().y += self.dy

    if self.head().x > WINDOW_WIDTH:
      self.head().x = 0
    if self.head().x < 0:
      self.head().x = WINDOW_WIDTH

  def draw(self):
    for i, point in enumerate(self.body):
      color = RED if i == 0 else GREEN
      pygame.draw.circle(screen, color, (point.x, point.y), self.radius)

  def add_tail(self):
    self.body.append(Point(0, 0))

snake = Snake()
food = Food()

game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        snake.dx, snake.dy = snake.block, 0
      if event.key == pygame.K_LEFT:
        snake.dx, snake.dy = -snake.block, 0
      if event.key == pygame.K_UP:
        snake.dx, snake.dy = 0, -snake.block
      if event.key == pygame.K_DOWN:
        snake.dx, snake.dy = 0, snake.block
      if event.key == pygame.K_SPACE:
        snake.add_tail()
        food.set_random_position()

  snake.move()


  screen.fill(BLACK)
  snake.draw()
  food.draw()

  pygame.display.flip()

  clock.tick(5)




pygame.quit()
