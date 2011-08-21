import math

from cls.vector import Vector

class Raycast:
    #Pre-calculated values
    twoPI = math.pi*2
    rad90deg = math.radians(90)
    rad270deg = math.radians(270)

    FOV = math.radians(60)

    plane_width = None
    plane_height = None
    distance_to_plane = None
    center_x = None
    center_y = None

    strip_width = 1
    rays_number = None
    rays_angle = None

    world_elem_size = None

    view_angle_tan = None

    def __init__(self,plane_size):
        self.initProjectionPlane(plane_size)

    def initProjectionPlane(self, plane_size):
        self.plane_width, self.plane_height = plane_size
        self.center_x = self.plane_width // 2
        self.center_y = self.plane_height // 2

        self.distance_to_plane = self.center_x / math.tan(self.FOV/2)

        self.rays_number = math.ceil(self.plane_width / self.strip_width)
        self.rays_angle = self.FOV / self.plane_width

        self.half_rays_number = self.rays_number//2


    def castRays(self, player, world):
        rays = []
        player_angle = player.direction.get_angle()
        for i in range(self.rays_number):
            ray_screen_pos = (-self.half_rays_number+i) * self.strip_width
            ray_angle = math.atan(ray_screen_pos / self.distance_to_plane)
            ray = self.castRay(player.coords, player_angle, ray_angle, world)
            if ray['distance'] >= 0:
                rays.append(ray)
            else:
                raise Exception('OMFG!')
        return rays


    def castRay(self, player_coords, player_angle, ray_angle, world):
        fishbowl_fix = math.cos(ray_angle);

        ray_angle = player_angle + ray_angle

        dist = None
        texture_x = -1
        x_hit = -1
        y_hit = -1

        #Make shure angle between 0 and 2PI
        ray_angle = Vector.get_positive_angle(None, ray_angle)
        #ray_angle = math.copysign((abs(ray_angle) % self.twoPI), ray_angle)
        #if (ray_angle < 0):
        #    ray_angle += self.twoPI

        #Get directions which ray is faced
        faced_right = Vector.faced_right(None, ray_angle)
        faced_up = not Vector.faced_up(None, ray_angle) #Becouse screen coords and math coords inversive
        #faced_right = (ray_angle < self.rad90deg or ray_angle > self.rad270deg)
        #faced_up = (ray_angle > math.pi)

        #Vertical colission
        slope = math.tan(ray_angle)

        x_step = 1 if faced_right else -1
        y_step = x_step * slope

        x = math.ceil(player_coords.x) if faced_right else math.floor(player_coords.x)
        y = player_coords.y + ((x - player_coords.x) * slope)
        while (0 < x < world.width and 0 < y < world.height):
            wall_x = math.floor(x)
            if not faced_right:
                wall_x = wall_x - 1
            wall_y = math.floor(y)

            wall = world.getItem(wall_x,wall_y)
            if not wall.isTransparent():
                dist_x = x - player_coords.x
                dist_y = y - player_coords.y
                dist = dist_x**2 + dist_y**2 # the distance from the player to this point, squared.
                texture_x = y % 1
                if (not faced_right): #if we're looking to the left side of the map, the texture should be reversed
                    texture_x = 1 - texture_x
                x_hit = x
                y_hit = y
                wall_hit = wall
                break

            x = x + x_step
            y = y + y_step


        #Horizontal colission
        if slope != 0:
            slope = 1 / slope
        else:
            slope = 0

        y_step = -1 if faced_up else 1
        x_step = y_step * slope

        y = math.floor(player_coords.y) if faced_up else math.ceil(player_coords.y)
        x = player_coords.x + ((y - player_coords.y) * slope)

        while (0 < x < world.width and 0 < y < world.height):
            wall_y = math.floor(y)
            if faced_up:
                wall_y = wall_y - 1
            wall_x = math.floor(x)

            wall = world.getItem(wall_x,wall_y)
            if not wall.isTransparent():
                dist_x = x - player_coords.x
                dist_y = y - player_coords.y
                hor_dist = dist_x**2 + dist_y**2 # the distance from the player to this point, squared.
                if (dist == None or hor_dist < dist):
                    dist = hor_dist
                    texture_x = x % 1
                    if (faced_up): #if we're looking to the left side of the map, the texture should be reversed
                        texture_x = 1 - texture_x
                    x_hit = x
                    y_hit = y
                    wall_hit = wall
                break

            x = x + x_step
            y = y + y_step

        dist = math.sqrt(dist)*fishbowl_fix

        result = {'distance':dist, 'texture_x':texture_x, 'coords':(x_hit,y_hit), 'wall':wall_hit}
        return result

def main():
    pass


if __name__ == '__main__':
    main()
