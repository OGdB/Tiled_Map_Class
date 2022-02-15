import Map


def is_tile_rotated(tileset, tile):
    rotated = 0x20000000
    hor_flip = 0x80000000
    ver_flip = 0x40000000

    tilecount = tileset["tilecount"]
    if 0 < tile - rotated < tilecount:
        return tile - rotated
    if 0 < tile - hor_flip < tilecount:
        return tile - hor_flip
    if 0 < tile - ver_flip < tilecount:
        return tile - ver_flip
    if 0 < tile - (hor_flip + rotated) < tilecount:
        return tile - (hor_flip + rotated)
    if 0 < tile - (ver_flip + rotated) < tilecount:
        return tile - (ver_flip + rotated)

    return tile

this_map = Map.Map("data\jsonmap2.json")

print(this_map.layers[0][0])
string_unrotated = ""
for rots in this_map.layers[0][0]:
    string_unrotated += str(is_tile_rotated(this_map.tile_set, rots)) + " / "
print(string_unrotated)

