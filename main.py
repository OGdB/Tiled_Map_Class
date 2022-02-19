import Map
import pygame

pygame.init()

win_w = 300
win_h = 300
win = pygame.display.set_mode((win_w, win_h))

this_map = Map.Map("map.json")

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

    this_map.draw_map(win)

    pygame.display.flip()

pygame.quit()
