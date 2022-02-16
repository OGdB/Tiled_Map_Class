import Map
import pygame
import SpriteSheet as Sprite

pygame.init()
this_map = Map.Map("map.json")

win_w = this_map.map_width * this_map.tile_width
win_h = this_map.map_height * this_map.tile_height
win = pygame.display.set_mode((win_w, win_h))
#clock = pygame.time.Clock()
#font = pygame.font.SysFont("Courier New", 20, True)

# Tile stuff
def unrotate_tile(tile_gid):
    return tile_gid & 0xFFFFFF  # strip all but the last 6 numbers from the binary of tile_gid and return that as a number

def get_tileset(tile_gid):
    if tile_gid != 0:
        for tileset in this_map.tile_sets:
            tile_set_start = tileset['firstgid']
            tile_set_end = tile_set_start + tileset['tilecount']
            if (tile_set_start <= tile_gid <= tile_set_end):
                # print(tileset['name'])
                return tileset
# Get sprites
# get the first tile of the first layer
# first_sprite = Sprite.SpriteSheet(tile_set_img).get_sprite(gid, 16, 16, 27)

# loop through every layer and store used tile and gid in dictionary
tiles = {}
for layer in this_map.layers:  # for every layer in the layers
    for row in layer:  # for every row in that layer
        for tile_gid in row:  # for every tile(gid) in that row
            if tile_gid not in tiles and tile_gid != 0:  # add the tile of that gid to the tile_dictionary if not in it
                tile = unrotate_tile(tile_gid)
                tile_set = get_tileset(tile)
                tile_image = pygame.image.load(tile_set['image'])
                tile_sprite = Sprite.SpriteSheet(tile_image).get_sprite(tile_gid, 16, 16, 27)
                tiles[tile_gid] = tile_sprite
print(tiles)
        # if tile is not already saved in dictionary
            # load original tile in variable
            # if (GIDTHINGY), flip original tile horizontally
            # elif (OTHERGIDTHINGY), flip original tile vertically,
            # if (FINALGIDTHINGY), rotate original tile diagonally
            # store the (rotated) image in dictionary with its gid
 # store the rotated images as separate images (not rotating the original every frame)


# print(this_map.layers[0][0])
string_unrotated = ""
for rots in this_map.layers[0][0]:
    string_unrotated += str(unrotate_tile(rots)) + " / "
# print(string_unrotated)


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
    #win.blit(first_sprite, (0, 0))

    pygame.display.flip()

pygame.quit()
