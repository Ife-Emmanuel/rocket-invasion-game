import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    def __init__(self, a1_settings, screen, rocket ):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__() #python 2.7 version of super().__init__()
        self.screen = screen

        #Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, a1_settings.bullet_width, a1_settings.bullet_height)
        self.rect.centerx = rocket.rect.centerx
        self.rect.top = rocket.rect.top

        #Store the bullet's postion as a decimal value.
        self.y = float(self.rect.top)

        self.colour = a1_settings.bullet_colour
        self.speed_factor = a1_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        #Update the decimal position of the bullet.
        self.y -= self.speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)