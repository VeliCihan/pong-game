# A Classic Pong Game made with `Python` and `pygame`

Python documents: [www.python.org](https://www.python.org/).

Pygame documents: [www.pygame.org](https://www.pygame.org/).

This is a simple classic pong game made within
an easy game engine that is python [pygame](https://www.pygame.org/).
You can build both simple games and complex games using pygame game engine.

### Required modules:
- `pygame`
- `random`
- `pygame.locals`

if pygame is not installed on your device you can run the command below:

Windows - Linux:
```
pip install pygame
```

Mac:
```
python3 -m pip3 install pygame
```

## Game Structure

### Importing Required Modules
```python
import pygame
import random
from pygame.locals import *
```

### Constant Variables
```python
# Screen sizes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Color values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle values
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 120
PADDLE_SPEED = 10

# Ball values
BALL_SIZE = 20
MIN_BALL_SPEED = 5
MAX_BALL_SPEED = 10

# setting up the frame count with FPS keyword
FPS = 40

```

### Game Sprite classes

```python
import pygame

# Paddle sprite class
class Paddle(pygame.sprite.Sprite):...
# Ball sprite class
class Ball(pygame.sprite.Sprite):...
```

### Game Screen setup
```python
# Screen size values
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Initializing pygame module on the game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game!")
```

### Creating and Adding Sprite Objects
```python

# Setting up the first paddle arguments
first_paddle = Paddle(...)

# Setting up the second paddle arguments
second_paddle = Paddle(...)
# Setting up the ball object
ball = Ball(...)

all_sprites = pygame.sprite.Group()
all_sprites.add(first_paddle)
all_sprites.add(second_paddle)
all_sprites.add(ball)
```

### Creating a Clock Object for Time Managing

```python
clock = pygame.time.Clock()

# Example usage:
# ...
# clock.tick(60)
# ...
```

### Main Game Loop
```python
run = True

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    draw_window()
    clock.tick(FPS)
pygame.quit()
```



### How to play the Game?
To play the classic pong game you can run the command below:
```
python pong.py
```
That's all for the documentation don't forget to enjoy playing the classic pong game.