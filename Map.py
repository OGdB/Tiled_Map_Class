import json

class Map:
    """Class with functions to read map data from json files made with Tiled"""
    def __init__(self, json_path):
        self.layers = []

        with open(json_path, "r") as fp:
            raw_data = json.load(fp)
            self.tile_set = raw_data['tilesets'][0]

            # Get every layer and store in layers list
            map_height = raw_data['height']
            map_width = raw_data['width']
            for layer in raw_data['layers']:
                layer_in_lists = []
                layer_data = layer['data']
                for x in range(map_height):
                    start = x * map_width
                    end = start + map_width
                    sublist = layer_data[start:end]
                    layer_in_lists.append(sublist)

                self.layers.append(layer_in_lists)