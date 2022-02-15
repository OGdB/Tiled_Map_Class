import Map
import pygame

pygame.init()

win_w = 800
win_h = 600
win = pygame.display.set_mode((win_w, win_h))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier New", 20, True)

# Tile stuff
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

    white = (255, 255, 255)
    fps_text = "FPS: " + str(round(clock.get_fps()))
    fps_text_render = font.render(fps_text, True, white)
    win.blit(fps_text_render, (680, 10))

    pygame.display.flip()

pygame.quit()
