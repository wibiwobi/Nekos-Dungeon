
import pygame
import cv2

class MainMenuButton:
    def __init__(self, button, screen, image, scale_width, scale_height, SCREEN_WIDTH, SCREEN_HEIGHT, space=0):
        self.screen = screen
        self.button = button

        self.SCREEN_WIDTH = SCREEN_WIDTH 
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.image = image 
        self.scaled_width = scale_width
        self.scaled_height = scale_height
        self.scaled_button = pygame.transform.scale(self.image, (self.scaled_width, self.scaled_height)) 
        
        self.space = space

        self.center_x = (SCREEN_WIDTH // 2) - (self.scaled_button.get_width() // 2)
        self.center_y = ((SCREEN_HEIGHT // 2) - (self.scaled_button.get_height() // 2)) + space
        self.center_cords = (self.center_x, self.center_y)

    def draw_btn(self):
        self.screen.blit(self.scaled_button, self.center_cords)    
    
    def hover_btn(self):
        mouse_pos = pygame.mouse.get_pos()
        btn_rect = self.scaled_button.get_rect(topleft=(self.center_cords))

        # if the mouse is not over the btn, unscale it
        if btn_rect.collidepoint(mouse_pos):
            self.scaled_button = pygame.transform.scale(self.image, (self.scaled_width + 5, self.scaled_height + 4)) 

            self.center_x = (self.SCREEN_WIDTH // 2) - (self.scaled_button.get_width() // 2)
            self.center_y = ((self.SCREEN_HEIGHT // 2) - (self.scaled_button.get_height() // 2)) + self.space
            self.center_cords = (self.center_x, self.center_y)
            return True
        else: # reset
            self.scaled_button = pygame.transform.scale(self.image, (self.scaled_width, self.scaled_height)) 



class MainMenu(MainMenuButton):
    def __init__(self, screen, WIDTH, HEIGHT):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.main_menu_video_path = "./assets/videos/main_menu_background.mp4"
        self.cap = cv2.VideoCapture(self.main_menu_video_path)

        self.logo_img = pygame.image.load("./assets/images/nekos_dungeon_logo.png").convert_alpha()
        self.scaled_logo = pygame.transform.scale(self.logo_img, (440, 230)) 

        self.start_img = pygame.image.load("./assets/images/buttons/start_button.png").convert_alpha()
        self.continue_img = pygame.image.load("./assets/images/buttons/continue_button.png").convert_alpha()
        self.settings_img = pygame.image.load("./assets/images/buttons/settings_button.png").convert_alpha()

        self.start_btn = MainMenuButton("START" ,screen, self.start_img, 230, 65, WIDTH, HEIGHT, -65)
        self.continue_btn = MainMenuButton("CONTINUE", screen, self.continue_img, 210, 65, WIDTH, HEIGHT)
        self.settings_btn = MainMenuButton("SETTINGS", screen, self.settings_img, 190, 65, WIDTH, HEIGHT, 60)

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        success, frame = self.cap.read()
        

        # loops the video back
        if not success:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        if success:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.transpose(frame)

            bg_surface = pygame.surfarray.make_surface(frame)
            bg_surface = pygame.transform.scale(bg_surface, (self.WIDTH, self.HEIGHT))

            self.screen.blit(bg_surface, (0, 0))
        
        self.start_btn.draw_btn()
        self.continue_btn.draw_btn()
        self.settings_btn.draw_btn()

        self.screen.blit(self.scaled_logo, ((self.WIDTH // 2) - self.scaled_logo.get_width() // 2, 0))
        self.start_btn.hover_btn()
        self.continue_btn.hover_btn()
        self.settings_btn.hover_btn()







