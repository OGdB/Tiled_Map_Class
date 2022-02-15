import json

class Map:
    def __init__(self, json_path):
        self.raw_data = ""
        with open(json_path, "r") as fp:
            self.raw_data = json.load(fp)

    def get_map(self):
        """Get the map in the form of multiple lists"""
        lists = []
        map_height = self.raw_data['height']
        map_width = self.raw_data['width']
        first_layer_data = self.raw_data['layers'][0]['data']
        for x in range(map_height):
            start = x * map_width
            end = start + map_width
            sublist = first_layer_data[start:end]
            lists.append(sublist)

        return lists
            ## print out the tiles in ints
            # s = ""
            # for v in sublist:
            #     s += str(v) + " "
            # print(s)