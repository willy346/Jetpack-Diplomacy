import pygame.key
from player import Player
from config import *
from pygame import mixer


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.select_char = True
        self.scenario = scenario1
        self.menu_looping = menu_looping
        self.char_looping_1 = char_looping_1
        self.char_looping_2 = char_looping_2
        self.gameplay_loop = gameplay_loop
        self.background = start_img_menu
        self.players_sprites = pygame.sprite.Group()
        self.players = []

    def get_screen(self):
        self.background = start_img_menu

    def game_loop(self):
        self.get_screen()
        while looping:
            self.get_menu()
            self.draw_sprites()
            pygame.display.update()
            clk.tick(fps)

    def get_menu(self):
        clk.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3 and self.menu_looping:
                    self.menu_looping = False
                    self.char_looping_1 = True

                if self.char_looping_1:
                    self.background = char_left_img_menu
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.select_char = not self.select_char
                    if event.key == pygame.K_SPACE:
                        self.char_looping_1 = False
                        self.char_looping_2 = True

                if self.char_looping_2:
                    self.background = char_right_img_menu
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.select_char = not self.select_char
                    if event.key == pygame.K_0:
                        self.gameplay_loop = True
                        self.char_looping_2 = False

                if self.gameplay_loop:
                    mixer.music.pause()
                    mixer.init()
                    mixer.music.load('song_game.mp3')
                    mixer.music.set_volume(0.4)
                    mixer.music.play()
                    self.background = scenario1

    def draw_sprites(self):
        screen.blit(self.background, (0, 0))

        # draw char picker 1
        if self.char_looping_1:
            if self.select_char:
                pygame.draw.circle(self.screen, WHITE, (255, 190), 20)
            else:
                pygame.draw.circle(self.screen, WHITE, (1035, 190), 20)
        # draw char picker 2
        elif self.char_looping_2:
            if self.select_char:
                pygame.draw.circle(self.screen, WHITE, (170, 190), 20)
            else:
                pygame.draw.circle(self.screen, WHITE, (1080, 180), 20)

