import pygame
import os
from random import randint
from abc import ABC, abstractmethod

# Global variables

HEIGHT = 600
WIDTH = 400
GAP = 150

PIPE_WIDTH = 65
PIPE_HEIGHT = 400
BIRD_WIDTH = 42
BIRD_HEIGHT = 29

# Klasa abstrakcyjna reprezentująca obiekt w grze
class GameObject(ABC):
    
    def __init__(self, x = 0, y = 0, width = WIDTH, height = HEIGHT):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @abstractmethod
    def display(self, WIN):
        pass


# Klasa reprezentująca tło
class Background(GameObject):

    def __init__(self, x = 0, y = 0, back_width = WIDTH, back_height = HEIGHT):

        super().__init__(x, y, back_width, back_height)
        self.back_image = pygame.transform.scale(pygame.image.load(
            os.path.join('assets/GameObjects', 'background.png')), (self.width, self.height))
        
    def display(self, WIN):
        WIN.blit(self.back_image, (self.x, self.y))

class Base(GameObject):

    def __init__(self, x, y, base_width = WIDTH, base_height = 100):
        super().__init__(x, y , base_width, base_height)
        self.base_image = pygame.transform.scale(pygame.image.load(
            os.path.join('assets/GameObjects', 'base.png')), (self.width, self.height))

        
    def display(self, WIN):
        WIN.blit(self.base_image, (self.x, self.y))

# Klasa reprezentująca ptaka
class Bird(GameObject):

    def __init__(self, x, y, bird_width = BIRD_WIDTH, bird_height = BIRD_HEIGHT):
        super().__init__(x, y, bird_width, bird_height)

        self.bird_image = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/GameObjects', 'bird-midflip.png')), (self.width, self.height))
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

class Pipe(GameObject):
    def __init__(self, x, y, rotate = False, pipe_width = PIPE_WIDTH, pipe_height = PIPE_HEIGHT):
        super().__init__(x, y, pipe_width, pipe_height)
        self.rotate = rotate
        self.pipe_image = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/GameObjects', 'pipe.png')), (self.width, self.height))
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
        self.background = Background(0, 0)
        self.bird = Bird(WIDTH // 2 - 21, HEIGHT // 2)
        self.base = Base(0, HEIGHT - 100)
        self.pipes = []
        self.generate_pipes()
    
    def generate_pipes(self):
        i_top = randint(-350, -100)
        i_bot = i_top + GAP + PIPE_HEIGHT
        self.pipes.append((Pipe(WIDTH, i_top, True), Pipe(WIDTH, i_bot)))

    def display(self):
        self.background.display(self.WIN)
        self.bird.display(self.WIN)
        	
        for pipe_pair in self.pipes:
            pipe_pair[0].display(self.WIN)
            pipe_pair[1].display(self.WIN)
        self.base.display(self.WIN)

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

            

            if self.pipes[0][0].x == WIDTH // 2:

                self.generate_pipes()

            if self.pipes[0][0].x < -65:
                self.pipes.pop(0) 
                self.generate_pipes()

            self.display()
            self.bird.update()

            pygame.display.update()

game = Main()
game.main()
