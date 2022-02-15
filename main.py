import Map
import pygame
import SpriteSheet as Sprite

pygame.init()
this_map = Map.Map("data/jsonmap2.json")
tile_map = Sprite.SpriteSheet(this_map.tile_set)

win_w = this_map.map_width * this_map.tile_width
win_h = this_map.map_height * this_map.tile_height
win = pygame.display.set_mode((win_w, win_h))
#clock = pygame.time.Clock()
#font = pygame.font.SysFont("Courier New", 20, True)

# Tile stuff
def is_tile_rotated(tile_set, tile):
    rotated = 0x20000000
    hor_flip = 0x80000000
    ver_flip = 0x40000000

    tile_count = tile_set["tilecount"]
    if 0 < tile - rotated < tile_count:  # rotated diagonally
        return tile - rotated
    if 0 < tile - hor_flip < tile_count:  # horizontally flipped
        return tile - hor_flip
    if 0 < tile - ver_flip < tile_count:  # Vertically flipped
        return tile - ver_flip
    if 0 < tile - (hor_flip + rotated) < tile_count:  # horizontally flipped & rotated diagonally
        return tile - (hor_flip + rotated)
    if 0 < tile - (ver_flip + rotated) < tile_count: # vertically flipped & rotated diagonally
        return tile - (ver_flip + rotated)

    return tile

# Get sprites
tile_set_img = pygame.image.load("data/tilemap_packed.png")
# get the first tile of the first layer
gid = is_tile_rotated(this_map.tile_set, this_map.layers[0][0][0])
print(f"gid: {gid}")
first_sprite = Sprite.SpriteSheet(tile_set_img).get_sprite(gid, 16, 16, 27)


print(this_map.layers[0][0])
string_unrotated = ""
for rots in this_map.layers[0][0]:
    string_unrotated += str(is_tile_rotated(this_map.tile_set, rots)) + " / "
print(string_unrotated)

# UPDATE
done = False
while not done:
    #delta_time = clock.tick() / 1000

    # INPUT
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        done = True
    all_keys = pygame.key.get_pressed()
    if all_keys[pygame.K_ESCAPE]:
        done = True

    # DRAWING
    win.fill((0, 0, 0))

    # OBJECTS
    # for row_num in range(self.map_height):
    #     # render row of tiles
    #     for col_num in range(self.map_width):
    #         # render one tile
    #         cur_code = cur_layer[row_num][col[num]]
    #         # cur_code is a tile-code (like 14 or 0)
    #         dest_pos = (???, y)
    #         src_area = (???, ???)
    #         surf.blit(???, dest_pos, src_area)
    win.blit(first_sprite, (0, 0))

    pygame.display.flip()

pygame.quit()
