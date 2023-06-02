import pygame
import os
from random import randint

HEIGHT = 600
WIDTH = 400
GAP = 150

# Klasa reprezentująca tło
class Background:
    def __init__(self, background_width, background_height):
        self.image = pygame.transform.scale(pygame.image.load(
            os.path.join('assets/GameObjects', 'background.png')), (background_width, background_height))
        
    def display(self, WIN):
        WIN.blit(self.image, (0, 0))

# Klasa reprezentująca ptaka
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bird_image = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/GameObjects', 'bird-midflip.png')), (42, 29))
        self.rect = self.bird_image.get_rect()
        self.vel = -3
    
    def jump(self):
        if self.y > 0:
            self.vel = -3
    
    def update(self):
        self.y += self.vel
        self.vel += 0.05
    
    def display(self, WIN):
        WIN.blit(self.bird_image, (self.x, self.y))

class Pipe:
    def __init__(self, x, y, rotate=False):
        self.x = x
        self.y = y
        self.rotate = rotate
        self.pipe_image = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/GameObjects', 'pipe.png')), (65, 400))
        self.rect = self.pipe_image.get_rect()

    def display(self, WIN):
        if self.rotate:
            WIN.blit(pygame.transform.rotate(self.pipe_image, 180), (self.x, self.y))
        else:
            WIN.blit(self.pipe_image, (self.x, self.y))

    def move(self):
        self.x -= 0.5

# Główna klasa gry
class Main:
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = Background(WIDTH, HEIGHT)
        self.bird = Bird(WIDTH // 2 - 21, HEIGHT // 2)
        self.pipes = []
        self.generate_pipes()
    
    def generate_pipes(self):
        i_top = randint(-300, 0)
        i_bot = i_top + GAP + 400
        self.pipes.append((Pipe(WIDTH, i_top, True), Pipe(WIDTH, i_bot)))

    def display(self):
        self.background.display(self.WIN)
        self.bird.display(self.WIN)
        for pipe_pair in self.pipes:
            pipe_pair[0].display(self.WIN)
            pipe_pair[1].display(self.WIN)

    def main(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")

        run = True
        
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

            for pipe_pair in self.pipes:
                pipe_pair[0].move()
                pipe_pair[1].move()

            if self.pipes[0][0].x < -65:
                self.pipes.pop(0)
                self.generate_pipes()

            self.display()
            self.bird.update()

            pygame.display.update()

game = Main()
game.main()
