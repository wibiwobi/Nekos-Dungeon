
from pytmx.util_pygame import load_pygame
import pygame
from entities.main_character import MainCharacter

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)


class ForestLevel:
    def __init__(self, screen):
        self.screen = screen
        self.tmx_forest_data = load_pygame("./assets/tiled/tile_maps/forest_map.tmx", pixelalpha=True)
        self.tile_width = self.tmx_forest_data.tilewidth
        self.tile_height = self.tmx_forest_data.tileheight
        
        self.layer_1 = self.tmx_forest_data.get_layer_by_name("Tile Layer 1")
        self.layer_2 = self.tmx_forest_data.get_layer_by_name("Tile Layer 2")
        self.obj_1 = self.tmx_forest_data.get_layer_by_name("Object Layer 1")

        self.sprite_group = pygame.sprite.Group()
        self.initial_screen_x = 150
        self.initial_screen_y = 780
        self.scale_intensity = 2.5


        self.main_character = MainCharacter(self.screen, self.get_main_character_spawn_point())

        

        # all visible objects here

    def add_tiles_to_sprite_group(self):
        for layer in self.tmx_forest_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    surf = pygame.transform.scale(surf, (surf.get_width() * self.scale_intensity, surf.get_height() * self.scale_intensity)).convert_alpha()
                    pos = ((x * self.tile_width - self.initial_screen_x) * self.scale_intensity, (y * self.tile_height - self.initial_screen_y) * self.scale_intensity)
                    
                    surf.set_colorkey((0, 0, 0))
                    Tile(pos = pos, surf = surf, groups = self.sprite_group)


        all_objects = []
        for obj in self.obj_1:
            if obj.image:
                surf = pygame.transform.scale(obj.image, (obj.image.get_width() * self.scale_intensity, obj.image.get_height() * self.scale_intensity)).convert_alpha()
                surf.set_colorkey((0, 0, 0))
                all_objects.append(((obj.y - self.initial_screen_y) * self.scale_intensity, (obj.x - self.initial_screen_x) * self.scale_intensity, surf))
            
            if obj.name == "Initial Spawn Point":
               self.spawn_point_pos = ((obj.x - self.initial_screen_x) * self.scale_intensity, (obj.y - self.initial_screen_y) * self.scale_intensity)

        all_objects.sort(key=lambda tuple:tuple[0])
        for y, x, surf in all_objects:
            Tile(pos = (x, y), surf = surf , groups=self.sprite_group)

    def get_main_character_spawn_point(self):
        for obj in self.obj_1:
            if obj.name == "Initial Spawn Point":
               return ((obj.x - self.initial_screen_x) * self.scale_intensity, (obj.y - self.initial_screen_y) * self.scale_intensity)
    
    
    def draw_map(self):
        self.sprite_group.draw(self.screen) 

    def run(self):
        self.main_character.draw_frames()
