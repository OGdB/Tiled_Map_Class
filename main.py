import Map
import pygame
import SpriteSheet as Sprite

pygame.init()
this_map = Map.Map("map.json")

win_w = this_map.map_width * this_map.tile_width
win_h = this_map.map_height * this_map.tile_height
win = pygame.display.set_mode((win_w, win_h))

tiles = this_map.load_used_tiles()

# UPDATE
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

    for layer_index in range(len(this_map.layers)):  # for every layer in the layers
        this_layer = this_map.layers[layer_index]
        for row_index in range(len(this_layer)):
            this_row = this_layer[row_index]
            tile_y_pos = row_index * 16
            for tile_index in range(len(this_row)):
                this_tile = this_row[tile_index]
                if this_tile != 0:
                    tile_x_pos = tile_index * 16
                    win.blit(tiles[this_tile], (tile_x_pos, tile_y_pos))

    pygame.display.flip()

pygame.quit()
