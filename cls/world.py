#project root
if __name__ == "__main__":
    import sys
    sys.path.append('../')

#local imports
from cls.space.wall import Wall
from cls.space.corridor import Corridor
from cls.vector import Vector

#stlib imports
from os.path import dirname
from math import floor, ceil

class WorldParserException(Exception):
    pass

class World:
    world = []
    starting_point = None
    width = None
    height = None


    WALL_CHAR = '#'
    SPACE_CHAR = ' '
    STARTING_POINT_CHAR = 'S'


    def __init__(self):
        self.world = []
        self.starting_point = None

    def getItem(self,x_y_as_vector, y = None):
        if isinstance(x_y_as_vector, Vector):
            coords = x_y_as_vector.floor().toInt()
            return self.world[coords.y][coords.x]
        else:
            return self.world[y][x_y_as_vector]


    def doesNotCollide(self, coords, size):
        coords = coords.copy()
        if size <= 1:
            if self.getItem(coords.copy().floor()).isEmpty():
                coords2 = coords.copy()
                coords2.x += size
                if self.getItem(coords2.floor()).isEmpty():
                    coords.y += size
                    if self.getItem(coords.copy().floor()).isEmpty():
                        coords.x += size
                        if self.getItem(coords.copy().floor()).isEmpty():
                            return True
            return False
        else:
            raise NotImplementedError()


    def isBlocking(self, vector):
        if not (0 < vector.x < self.width and 0 < vector.y < self.height):
            return True

        return (not self.getItem(vector.copy().floor()).isEmpty())

    def loadTextWorld(self, worldname):
        path = dirname(__file__)+'/../text_worlds/'
        world_file = open(path+worldname+'.world', 'r')
        lines = world_file.readlines()

        new_world = []
        world_width = len(lines[0].strip())
        y = 0

        for line in lines:
            line = line.strip()
            x = 0
            new_world.append([])
            if (len(line) != world_width):
                pass
                raise WorldParserException('world file has to have same length in each row')
            for char in line:
                if (char == Wall.CHAR):
                    item = Wall((x,y))
                elif (char == Corridor.CHAR):
                    item = Corridor((x,y))
                elif (char == Corridor.STARTING_POINT_CHAR):
                    item = Corridor((x,y))
                    item.is_starting_point = True
                    self.starting_point = ((x,y))
                else:
                    raise WorldParserException('unsupported char in world file - "'+char+'" '+str((x,y)))
                new_world[y].append(item)
                x += 1
            y += 1

        if (not self.starting_point):
            raise WorldParserException('starting point is not defined in world file')

        self.world = new_world
        self.recalculateSize()
        return True

    def recalculateSize(self):
        self.height = len(self.world)
        self.width = len(self.world[0])

        return True

    def getSize(self):
        return (self.width, self.height)

    def __str__(self):
        result = ''
        for row in self.world:
            for item in row:
                result += str(item)
            result += '\n'
        return result

    def getWorldAsCharList(self):
        result = []
        i = 0
        for row in self.world:
            result.append([])
            for item in row:
                result[i].append(str(item))
            i += 1
        return result

    def generatedLevel(self):
        raise NotImplementedError()

def main():
    a = World()
    a.loadTextWorld('sample')
    print(a)

if __name__ == "__main__":
    main()
