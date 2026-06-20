import pygame

class BannerStateManager:
    def __init__(self, screen, banners):
        self.banners = banners 
        self.screen = screen
        self.current_banner_index = 0

        self.inital_banner = self.banners[self.current_banner_index]
        self.banner_queue = banners

    def change_banner(self, pressed_button):
        if pressed_button == "PREV":
            if self.current_banner_index -1 == -1:
                self.current_banner_index = 2
            else: 
                self.current_banner_index -= 1    
        if pressed_button == "NEXT":
            if self.current_banner_index + 1 == 3:
                self.current_banner_index = 0
            else: 
                self.current_banner_index += 1   

        self.inital_banner = self.banners[self.current_banner_index]        

        
    def draw_banner(self):
        self.screen.blit(self.inital_banner.banner_img, self.inital_banner.banner_cords)

    # func that checks for banner hovers
    def banner_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        banner_rect = self.inital_banner.banner_img.get_rect(topleft=(self.inital_banner.banner_cords))

        if banner_rect.collidepoint(mouse_pos):
            return self.inital_banner.banner_name
        return




class LevelImageBanners:
    def __init__(self, screen, banner_img, SCREEN_WIDTH, SCREEN_HEIGHT, banner_name):
        self.screen = screen
        self.banner_img = pygame.transform.scale(banner_img, (541, 612))
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.banner_name = banner_name

        self.banner_cords = (self.SCREEN_WIDTH // 2 - (self.banner_img.get_width() // 2), self.SCREEN_HEIGHT // 2 - (self.banner_img.get_height() // 2))
        print(self.banner_cords)


# class for arrows
class Arrow:
    def __init__(self, img, screen, SCREEN_WIDTH, SCREEN_HEIGHT, arrow_type):
        self.img = img
        self.scaled_arrow_img = pygame.transform.scale(img, (50, 50)) 
        self.arrow_type = arrow_type

        self.screen = screen 
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.arrow_cords = ()
        if self.arrow_type == "PREV":
            self.arrow_cords = (100, self.SCREEN_HEIGHT // 2 - (self.scaled_arrow_img.get_height()))
        if self.arrow_type == "NEXT":
            self.arrow_cords = (self.SCREEN_WIDTH - (self.scaled_arrow_img.get_width()) - 100, self.SCREEN_HEIGHT // 2 - (self.scaled_arrow_img.get_height())) 


        

    def draw_arrow(self):
        self.screen.blit(self.scaled_arrow_img, self.arrow_cords)


    def arrow_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        arrow_rect = self.scaled_arrow_img.get_rect(topleft=(self.arrow_cords))

        if arrow_rect.collidepoint(mouse_pos):
            self.scaled_arrow_img = pygame.transform.scale(self.img, (55, 55))
            return True
        else: # reset
            self.scaled_arrow_img = pygame.transform.scale(self.img, (50, 50)) 
        return
        
    




        

class LevelMenu:
    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.screen = screen 

        prev_img = pygame.image.load("./assets/images/buttons/levels_menu/previous_arrow.png").convert_alpha()
        next_img = pygame.image.load("./assets/images/buttons/levels_menu/next_arrow.png").convert_alpha()
        self.prev_arrow = Arrow(prev_img, screen, SCREEN_WIDTH, SCREEN_HEIGHT, "PREV") 
        self.next_arrow = Arrow(next_img, screen, SCREEN_WIDTH, SCREEN_HEIGHT, "NEXT")


        forest_banner_img = pygame.image.load("./assets/images/buttons/levels_menu/forest_banner.png")
        dungeon_banner_img = pygame.image.load("./assets/images/buttons/levels_menu/dungeon_banner.png")
        city_banner_img = pygame.image.load("./assets/images/buttons/levels_menu/city_banner.png")
        self.forest_banner = LevelImageBanners(screen, forest_banner_img, SCREEN_WIDTH, SCREEN_HEIGHT, "Forest Banner")
        self.dungeon_banner = LevelImageBanners(screen, dungeon_banner_img, SCREEN_WIDTH, SCREEN_HEIGHT, "Dungeon Banner")
        self.city_banner = LevelImageBanners(screen, city_banner_img, SCREEN_WIDTH, SCREEN_HEIGHT, "City Banner")

        self.banner_state_manager = BannerStateManager(screen, [self.forest_banner, self.dungeon_banner, self.city_banner])


    def run(self):
        self.screen.fill((255, 255, 255))
        self.prev_arrow.draw_arrow()
        self.next_arrow.draw_arrow()

        self.prev_arrow.arrow_hovered()
        self.next_arrow.arrow_hovered()

        self.banner_state_manager.draw_banner()


        # func that checks for banner hovers






