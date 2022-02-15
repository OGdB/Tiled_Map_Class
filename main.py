import json

with open("data\jsonmap.json", "r") as fp:
    raw_data = json.load(fp)
    if "width" in raw_data:
        map_width = raw_data['width']
    map_height = raw_data['height']

    first_layer = raw_data['layers'][0]
    first_layer_data = first_layer['data']
    first_layer_height = first_layer['height']
    first_layer_width = first_layer['width']
    # print(first_layer_data)
    # print(first_layer_height)

    all_tilesets = raw_data['tilesets']
    first_gid = all_tilesets[0]['firstgid']
    tileset_name = all_tilesets[0]['name']

    # print 1 layer in numbers
    y = 0
    for x in range(map_height):
        start = x * (map_width - 1)
        end = start + map_width
        sublist = first_layer_data[start:end]

        print(first_layer_data)