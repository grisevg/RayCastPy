#stlib imports
#from random import random
#import os

#pygame imports
#import pygame
from pygame.time import Clock

#local imports
from cls.world import World
from cls.player import Player
from cls.display import Display
from cls.controls import Controls
from cls.vector import Vector

class Game:
    #Constants

    #Properties
    world = None
    player = None
    display = None
    controls = None
    clock = None
    is_running = False
    fps = -1



    def __init__(self):
        self.world = World()
        self.display = Display()
        self.controls = Controls()
        self.clock = Clock()
        self.fps = -1
        #self.is_running = False ?

    def init(self):
        self.display.initWindow()
        self.world.loadTextWorld('sample')
        self.display.initMinimap(self.world)
        self.player = Player(Vector(self.world.starting_point)+0.5)


    def startLoop(self):
        time_to_exit = False
        while not time_to_exit:
            self.clock.tick(30)
            self.fps = self.clock.get_fps()
            keys = self.controls.getInput()
            self.player.move(self.world, keys)
            self.display.draw(self)
            time_to_exit = keys[self.controls.ESCAPE]

    def close(self):
        self.display.close()

def main():
    pass

if __name__ == '__main__':
    main()
