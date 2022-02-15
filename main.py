import Map

this_map = Map.Map("data\jsonmap2.json")

print(this_map.tile_set['name'])

for l in this_map.layers:  # print first layer
    for t in l:
        print(t)
    print("\n")
