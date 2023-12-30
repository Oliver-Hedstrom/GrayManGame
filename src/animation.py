# Deals with the different animations - electrifying fence, electrocuting attacker, loss animation.
# src/animation.py
# src/animation.py
import pygame
from colors import COLORS

# This is our stick figure - split into lines
stick_figure = [
    " O ",
    "-|-",
    "/ \\",
]

# Alternative stick figure for electric impact
electric_impact_figure = [
    " \\O/ ",
    " -|- ",
    " / \\ ",
]


def check_collision(attacker_pos, fence_x_position, fence_width):
    # Returns True if the attacker has collided with the fence
    return attacker_pos >= fence_x_position and attacker_pos < (
        fence_x_position + fence_width
    )


def animate_attacker(
    screen, font, attacker_pos, fence_x_position, fence_width, distance, game_state
):
    # Check for collision
    collision = check_collision(attacker_pos, fence_x_position, fence_width)
    electricity_activity = game_state["fence_electrified"] and collision
    current_figure = electric_impact_figure if electricity_activity else stick_figure

    # Determine the color based on collision
    color = set_color(collision, electricity_activity)

    # Optionally update ASCII art for electric impact
    if collision:
        # stick_figure = updated ASCII art for electric impact
        pass

    # Blit each line of ASCII art as a separate text Surface
    for i, line in enumerate(current_figure):
        s = font.render(line, True, color)
        pos = (distance, i * 50)  # 50 is roughly the height of each line
        screen.blit(s, pos)


def set_color(collision, electricity_activity):
    if electricity_activity and (pygame.time.get_ticks() // 250) % 2:
        color = COLORS["RED"]
    elif collision and not electricity_activity:
        color = COLORS["GREEN"]
    else:
        color = COLORS["WHITE"]
    return color
