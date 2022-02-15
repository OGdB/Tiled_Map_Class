import Map
import pygame
import SpriteSheet as Sprite

pygame.init()

win_w = 800
win_h = 600
win = pygame.display.set_mode((win_w, win_h))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier New", 20, True)

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

this_map = Map.Map("data/jsonmap2.json")

# Get sprites
tile_set_img = pygame.image.load("data/tilemap_packed.png")
# get the first tile of the first layer
gid = is_tile_rotated(this_map.tile_set, this_map.layers[0][1][0])
print(f"gid: {gid}")
first_sprite = Sprite.SpriteSheet(tile_set_img).get_sprite(gid, 16, 16, 27)

print(this_map.layers[0][0])
string_unrotated = ""
for rots in this_map.layers[0][0]:
    string_unrotated += str(is_tile_rotated(this_map.tile_set, rots)) + " / "
print(string_unrotated)

tile_map = Sprite.SpriteSheet(this_map.tile_set)

# UPDATE
done = False
while not done:
    delta_time = clock.tick() / 1000

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
    win.blit(first_sprite, (0, 0))

    # TEXT
    white = (255, 255, 255)
    fps_text = "FPS: " + str(round(clock.get_fps()))
    fps_text_render = font.render(fps_text, True, white)
    win.blit(fps_text_render, (680, 10))

    pygame.display.flip()

pygame.quit()
