import os

import pygame

def play_file(file_name: str):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    # pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    print('should be playing now')
    while pygame.mixer.music.get_busy():
        continue

if __name__ == '__main__':
    if os.path.exists("../birds.wav"):
        print('file bestaat')
    play_file("../birds.wav")
