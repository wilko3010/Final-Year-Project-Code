import pygame

pygame.mixer.init()
pygame.mixer.music.load("doorbell.wav")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
