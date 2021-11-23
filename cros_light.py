import pygame
from map import world_map
from setting import *
class Light:
    def __init__(self):
        self.red=RED
        self.green=GREEN
        self.yellow=YELLOW
    @property
    def stan(self):
        return self.yellow
