import pygame
import os

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800


class Bird:
    IMAGES = None
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = 0
        self.img_count = 0
        self.mg = self.IMAGES[0]
