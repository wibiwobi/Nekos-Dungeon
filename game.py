import pygame
from states.main_menu import MainMenu
from states.level_menu import LevelMenu

pygame.init()

class Game:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 1300, 650
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Neko's Dungeon")
        self.clock = pygame.time.Clock()

        self.main_menu = MainMenu(self.screen, self.WIDTH, self.HEIGHT)
        self.level_menu = LevelMenu(self.screen, self.WIDTH, self.HEIGHT)

        self.initial_state = self.main_menu

    def run(self):
        
        running = True
        current_state = self.initial_state
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("executed")
                    
                    if event.button == 1 and self.main_menu.start_btn.hover_btn(): 
                        current_state = self.level_menu  
                    


                    elif event.button == 1 and current_state == self.level_menu:
                        if self.level_menu.prev_arrow.arrow_hovered() == True: 
                            self.level_menu.banner_state_manager.change_banner("PREV")
                        if self.level_menu.next_arrow.arrow_hovered() == True: 
                            self.level_menu.banner_state_manager.change_banner("NEXT")

            
            current_state.run()                  

            pygame.display.flip()
            self.clock.tick(30)



            # 16:08: https://www.youtube.com/watch?v=N6xqCwblyiw







