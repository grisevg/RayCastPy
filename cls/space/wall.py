#local imports
from cls.space.space import Space

class Wall(Space):
    CHAR = "#"
    EMPTY = False
    TRANPARENT = False
    map_color = (51,51,51)
    texture_no = 0

    #def __init__(self):
    #    pass

def main():
    pass

if __name__ == '__main__':
    main()