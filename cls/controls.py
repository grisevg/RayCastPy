#project root
if __name__ == "__main__":
    import sys
    sys.path.append('../')

#local imports
from cls.display import Display

#pygame imports
from pygame import event as event
from pygame import locals as keys

class Controls:
    #Constants
    FORWARD = 0
    BACKWARD = 1
    TURN_LEFT = 2
    TURN_RIGHT = 3
    ESCAPE = 4

    #Properties
    gamepad_keys = {}
    keyboard_keys = {}
    keys_state = {}
    gamepad_enabled = False

    def __init__(self):
        #pygame.joystick.init()
        self.gamepad_keys = {}
        self.keys_state = {}
        self.gamepad_enabled = False
        self.loadConfig()



    def getInput(self):
        return self.getKeyboardInut()


    def loadConfig(self):
        self.keyboard_keys = {
            keys.K_UP:self.FORWARD,
            keys.K_DOWN:self.BACKWARD,
            keys.K_LEFT:self.TURN_LEFT,
            keys.K_RIGHT:self.TURN_RIGHT,
            keys.K_ESCAPE:self.ESCAPE,
        }
        self.keys_state = {
            self.FORWARD:False,
            self.BACKWARD:False,
            self.TURN_LEFT:False,
            self.TURN_RIGHT:False,
            self.ESCAPE:False,
        }

    def getKeyboardInut(self):
        events = event.get((keys.KEYUP, keys.KEYDOWN))
        for e in events:
            if (e.key in self.keyboard_keys):
                self.keys_state[self.keyboard_keys[e.key]] = (e.type == keys.KEYDOWN)
        return self.keys_state




    #def getGamepadInut(self):
    #    events = pygame.event.get((keys.JOYBUTTONUP, keys.JOYBUTTONDOWN))


def main():
    pass
##    import os
##    from pygame import init as init
##
##    init()
##    display = Display()
##    display.initWindow()
##    controls = Controls()
##
##    while 1:
##        os.system(['clear','cls'][os.name == 'nt'])
##        controls.getInput()
##        for key, state in controls.keys_state.items():
##            print("key:"+str(key)+" state:"+str(state))

if __name__ == "__main__":
    main()
