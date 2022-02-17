import Map
import pygame
import sys
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
    """Return the tileset whic the provided gid is from"""
    if tile_gid != 0:
        for tile_set in this_map.tile_sets:
            tile_set_start = tile_set['firstgid']
            tile_set_end = tile_set_start + tile_set['tilecount'] - 1
            if (tile_set_start <= tile_gid <= tile_set_end):
                # print(tile_set['name'])
                return tile_set

def pretty_print(column_sizes, *values):
    i = 0
    for val in values:
        if i < len(column_sizes):
            column_size = column_sizes[i]
        else:
            column_size = 10
        val_as_str = str(val)
        if len(val_as_str) < column_size:
            val_as_str = " " * (column_size - len(val_as_str)) + val_as_str
        print(val_as_str, end="")
        i += 1


special_codes = {0: "normal", 3: "rot90", 6: "rot180", 5: "rot270", 4: "flipH", 2: "flipV", 1: "flipH+rot90", 7: "flipH+rot270"}
def decipher(gid):
    raw_number = gid
    bin_value = bin(raw_number)  # Convert the int raw_number to the binary equivalent
    hex_value = hex(raw_number)  # Convert the int raw_number to the hexadecimal equivalent

    # This is to simulate what *you* might do to decipher if a given code is rotated, etc.
    real_code = raw_number & 0x1FFFFFFF  # This "masks" off the low-order 29 bits (reserved for the code)
    special_flags = raw_number & 0xE0000000  # This "masks" off the high-order 5 bits (everything but the real_code)
    special_flags = special_flags >> 29  # Not technically necessary, but this "shifts" the special flags
    # bits to the right 29 binary digits (making the values less big)
    deciphered_operation = special_codes[special_flags]

    # special_flags_meaning =
    pretty_print((11, 35, 13, 5, 6, 2, 14), raw_number, bin_value, hex_value, real_code, bin(special_flags),
                 special_flags, deciphered_operation)

def return_real_gid(gid):
    return gid & 0x1FFFFFFF  # This "masks" off the low-order 29 bits (reserved for the code)

def get_rotation(raw_gid):
    special_flags = raw_gid & 0xE0000000  # This "masks" off the high-order 5 bits (everything but the real_code)
    special_flags = special_flags >> 29  # Not technically necessary, but this "shifts" the special flags
    # bits to the right 29 binary digits (making the values less big)
    return special_codes[special_flags]

raw_gid = this_map.layers[0][0][1]
print(f"raw: {raw_gid}")
print(f"rotation: {get_rotation(raw_gid)}")
real = return_real_gid(raw_gid)
print(f"real: {real}")

# Deciper and put each tile into its own dictionary.
# for layer in this_map.layers:
#     for rows in layer:
#         for tile_gid in rows:
#             if tile_gid != 0:
#                 decipher(tile_gid)
#                 print()

# loop through every layer and store used tile and gid in dictionary
tiles = {}
for layer in this_map.layers:  # for every layer in the layers
    for row in layer:  # for every row in that layer
        for tile_gid in row:  # for every tile(gid) in that row
            if tile_gid not in tiles and tile_gid != 0:  # add the tile of that gid to the tile_dictionary if not in it
                real_tile = return_real_gid(tile_gid)
                tile_set = get_tileset(real_tile)
                tile_image = pygame.image.load(tile_set['image'])
                tile_sprite = Sprite.SpriteSheet(tile_image).get_sprite(tile_gid, 16, 16, tile_set['columns'])
                rotation_flag = get_rotation(tile_gid)
                # Rotate tilesprite according to gid
                if rotation_flag == 'rot90':
                    # rotate 90
                    tile_sprite = pygame.transform.rotate(tile_sprite, 90)
                    pass
                if rotation_flag == 'rot180':
                    # rotate 180
                    tile_sprite = pygame.transform.rotate(tile_sprite, 180)
                    pass
                if rotation_flag == 'rot270':
                    # rotate 270
                    tile_sprite = pygame.transform.rotate(tile_sprite, 270)
                    pass
                if rotation_flag == 'flipH':
                    # flip horizontally
                    tile_sprite = pygame.transform.flip(tile_sprite, True, False)
                    pass
                if rotation_flag == 'flipV':
                    # flip vertically
                    tile_sprite = pygame.transform.flip(tile_sprite, False, True)
                    pass
                if rotation_flag == 'flipH+rot90':
                    # rotate flip and rotate 90
                    tile_sprite = pygame.transform.flip(tile_sprite, True, False)
                    tile_sprite = pygame.transform.rotate(tile_sprite, 90)
                    pass
                if rotation_flag == 'flipH+rot270':
                    # rotate flip and rotate 270
                    tile_sprite = pygame.transform.flip(tile_sprite, True, False)
                    tile_sprite = pygame.transform.rotate(tile_sprite, 270)
                    pass

                tiles[tile_gid] = tile_sprite
                #tiles[tile_gid] = rotation_flag
print(tiles)

# UPDATE
done = True
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
