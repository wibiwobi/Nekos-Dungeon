import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 1. Camera Positions
camera_x = 0
camera_y = 0

# 2. Hardcoded object coordinates in the in-game "World"
world_objects = [(100, 100), (400, 300), (700, 500)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Read input to move camera positions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:  camera_x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: camera_x += 5
    if keys[pygame.K_UP] or keys[pygame.K_w]:    camera_y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:  camera_y += 5

    screen.fill((30, 30, 30))

    # 4. Render by transforming World Coordinates to Screen Coordinates
    for obj_x, obj_y in world_objects:
        screen_x = obj_x - camera_x
        screen_y = obj_y - camera_y
        
        # Only draw if the calculated point is inside the screen boundaries
        pygame.draw.circle(screen, (255, 0, 0), (screen_x, screen_y), 20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()