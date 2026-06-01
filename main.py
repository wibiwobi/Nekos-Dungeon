class MainMenuButton:
    def __init__(self, image, scale_width, scale_height, SCREEN_WIDTH, SCREEN_HEIGHT, space=0):
        self.image = image 
        self.scaled_width = scale_width
        self.scaled_height = scale_height
        self.scaled_button = pygame.transform.scale(self.image, (self.scaled_width, self.scaled_height)) 
        
        self.SCREEN_WIDTH = WIDTH 
        self.SCREEN_HEIGHT = HEIGHT
        self.space = space

        self.center_x = (SCREEN_WIDTH // 2) - (self.scaled_button.get_width() // 2)
        self.center_y = ((SCREEN_HEIGHT // 2) - (self.scaled_button.get_height() // 2)) + space
        self.center_cords = (self.center_x, self.center_y)

    def draw_btn(self):
        screen.blit(self.scaled_button, self.center_cords)    
    
    def hover_btn(self):
        mouse_pos = pygame.mouse.get_pos()
        btn_rect = self.scaled_button.get_rect(topleft=(self.center_cords))

        # if the mouse is not over the btn, unscale it
        if btn_rect.collidepoint(mouse_pos):
            self.scaled_button = pygame.transform.scale(self.image, (self.scaled_width + 5, self.scaled_height + 4)) 

            self.center_x = (self.SCREEN_WIDTH // 2) - (self.scaled_button.get_width() // 2)
            self.center_y = ((self.SCREEN_HEIGHT // 2) - (self.scaled_button.get_height() // 2)) + self.space
            self.center_cords = (self.center_x, self.center_y)
        else: # reset
            self.scaled_button = pygame.transform.scale(self.image, (self.scaled_width, self.scaled_height)) 



import pygame
import cv2

pygame.init()

WIDTH, HEIGHT = 1300, 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neko's Dungeon")

main_menu_video_path = "./assets/videos/main_menu_background.mp4"
cap = cv2.VideoCapture(main_menu_video_path)


clock = pygame.time.Clock()

logo_img = pygame.image.load("./assets/images/nekos_dungeon_logo.png").convert_alpha()
scaled_logo = pygame.transform.scale(logo_img, (440, 230)) 

start_img = pygame.image.load("./assets/images/buttons/start_button.png").convert_alpha()
continue_img = pygame.image.load("./assets/images/buttons/continue_button.png").convert_alpha()
settings_img = pygame.image.load("./assets/images/buttons/settings_button.png").convert_alpha()

start_btn = MainMenuButton(start_img, 230, 65, WIDTH, HEIGHT, -65)
continue_btn = MainMenuButton(continue_img, 210, 65, WIDTH, HEIGHT)
settings_btn = MainMenuButton(settings_img, 190, 65, WIDTH, HEIGHT, 60)

start_btn.center = (2, 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    success, frame = cap.read()
    

    # loops the video back
    if not success:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    if success:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.transpose(frame)

        bg_surface = pygame.surfarray.make_surface(frame)
        bg_surface = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT))

        screen.blit(bg_surface, (0, 0))
    
    start_btn.draw_btn()
    continue_btn.draw_btn()
    settings_btn.draw_btn()

    screen.blit(scaled_logo, ((WIDTH // 2) - scaled_logo.get_width() // 2, 0))
    start_btn.hover_btn()
    continue_btn.hover_btn()
    settings_btn.hover_btn()

    pygame.display.flip()
    clock.tick(30)

# 5. Clean Up
pygame.quit()




