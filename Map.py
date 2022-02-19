import json
import pygame
import SpriteSheet as Sprite

def return_real_gid(gid):
    return gid & 0x1FFFFFFF  # This "masks" off the low-order 29 bits (reserved for the code)

special_codes = {0: "normal", 3: "rot90", 6: "rot180", 5: "rot270", 4: "flipH", 2: "flipV", 1: "flipH+rot90",
                 7: "flipH+rot270"}
def get_rotation(raw_gid):
    special_flags = raw_gid & 0xE0000000  # This "masks" off the high-order 5 bits (everything but the real_code)
    special_flags = special_flags >> 29  # Not technically necessary, but this "shifts" the special flags
    # bits to the right 29 binary digits (making the values less big)
    return special_codes[special_flags]

class Map:
    """Class with functions to read map data from json files made with Tiled"""
    def __init__(self, json_path):
        with open(json_path, "r") as fp:
            raw_data = json.load(fp)
            self.map_width = raw_data['width']
            self.map_height = raw_data['height']
            self.tile_sets = []
            for tile_set in raw_data['tilesets']:
                self.tile_sets.append(tile_set)
            self.tile_width = raw_data['tileheight']
            self.tile_height = raw_data['tilewidth']

            # Get every layer and store in layers list
            self.layers = []
            map_height = raw_data['height']
            map_width = raw_data['width']
            for layer in raw_data['layers']:
                layer_in_lists = []
                layer_data = layer['data']
                for y in range(map_height):  # get the row for every y-unit
                    start = y * map_width
                    end = start + map_width
                    sublist = layer_data[start:end]
                    layer_in_lists.append(sublist)

                self.layers.append(layer_in_lists)

    def get_tileset(self, tile_gid):
        """Return the tileset whic the provided gid is from"""
        if tile_gid != 0:
            for tile_set in self.tile_sets:
                tile_set_start = tile_set['firstgid']
                tile_set_end = tile_set_start + tile_set['tilecount'] - 1
                if tile_set_start <= tile_gid <= tile_set_end:
                    return tile_set

    # loop through every layer and store used tile and gid in dictionary
    def load_used_tiles(self):
        used_tiles = {}
        for layer in self.layers:  # for every layer in the layers
            for row in layer:  # for every row in that layer
                for tile_gid in row:  # for every tile(gid) in that row
                    if tile_gid not in used_tiles and tile_gid != 0:  # add the tile of that gid to the tile_dictionary if not in it
                        real_tile = return_real_gid(tile_gid)
                        tile_set = self.get_tileset(real_tile)
                        local_gid = real_tile - tile_set['firstgid']
                        tile_image = pygame.image.load(tile_set['image'])
                        tile_sprite = Sprite.SpriteSheet(tile_image).get_sprite(local_gid, 16, 16, tile_set['columns'])
                        rotation_flag = get_rotation(tile_gid)

                        # Rotate tilesprite according to gid
                        if rotation_flag == 'rot90':
                            tile_sprite = pygame.transform.rotate(tile_sprite, 90)

                        if rotation_flag == 'rot180':
                            tile_sprite = pygame.transform.rotate(tile_sprite, 180)

                        if rotation_flag == 'rot270':
                            tile_sprite = pygame.transform.rotate(tile_sprite, 270)

                        if rotation_flag == 'flipH':
                            tile_sprite = Sprite.SpriteSheet(tile_sprite).flip_sprite(True, False)

                        if rotation_flag == 'flipV':
                            tile_sprite = Sprite.SpriteSheet(tile_sprite).flip_sprite(False, True)

                        if rotation_flag == 'flipH+rot90':
                            tile_sprite = Sprite.SpriteSheet(tile_sprite).flip_sprite(True, False)
                            tile_sprite = pygame.transform.rotate(tile_sprite, 90)

                        if rotation_flag == 'flipH+rot270':
                            tile_sprite = Sprite.SpriteSheet(tile_sprite).flip_sprite(True, False)
                            tile_sprite = pygame.transform.rotate(tile_sprite, 270)

                        used_tiles[tile_gid] = tile_sprite
        return used_tiles

    def draw_map(self, win, tiles):
        for layer_index in range(len(self.layers)):  # for every layer in the layers
            this_layer = self.layers[layer_index]
            for row_index in range(len(this_layer)):
                this_row = this_layer[row_index]
                tile_y_pos = row_index * 16
                for tile_index in range(len(this_row)):
                    this_tile = this_row[tile_index]
                    if this_tile != 0:
                        tile_x_pos = tile_index * 16
                        win.blit(tiles[this_tile], (tile_x_pos, tile_y_pos))