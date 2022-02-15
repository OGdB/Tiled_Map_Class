import pygame

class SpriteSheet:
    """Deals with getting portions of spritesheets"""
    def __init__(self, image):
        self.sheet = image

    def get_sprite(self, frame, width, height, color):
        """return a specific sprite from sprite sheet"""
        sprite = pygame.Surface((width, height)).convert_alpha()
        sprite.set_colorkey(color)
        sprite.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        return sprite

    def load_animation(self, start_frame, amount_of_frames):
        """return an animation from a sprite sheet starting at start_frame for specified amount of frames"""
        animation = []
        current_frame = start_frame

        for x in range(amount_of_frames):
            animation.append(self.get_sprite(current_frame, 64, 64, (0, 0, 0)))
            current_frame += 1
        return animation
