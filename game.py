import pygame
from states.main_menu import MainMenu

from states.level_menu import LevelMenu
from states.forest_level import ForestLevel

pygame.init()

class Game:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 1300, 650
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        pygame.display.set_caption("Neko's Dungeon")
        self.clock = pygame.time.Clock()
     
        

        self.main_menu = MainMenu(self.screen, self.WIDTH, self.HEIGHT)
        self.level_menu = LevelMenu(self.screen, self.WIDTH, self.HEIGHT)

        self.forest_level = ForestLevel(self.screen)

        self.banner_state_manager = self.level_menu.banner_state_manager

        self.initial_state = self.main_menu

    def run(self):
        
        running = True
        current_state = self.initial_state
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        
                    if self.main_menu.start_btn.hover_btn(): 
                        current_state = self.level_menu  

                    elif current_state == self.level_menu: 
                        # ! User can see all the different levels
                        if self.level_menu.prev_arrow.arrow_hovered() == True: 
                            self.level_menu.banner_state_manager.change_banner("PREV")
                        if self.level_menu.next_arrow.arrow_hovered() == True: 
                            self.level_menu.banner_state_manager.change_banner("NEXT")

                        # ! Change level state menu to a specific level
                        if self.banner_state_manager.banner_hovered() == "Forest Banner":
                            current_state = self.forest_level
                            self.screen.fill((255, 255, 255))
                            self.forest_level.add_tiles_to_sprite_group()
                            self.forest_level.draw_map()


            current_state.run()                  

            pygame.display.flip()
            self.clock.tick(30)



            # 16:08: https://www.youtube.com/watch?v=N6xqCwblyiw







