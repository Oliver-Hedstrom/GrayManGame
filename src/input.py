# src/input.py
import pygame

def handle_input(events, game_state):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state['fence_electrified'] = True
            elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                game_state['running'] = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                game_state['fence_electrified'] = False