from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.freddy import Freddy
from dino_runner.components.obstacles.fuego import Fuego
from dino_runner.components.obstacles.monster import Monster
from dino_runner.components.obstacles.zombi import Zombi

from dino_runner.utils.constants import BIRD, FREDDY, FUEGO, MONSTER, SMALL_CACTUS, ZOMBI
import pygame
import random
class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            rand = random.randint(0 ,5)
            if rand== 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif rand== 1 : 
                self.obstacles.append(Bird(BIRD))
            elif rand== 2 : 
                self.obstacles.append(Freddy(FREDDY))
            elif rand== 3 : 
                self.obstacles.append(Fuego(FUEGO))
            elif rand== 4 : 
                self.obstacles.append(Monster(MONSTER))
            elif rand== 5 : 
                self.obstacles.append(Zombi(ZOMBI))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count +=1 ##
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):###
        self.obstacles = []
        
