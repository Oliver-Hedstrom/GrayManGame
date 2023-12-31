# src/animation.py
import pygame
from audio import play_electrocuted_sound
from colors import COLORS

# Constants for the figures
STICK_FIGURE = [" O ", "-|-", "/ \\"]
STICK_FIGURE_SIZE = STICK_FIGURE[0].count(" ")

ELECTRIC_IMPACT_FIGURE = [" \\O/ ", " -|- ", " / \\ "]


def check_collision(attacker_pos, fence_x_position, fence_width):
    return attacker_pos >= fence_x_position and attacker_pos < (
        fence_x_position + fence_width
    )


def get_figure(electricity_activity):
    return ELECTRIC_IMPACT_FIGURE if electricity_activity else STICK_FIGURE


def get_color(game_state, collision, electricity_activity):
    if collision and (electricity_activity or game_state.get("zapped")):
        return (
            COLORS["RED"] if (pygame.time.get_ticks() // 250) % 2 else COLORS["WHITE"]
        )
    if collision:
        return COLORS["GREEN"]
    return COLORS["WHITE"]


def update_zapped_state(game_state, current_figure):
    if not game_state.get("zapped"):
        return current_figure, False

    print("zapped progress:", game_state["zapped_progress"])
    zapped_progress = game_state["zapped_progress"]
    zapped_figure = [
        line[: max(0, len(line) - zapped_progress)] for line in current_figure
    ]
    game_state["zapped_progress"] += 1

    if zapped_progress > STICK_FIGURE_SIZE:
        game_state["zapped_progress"] = 0
        game_state["zapped"] = False

    return zapped_figure


def animate_attacker(
    screen, font, attacker_pos, fence_x_position, fence_width, distance, game_state
):
    collision = check_collision(attacker_pos, fence_x_position, fence_width)
    electricity_activity = game_state["fence_electrified"] and collision
    current_figure = get_figure(electricity_activity)
    color = get_color(game_state, collision, electricity_activity)

    if electricity_activity:
        play_electrocuted_sound()
        game_state["zapped"] = True

    # Change color to black after passing the fence if zapped
    if game_state.get("zapped") and attacker_pos > fence_x_position + fence_width:
        current_figure = update_zapped_state(game_state, current_figure)
        color = COLORS["BLACK"]
        print("zapped")

    move_attacker(screen, font, distance, current_figure, color)


def move_attacker(screen, font, distance, current_figure, color):
    for i, line in enumerate(current_figure):
        text_surface = font.render(line, True, color)
        position = (distance, i * 50)
        screen.blit(text_surface, position)
