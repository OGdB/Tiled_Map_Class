import Map
import pygame
import SpriteSheet as Sprite

pygame.init()
this_map = Map.Map("map.json")

win_w = this_map.map_width * this_map.tile_width
win_h = this_map.map_height * this_map.tile_height
win = pygame.display.set_mode((win_w, win_h))

tiles = this_map.load_used_tiles()

done = False
while not done:
    # INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if event.key == pygame.K_ESCAPE:
                done = True

    # DRAWING
    win.fill((0, 0, 0))

    this_map.draw_map(win, tiles)

    pygame.display.flip()

pygame.quit()
