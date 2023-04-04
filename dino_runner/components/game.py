import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cl = 200
        self.y_pos_cl = 100
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input) #update de la clase dinosaur
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.cloud()
        self.player.draw(self.screen) #draw de la clase dinusaur
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cl, self.y_pos_cl))
        if self.x_pos_cl < -image_width:
            self.x_pos_cl = SCREEN_WIDTH
        self.x_pos_cl -= self.game_speed
        

    def draw_background(self):
        image_width = BG.get_width() #obtiene el ancho de la imagen
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
