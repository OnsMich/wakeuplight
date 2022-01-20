import settings
import pygame


class AudioPlayer:
    def __init__(self, audio_file=settings.AUDIO_FILE):
        self.audio_file = f'../{audio_file}'
        pygame.mixer.init()

    def play_file(self):
        pygame.mixer.music.load(self.audio_file)
        pygame.mixer.music.play()
        print('audio')
        while pygame.mixer.music.get_busy():
            continue
