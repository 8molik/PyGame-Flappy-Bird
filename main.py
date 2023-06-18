import pygame
import os
from random import randint
from abc import ABC, abstractmethod

pygame.mixer.init()

# Global variables
FPS = 60
WIDTH, HEIGHT = 400, 600
GAP = 140

PIPE_SPEED = 1.5
PIPE_WIDTH, PIPE_HEIGHT = 65, 400
BIRD_WIDTH, BIRD_HEIGHT = 42, 29
NUMBER_WIDTH, NUMBER_HEIGHT = 24, 36
GAMEOV_WIDTH, GAMEOV_HEIGHT = 192, 42
BUTTON_WIDTH, BUTTON_HEIGHT = 107, 37
BASE_WIDTH, BASE_HEIGHT = WIDTH, 100
START_WIDTH, START_HEIGHT = WIDTH // 2 + 30, HEIGHT // 2 + 25

HIT = pygame.USEREVENT + 1

# Abstract class representing Game Object
class GameObject(ABC):
    def __init__(self, x = 0, y = 0, width = WIDTH, height = HEIGHT):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @abstractmethod
    def display(self, WIN):
        pass

    @abstractmethod
    def get_rect(self):
        pass

# Background
class Background(GameObject):
    def __init__(self, x = 0, y = 0, back_width = WIDTH, back_height = HEIGHT):
        super().__init__(x, y, back_width, back_height)
        self.back_image = pygame.transform.scale(pygame.image.load(
            os.path.join('assets/GameObjects', 'background.png')), (self.width, self.height))

    def display(self, WIN):
        WIN.blit(self.back_image, (self.x, self.y))

    def get_rect(self):
        pass

# Base of the screen
class Base(GameObject):
    def __init__(self, x, y, base_width = BASE_WIDTH, base_height = BASE_HEIGHT):
        super().__init__(x, y , base_width, base_height)
        self.base_image = pygame.transform.scale(pygame.image.load(
            os.path.join('assets/GameObjects', 'base.png')), (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def display(self, WIN):
        WIN.blit(self.base_image, (self.x, self.y))

    def get_rect(self):
        return self.rect

# Bird/player
class Bird(GameObject):
    def __init__(self, x, y, bird_width = BIRD_WIDTH, bird_height = BIRD_HEIGHT):
        super().__init__(x, y, bird_width, bird_height)
        self.bird_image = {'downflip': pygame.transform.scale(
                                          pygame.image.load(os.path.join('assets/GameObjects', 'bird-downflip.png')), (BIRD_WIDTH, BIRD_HEIGHT)),
                           'midflip': pygame.transform.scale(
                                          pygame.image.load(os.path.join('assets/GameObjects', 'bird-midflip.png')), (BIRD_WIDTH, BIRD_HEIGHT)),
                           'upflip': pygame.transform.scale(
                                          pygame.image.load(os.path.join('assets/GameObjects', 'bird-upflip.png')), (BIRD_WIDTH, BIRD_HEIGHT))}
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vel = 0
        self.image_name = 'downflip'
        self.image = self.bird_image[self.image_name]
    
    def jump(self): 
        if self.y > 0:
            self.vel = -8
        
    def update(self):
        self.y += self.vel
        self.vel += 0.5

        #Jump anitmation
        if self.vel < -4:
            self.image_name = 'upflip'
        elif self.vel < 0:
            self.image_name = 'midflip'
        else:
            self.image_name = 'downflip'

        self.image = self.bird_image[self.image_name]
        self.image = pygame.transform.rotate(self.image, self.vel * -2)
            
        if self.y >= (HEIGHT - BASE_HEIGHT - self.height):
            self.vel = 0

        # Updates current bird rect location
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def display(self, WIN):
        WIN.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return self.rect

# Pipe
class Pipe(GameObject):
    def __init__(self, x, y, rotate = False, pipe_width = PIPE_WIDTH, pipe_height = PIPE_HEIGHT):
        super().__init__(x, y, pipe_width, pipe_height)
        self.rotate = rotate
        self.pipe_image = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/GameObjects', 'pipe.png')), (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def display(self, WIN):
        if self.rotate:
            WIN.blit(pygame.transform.rotate(self.pipe_image, 180), (self.x, self.y))
        else:
            WIN.blit(self.pipe_image, (self.x, self.y))

    def move(self):
        self.x -= PIPE_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_rect(self):
        return self.rect

# Sound
class Sound:
    def __init__(self):
        self.sound = {'swoosh': pygame.mixer.Sound(os.path.join('assets/SoundEffects', 'swoosh.wav')),
                      'die': pygame.mixer.Sound(os.path.join('assets/SoundEffects', 'die.wav')),
                      'hit': pygame.mixer.Sound(os.path.join('assets/SoundEffects', 'hit.wav')),
                      'point': pygame.mixer.Sound(os.path.join('assets/SoundEffects', 'point.wav')),
                      'wing': pygame.mixer.Sound(os.path.join('assets/SoundEffects', 'wing.wav'))}
                
    def play_sound(self, name):
        self.sound[name].play()

# Score   
class Score:
    def __init__(self, score = 0):
        self.score = score
        self.numbers = {"0" : pygame.image.load(os.path.join('assets/UI/Numbers', '0.png')),
                        "1" : pygame.image.load(os.path.join('assets/UI/Numbers', '1.png')),
                        "2" : pygame.image.load(os.path.join('assets/UI/Numbers', '2.png')),
                        "3" : pygame.image.load(os.path.join('assets/UI/Numbers', '3.png')),
                        "4" : pygame.image.load(os.path.join('assets/UI/Numbers', '4.png')),
                        "5" : pygame.image.load(os.path.join('assets/UI/Numbers', '5.png')),
                        "6" : pygame.image.load(os.path.join('assets/UI/Numbers', '6.png')),
                        "7" : pygame.image.load(os.path.join('assets/UI/Numbers', '7.png')),
                        "8" : pygame.image.load(os.path.join('assets/UI/Numbers', '8.png')),
                        "9" : pygame.image.load(os.path.join('assets/UI/Numbers', '9.png'))}
        self.number = self.numbers['0']

    def update_score(self):
        self.score += 1
        self.number = self.generate_number()   

    def generate_number(self):
        num = str(self.score)
        # List of number pictures
        images = []  

        for digit in num:
            image = self.numbers[digit].convert_alpha() 
            image.set_alpha(255)
            images.append(image)
    
        # Creating picture of multiple numbers
        number_surface = pygame.Surface((len(num) * NUMBER_WIDTH, NUMBER_HEIGHT), pygame.SRCALPHA)
        x_offset = 0
        for image in images:
            number_surface.blit(image, (x_offset, 0))
            x_offset += image.get_width()
        return number_surface

    def display_score(self, WIN):
        WIN.blit(self.number, (WIDTH // 2 - 10, 50))

# Menu - starting and ending screens
class Menu:
    def __init__(self):
        self.x =  WIDTH // 4
        self.y = HEIGHT // 4
        self.height = HEIGHT
        self.width = WIDTH
        self.start = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/UI', 'message.png')), (START_WIDTH, START_HEIGHT))
        self.game_over = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/UI', 'gameover.png')), (GAMEOV_WIDTH, GAMEOV_HEIGHT))
        self.restart_button = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/UI', 'restart.png')), (BUTTON_WIDTH, BUTTON_HEIGHT))
        self.restart_rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)

    def display_start(self, WIN):
        WIN.blit(self.start, (WIDTH // 2 - START_WIDTH // 2, HEIGHT // 4  - BIRD_HEIGHT * 2 + 2))
    
    def display_end(self, WIN):
        WIN.blit(self.game_over, (WIDTH // 2 - GAMEOV_WIDTH // 2, HEIGHT // 4))
        WIN.blit(self.restart_button, (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2))
        self.restart_rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)

class Main:
    def __init__(self):
        self.background = Background(0, 0)
        self.bird = Bird(WIDTH // 2 - 21, HEIGHT // 2)
        self.base = Base(0, HEIGHT - 100)
        self.score = Score()
        self.menu = Menu()
        self.sound = Sound()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.pipes = []
        self.generate_pipes()
        self.game_started = False
        self.game_ended = False
    
    def generate_pipes(self):
        i_top = randint(-350, -100)
        i_bot = i_top + GAP + PIPE_HEIGHT

        # Pair of top pipe and bottom pipe
        self.pipes.append((Pipe(WIDTH, i_top, True), Pipe(WIDTH, i_bot)))
    
    def handle_hits(self, bird_rect):
        if bird_rect.colliderect(self.base.get_rect()):
            pygame.event.post(pygame.event.Event(HIT))
        else: 
            for pipe_pair in self.pipes:
                pipe_top, pipe_bot = pipe_pair
                pipe_top_rect = pipe_top.get_rect()
                pipe_bot_rect = pipe_bot.get_rect()
        
                if bird_rect.colliderect(pipe_top_rect) or bird_rect.colliderect(pipe_bot_rect):
                    pygame.event.post(pygame.event.Event(HIT))       

    def display(self):
        self.background.display(self.WIN)
        if self.game_started:
            for pipe_pair in self.pipes:
                pipe_pair[0].display(self.WIN)
                pipe_pair[1].display(self.WIN)
            self.score.display_score(self.WIN)
        else:
            self.menu.display_start(self.WIN)
        if self.game_ended:
            self.menu.display_end(self.WIN)
        self.bird.display(self.WIN)
        self.base.display(self.WIN)
        pygame.display.update()

    def handle_pipes(self):
        pipes_to_remove = []
        for i in range(len(self.pipes)):
            if self.pipes[i][0].x == WIDTH // 2 - 1:
                self.generate_pipes()
                self.score.update_score()
                self.sound.play_sound("point")
            elif self.pipes[i][0].x < -65:
                pipes_to_remove.append(self.pipes[i])

        for pipe in pipes_to_remove:
            self.pipes.remove(pipe)    

    def main(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        clock = pygame.time.Clock()

        run = True

        while run:
            bird_rect = self.bird.get_rect()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.game_ended:
                        if not self.game_started: 
                            self.game_started = True                            
                        self.bird.jump()
                        self.sound.play_sound("wing")
                                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_ended:
                        mouse_pos = pygame.mouse.get_pos()
                        button_rect = self.menu.restart_rect
                        if button_rect.collidepoint(mouse_pos):
                            if pygame.mouse.get_pressed()[0] == 1:
                                self.sound.play_sound("swoosh")
                                self.__init__()
                            
                if event.type == HIT:
                    if not self.game_ended:
                        self.sound.play_sound("hit")
                    self.bird.update()
                    self.game_ended = True
                    
            if self.game_started:
                if not self.game_ended:
                    for pipe_pair in self.pipes:
                        pipe_pair[0].move()
                        pipe_pair[1].move()
                
                self.handle_hits(bird_rect)
                self.handle_pipes()
                self.bird.update()

            self.display()
            clock.tick(FPS)

if __name__ == '__main__':
    game = Main()
    game.main()