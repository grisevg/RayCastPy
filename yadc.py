#from cls.game import Game
from cls.game import Game

def main():
    game = Game()
    game.init()
    game.startLoop()
    game.close()

if __name__ == '__main__':
    main()
