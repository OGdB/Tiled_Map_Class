import json

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
