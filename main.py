import pygame
import os

#HEIGHT = 600
#WIDTH = 400

class Main:
    def __init__(self):
        self.display_width = 400
        self.display_height = 600
        self.WIN = pygame.display.set_mode((self.display_width, self.display_height))
        self.background = pygame.transform.scale(pygame.image.load(
            os.path.join('assets/GameObjects', 'background.png')), (self.display_width, self.display_height))
        self.bird = Bird(self.display_width // 2 - 21, self.display_height // 2)

    def display(self):
        self.WIN.blit(self.background, (0, 0))
        self.WIN.blit(self.bird.bird_image, (self.bird.x, self.bird.y))
        
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

            self.display()
            self.bird.update()
            pygame.display.update()

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

        






game = Main()
game.main()