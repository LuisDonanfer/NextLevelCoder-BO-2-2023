import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import ZOMBI


class Zombi(Obstacle):

    def __init__(self, image_list):
        self.type = random.randint(0 ,1)
        super().__init__(image_list[self.type])
        self.rect.y = 320
        self.step_index = 0

    def draw(self,screen):
        self.image_list = ZOMBI[0] if self.step_index < 10 else ZOMBI[1]
        screen.blit(self.image_list,self.rect)
        self.step_index +=1
        if self.step_index >= 20:
            self.step_index = 0