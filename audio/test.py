import pygame

def play_file(file_name: str):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

if __name__ == '__main__':
    play_file("../birds.wav")
