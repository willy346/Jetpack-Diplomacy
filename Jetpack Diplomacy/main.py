from config import *
from game import Game
from pygame import mixer
mixer.init()
mixer.music.load('ussr_anthem.mp3')
mixer.music.set_volume(0.3)
pygame.init()
mixer.music.play()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jetpack-Diplomacy")
play = Game(screen)
play.game_loop()
