# Manages the sound effects.
import pygame

electrocuted_sound = None


def load_sounds():
    global electrocuted_sound
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    if electrocuted_sound is None:
        electrocuted_sound = pygame.mixer.Sound("resources/sounds/electricity.wav")


def play_electrocuted_sound():
    if electrocuted_sound is None:
        load_sounds()
    electrocuted_sound.play()
