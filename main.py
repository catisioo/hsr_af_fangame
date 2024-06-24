import pygame
import pygame_menu
from pygame_menu import Theme

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1200, 600))

# Create a custom theme
mytheme = Theme(
    background_color=(0, 0, 0, 0),  # transparent background
    title_background_color=(4, 47, 126),
    title_font_shadow=True,
    widget_padding=25,
)

# Create a menu with the custom theme
menu = pygame_menu.Menu(
    title='My Menu',
    width=1200,
    height=600,
    theme=mytheme
)

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    
    menu.update(events)
    menu.draw(screen)
    pygame.display.flip()

pygame.quit()
