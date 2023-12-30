# Deals with the different animations - electrifying fence, electrocuting attacker, loss animation.
# src/animation.py
# src/animation.py
import pygame
from audio import play_electrocuted_sound
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
    color = update_colors(
        game_state,
        current_figure,
        collision,
        electricity_activity,
        fence_x_position,
        fence_width,
        attacker_pos,
    )  # Determine the color based on collision

    if electricity_activity:
        play_electrocuted_sound()
        game_state["zapped"] = True

    # Blit each line of ASCII art as a separate text Surface
    for i, line in enumerate(current_figure):
        s = font.render(line, True, color)
        pos = (distance, i * 50)  # 50 is roughly the height of each line
        screen.blit(s, pos)

def handle_zapped_attacker(game_state, current_figure, color, attacker_pos, fence_x_position, fence_width):
    if game_state.get("zapped"):
        color = COLORS["BLACK"]
        zapped_figure = [
            line[: max(0, len(line) - game_state["zapped_progress"])]
            + " " * game_state["zapped_progress"]
            for line in current_figure  # Use current_figure instead of stick_figure
        ]
        current_figure = zapped_figure
        # Increment zapped progress
        game_state["zapped_progress"] += 1
        if game_state["zapped_progress"] >= len(current_figure[0]):
            game_state["zapped_progress"] = 0
            game_state["zapped"] = False
    else:
        # Reset zapped progress and color
        game_state["zapped_progress"] = 0
        color = COLORS["WHITE"]

    return current_figure, color  # Return both current_figure and color

def update_colors(game_state, current_figure, collision, electricity_activity, fence_x_position, fence_width, attacker_pos):
    color = COLORS["WHITE"]  # Initialize color before using it
    if game_state.get("zapped") and attacker_pos > fence_x_position + fence_width:
        current_figure, color = handle_zapped_attacker(
            game_state, current_figure, color, attacker_pos, fence_x_position, fence_width
        )
    else:
        game_state["zapped_progress"] = 0
        color = COLORS["WHITE"]
        current_figure = stick_figure if not electricity_activity else electric_impact_figure

    if electricity_activity and (pygame.time.get_ticks() // 250) % 2:
        color = COLORS["RED"]
    elif collision and not electricity_activity:
        color = COLORS["GREEN"]
    else:
        color = COLORS["WHITE"]

    return color