import math

#Screen Res
width, height = 1024, 576
half_width = width // 2
half_height = height // 2
fps = 60

tile_size = width // 16

#player settings
player_pos = 1.5, 5 #minimap
player_speed = 0.002
player_angle = 0
player_rotation_speed = 0.002

#raycasting
fov = math.pi / 3
half_fov = fov / 2
ray_num = width // 2
half_ray_num = ray_num // 2
delta_angle = fov / ray_num
max_depth = 20

#3d projection
screen_dist = half_width / math.tan(half_fov)
scale = width // ray_num