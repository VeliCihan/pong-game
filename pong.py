# Importing required modules
import pygame
import random
from pygame.locals import *


# Screen size values
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

# Score values for the main game
score1 = 0
score2 = 0


# Paddle sprite class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, first_paddle: bool, width, height, x, y, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.first_paddle = first_paddle
        self.speed = PADDLE_SPEED

    def update(self):
        keys = pygame.key.get_pressed()

        if self.first_paddle:
            if keys[K_w] and self.rect.top > 0:
                self.rect.y -= self.speed
            elif keys[K_s] and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.y += self.speed
        else:
            if keys[K_UP] and self.rect.top > 0:
                self.rect.y -= self.speed
            elif keys[K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.y += self.speed


# Ball sprite class
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = [5, 5]
        self.set_speed()

    def update(self):
        global score1, score2
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0:
            self.reset()
            score2 += 1

        if self.rect.right > SCREEN_WIDTH:
            self.reset()
            score1 += 1

        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] *= -1

        if self.rect.colliderect(first_paddle.rect) or self.rect.colliderect(second_paddle.rect):
            self.speed[0] *= -1

    def reset(self):
        self.set_speed()
        self.rect.center = screen_rect.center

    def set_speed(self):
        self.speed[0] = random.randint(MIN_BALL_SPEED, MAX_BALL_SPEED)
        self.speed[1] = random.randint(MIN_BALL_SPEED, MAX_BALL_SPEED)


# Initializing pygame module on the game
pygame.init()

# Setting up the screen object of the game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Classic Pong Game!")
screen_rect = screen.get_rect()

# font = pygame.font.Font("Arial", size)
font = pygame.font.Font(None, 120)

# Setting up the first paddle arguments
first_paddle = Paddle(True, PADDLE_WIDTH, PADDLE_HEIGHT, 20, 0, WHITE)
first_paddle.rect.centery = screen_rect.centery

# Setting up the second paddle arguments
second_paddle = Paddle(False, PADDLE_WIDTH, PADDLE_HEIGHT, SCREEN_WIDTH - 20, 0, WHITE)
second_paddle.rect.centery = screen_rect.centery

ball = Ball(0, 0, WHITE)
ball.rect.center = screen_rect.center

# Setting up a sprite group to store and manage the sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(first_paddle)
all_sprites.add(second_paddle)
all_sprites.add(ball)


# Function to draw all the sprites and other objects
def draw_window():
    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT), 2)
    pygame.draw.circle(screen, WHITE, screen_rect.center, 100, 2)
    pygame.draw.circle(screen, WHITE, screen_rect.center, 5, 0)
    all_sprites.draw(screen)

    screen.blit(score1_font, score1_rect)
    screen.blit(score2_font, score2_rect)

    all_sprites.update()
    pygame.display.flip()


run = True

# Creating a clock object to manage the execution time
clock = pygame.time.Clock()

# Main game loop
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    # Rendering the font objects and font rectangles
    score1_font = font.render(str(score1), True, WHITE)
    score1_rect = score1_font.get_rect()
    score1_rect.center = (SCREEN_WIDTH / 4, screen_rect.centery)

    score2_font = font.render(str(score2), True, WHITE)
    score2_rect = score1_font.get_rect()
    score2_rect.center = (SCREEN_WIDTH / 4 * 3, screen_rect.centery)

    draw_window()
    clock.tick(FPS)

pygame.quit()
