# -*- coding: utf-8 -*-
#stdlib imports
import os

#local imports
from cls.config import Config
from cls.raycast import Raycast

#pygame imports
from pygame import Surface
from pygame import display
from pygame import locals as flags
from pygame import draw
from pygame import image
from pygame import transform
from pygame import font

class Display:
    screen = None
    size = None
    background = None
    minimap_surface = None
    minimap_scale = 10 

    texture_size = 64

    main_wall_texture = None
    wall_textures = None
    textures_count = None
    texture_types_count = None

    main_sprite_texture = None
    sprites_count = None
    sprites = None


    raycast = None

    default_font = None

    def __init__(self):
        self.screen = None
        self.size = None
        self.background = None
        self.minimap_surface = None

    def loadTextures(self):
        self.main_wall_texture = image.load(os.path.join('data', 'walls.png')).convert()
        main_texture_size = self.main_wall_texture.get_size()
        self.textures_count = round(main_texture_size[1]/self.texture_size)
        self.texture_types_count = round(main_texture_size[0]/self.texture_size)
        self.wall_textures = []
        for i in range(self.textures_count):
            texture_types = []
            for t in range(self.texture_types_count-1):
                texture_type = []
                x = t * self.texture_size
                y = i * self.texture_size
                for strip in range(self.texture_size):
                    texture_type.append(
                        self.main_wall_texture.subsurface((x, y, 1, self.texture_size)).convert()
                    )
                    x = x + 1
                texture_types.append(texture_type)
            self.wall_textures.append(texture_types)
        pass

        self.main_sprite_texture = image.load(os.path.join('data', 'sprites.png')).convert()
        self.sprites_count = self.main_sprite_texture.get_size()[0]//self.texture_size
        self.sprites = []
        for i in range(self.sprites_count):
            sprite = []
            x = i * self.texture_size
            y = 0
            for strip in range(self.texture_size):
                sprite.append(
                    self.main_sprite_texture.subsurface((x, y, 1, self.texture_size)).convert()
                )
                x = x + 1
            self.sprites.append(sprite)
        pass



    def initWindow(self, size = None):
        if (size == None):
            self.size = Config.screen_size
        display.init()
        font.init()
        self.screen = display.set_mode(
            self.size,
            flags.FULLSCREEN if Config.fullscreen else flags.RESIZABLE
        )
        display.set_caption(Config.screen_caption)

        #Initializing bachground surface
        self.background = Surface(self.size).convert()
        self.background.fill(Config.background_color)

        #Initializing raycast engine
        self.raycast = Raycast(self.size)

        self.loadTextures()

        self.default_font = font.SysFont('Arial', 15)

    def close(self):
        display.quit()
        #TODO:use

    def drawRaycastedView(self,rays):
        default_texture = 1
        default_type = 0
        strip_no = 0
        strip_width = self.raycast.strip_width
        x = 0
        last_slice_meta = (None, None, None, None)
        last_slice = None
        for ray in rays:
            this_slice_meta = (default_texture, default_type, ray['texture_x'], ray['distance'])
            if (this_slice_meta != last_slice_meta):
                last_slice_meta = this_slice_meta
                strip_height = round(self.raycast.distance_to_plane / ray['distance'])
                y = round((self.size[1]-strip_height)/2)
                required_slice = round((self.texture_size/strip_width)*ray['texture_x']) - 1
                try:
                    last_slice = transform.scale(self.wall_textures[default_texture][default_type][required_slice], (strip_width, strip_height))
                except Exception as e:
                    pass
            try:
                self.screen.blit(last_slice,(x,y))
            except Exception as e:
                pass

            x += strip_width
            strip_no = strip_no + 1


    def draw(self,game):
        self.clearScreen()
        rays = self.raycast.castRays(game.player, game.world)
        self.drawRaycastedView(rays)
        self.drawUpdatedMinimap(game.world, game.player, rays, (0,0))
        self.drawFPS(game.fps)
        self.finishDrawing()


    def clearScreen(self):
        self.screen.blit(self.background, (0, 0))

    def initMinimap(self, world):
        size = ((world.width+2) * self.minimap_scale,(world.height+2) * self.minimap_scale)
        self.minimap_surface = Surface(size).convert()
        self.prenderMinimap(world)

    def prenderMinimap(self, world):
        self.minimap_surface.fill((0, 0, 0))
        scale = self.minimap_scale
        y = scale # margin
        for row in world.world:
            x = scale
            for item in row:
                draw.rect(
                    self.minimap_surface,
                    item.map_color,
                    (x,y,scale,scale)
                )
                x = x + scale
            y = y + scale

    def drawUpdatedMinimap(self, world, player, rays, coords):
        scale = self.minimap_scale
        player_coords = ((player.coords+1) * scale).rounded().toInt().toTuple()
        player_direction = player.direction * scale
        player_direction = (player_direction + player_coords).rounded().toInt().toTuple()
        minimap = self.minimap_surface.copy()
        draw.circle(
            minimap,
            player.map_color,
            player_coords,
            round(player.size*scale)
        )
        for ray in rays:
            draw.line(
                minimap,
                (0,255,0),
                player_coords,
                ((ray['coords'][0]+1)*scale, (ray['coords'][1]+1)*scale)
        )
        draw.line(
            minimap,
            player.map_color,
            player_coords,
            player_direction
        )

        self.screen.blit(minimap, coords)


    def finishDrawing(self):
        display.flip()

    def drawFPS(self, fps):
        fps = round(fps)
        if (fps >= 40):
            fps_color = (0,102,0)
        elif(fps >= 20):
            fps_color = (255, 153, 0)
        else:
            fps_color = (204, 0, 0)
        self.screen.blit(
            self.default_font.render('FPS: '+str(fps), False, fps_color),
            (self.size[0]-70, 5)
        )


def main():
    pass

if __name__ == "__main__":
    #project root
    import sys
    sys.path.append('../')

    main()
