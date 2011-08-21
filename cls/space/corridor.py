#local imports
from cls.space.space import Space

class Corridor(Space):
    #Constants
    CHAR = " "
    STARTING_POINT_CHAR = 'S'
    EMPTY = True
    TRANSPARENT = True


    #Propetioes
    is_starting_point = None
    map_color = (204,204,204)
    type = "Corridor"

    #def __init__(self):
    #    pass

    def __str__(self):
        if (self.is_starting_point):
            return self.STARTING_POINT_CHAR
        else:
            return self.CHAR



def main():
    pass

if __name__ == '__main__':
    main()