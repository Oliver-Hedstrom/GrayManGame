import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This is our stick figure - split into lines
stick_figure = [
    " O ",
    "-|-",
    "/ \\",
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)  # You can choose your own font and size

running = True
distance = 0  # Distance from left screen edge

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black
    screen.fill(BLACK)
    
    # Blit each line of ASCII art as a separate text Surface
    for i, line in enumerate(stick_figure):
        s = font.render(line, True, WHITE)
        pos = (distance, i * 50)  # 50 is roughly the height of each line
        screen.blit(s, pos)
    
    distance += 1  # Move 1px/frame to the right

    # If figure moved off screen, reset back to left edge
    if distance > WIDTH:
        distance = 0
    
    # Flip the display
    pygame.display.flip()

pygame.quit()
sys.exit()
