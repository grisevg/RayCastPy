#local imports
from cls.space.sprite import Sprite

class Test_sprite(Sprite):
    #Constants
    CHAR = 'X'
    EMPTY = False
    TRANSPARENT = True

    #Properties
    coords = None
    height = 1
    map_color = (0,0,128)
    type = "Sprite"


def main():
    pass

if __name__ == '__main__':
    main()