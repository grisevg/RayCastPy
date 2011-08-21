#project root
if __name__ == "__main__":
    import sys
    sys.path.append('../')

import math

#local imports
from cls.vector import Vector
from cls.controls import Controls
from cls.raycast import Raycast

class Player:
    #Constants
    CHAR = 'C'
    up_directions = ((-1, 0),(-1,-1),(0,-1),(1,-1),(1, 0))
    down_directions = ((-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0))
    top = Vector(0,-1)
    bottom = Vector(0,1)
    left = Vector(-1,0)
    right = Vector(1,0)
    #up_directions = (
    #    ((-1,-1),(0,-1),(1,-1)),
    #    ((-1, 0),       (1, 0)),
    #    ((-1, 1),(0, 1),(1, 1)),
    #)

    #Properties
    coords = None
    direction = None
    map_color = (255,0,0)
    movement_speed = 0.18
    rotation_speed = math.radians(6)
    size = 0.5

    def __init__(self, coords, direction = Vector(0,-1)):
        if (type(coords) != Vector):
            self.coords = Vector(coords)
        else:
            self.coords = coords.copy()
        self.coords

        if (type(coords) != Vector or not direction):
            direction = Vector(0,1)
        self.direction = direction.normalized()

        if self.size > 0.5:
            raise Exception('Collision algorithm does not support radius more than 0.5')

    def move(self, world, keys_state):
        if (keys_state[Controls.TURN_LEFT]):
            self.direction.rotate(-self.rotation_speed)
        elif (keys_state[Controls.TURN_RIGHT]):
            self.direction.rotate(self.rotation_speed)
        elif (keys_state[Controls.FORWARD] or keys_state[Controls.BACKWARD]):
            modifier = 1 if keys_state[Controls.FORWARD] else -1
            new_coords = self.coords + (self.direction*self.movement_speed*modifier)
            if not world.isBlocking(new_coords):
                self.coords = new_coords
            else:
                pass
                #self.coords = self.smartCollisionCheck(new_coords)

##    def smartCollisionCheck(self_size, world, coords, movement):
##        #if (movement.get_length() > 1):
##        #    raise Exception('Collision algorithm does not support movement for more than 1 unit')
##
##        new_cords = movement + coords
##
##        cross_left = (new_cords.x % 1 - self_size) > 0
##        cross_right = (new_cords.x % 1 + self_size) < 1
##
##        cross_up = False
##        cross_bottom = False
##        curr_cell = coords.floor()
##
##        if world.getItem(curr_cell+self.top):
##            cross_up = (new_cords.y % 1 - self_size)
##            if (cross_up > 0):
##                cross_vertical = cross_up
##                cross_up = True
##        elif world.getItem(curr_cell+self.bottom):
##            cross_bottom = (new_cords.y % 1 + self_size) < 1
##            if (cross_bottom > 0):
##                cross_vertical = cross_bottom
##                cross_bottom = True
##        else:
##            cross_vertical = 0
##
##        if cross_left:
##            cross_horizontal = cross_left
##        elif cross_right:
##            cross_horizontal = cross_right
##        else:
##            cross_horizontal = 0
##
##        #if cross_vertical:
##        #    movement.y = movement.y - cross_vertical
##
##        #if cross_horizontal:
##        #    movement.x = movement.x - cross_horizontal
##
##        if cross_vertical and cross_horizontal:
##            dx = (self_size - abs(cross_horizontal))
##            dy = (self_size - abs(cross_vertical))
##            d = math.sqrt(dx**2+dy**2)
##            if (d < self_size):
##                c = self_size/d
##                movement.y = movement.y - (c * dy - dy)
##                movement.x = movement.x - (c * dx - dx)
##
##
##        return movement

def main():
    pass

if __name__ == "__main__":
    main()
