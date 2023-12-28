import pygame
from pygame.locals import *
import sys
from animation import animate_attacker 

pygame.init()

# Constants
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)



screen_info = pygame.display.Info()
# Calculate 90% of the screen width
screen_width = int(screen_info.current_w/2)
screen_height = int(screen_info.current_h/4)

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)  # You can choose your own font and size

running = True
distance = 0  # Distance from left screen edge

# Load the fence image
fence_image = pygame.image.load('resources/sprites/fence.png')
# Scale the image to be 5 times bigger
fence_image = pygame.transform.scale(fence_image, (fence_image.get_width() * 3, fence_image.get_height() * 3))
# Get the rectangle of the scaled image
fence_rect = fence_image.get_rect()
fence_x_position = int(screen_width * 0.75)
fence_width = fence_rect.width
# Calculate how many times the image should be repeated to fill the screen height
repeat_count = screen_height // fence_rect.height + 1


while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black
    screen.fill(GREY)

    # Blit the scaled fence image repeatedly to create a contiguous line
    for i in range(repeat_count):
        screen.blit(fence_image, (fence_x_position, i * fence_rect.height))

# ... rest of your game loop code ...

    
    # Blit each line of ASCII art as a separate text Surface
    # for i, line in enumerate(stick_figure):
    #     s = font.render(line, True, WHITE)
    #     pos = (distance, i * 50)  # 50 is roughly the height of each line
    #     screen.blit(s, pos)
    animate_attacker(screen, font, distance, fence_x_position, fence_width, distance)
    
    distance += 1  # Move 1px/frame to the right

    # If figure moved off screen, reset back to left edge
    if distance > screen_width:
        distance = 0
    
    # Flip the display
    pygame.display.flip()

pygame.quit()
sys.exit()
