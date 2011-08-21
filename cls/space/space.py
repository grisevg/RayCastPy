class Space:
    #Constants
    CHAR = '?'
    EMPTY = None
    TRANSPARENT = None

    #Properties
    coords = None
    height = 1
    map_color = None
    type = "Space-Abstract"


    def __init__(self, coords):
        self.height = 1
        self.coords = coords

    def __str__(self):
        return self.CHAR

    def isEmpty(self):
        return self.EMPTY

    def isTransparent(self):
        return self.TRANSPARENT

def main():
    pass

if __name__ == '__main__':
    main()