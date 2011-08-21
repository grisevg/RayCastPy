#local imports
from cls.space.space import Space

class Sprite(Space):
    #Constants
    CHAR = '?'
    EMPTY = False
    TRANSPARENT = True

    #Properties
    coords = None
    height = 1
    map_color = None
    type = "Sprite-Abstract"


def main():
    pass

if __name__ == '__main__':
    main()