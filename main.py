import pygame
import Map

pygame.init()

clock = pygame.time.Clock()

win_w = 300
win_h = 300
win = pygame.display.set_mode((win_w, win_h))
x = 0
y = 0
this_map = Map.Map("map.json")

move_speed = 150

done = False
while not done:
    delta_time = clock.tick() / 1000

    # INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y += move_speed * delta_time
    if keys[pygame.K_s]:
        y -= move_speed * delta_time
    if keys[pygame.K_d]:
        x -= move_speed * delta_time
    if keys[pygame.K_a]:
        x += move_speed * delta_time

    # DRAWING
    win.fill((0, 0, 0))

    this_map.render_map(win, x, y)

    pygame.display.flip()

pygame.quit()
