import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT

pygame.init()

# Window and clock setup
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Sprites
image_paths = ["images/n1.png", "images/n2.png", "images/n3.png", "images/n4.png"]
image_path_index = 0
current_sprite = pygame.image.load(image_paths[image_path_index])
sprite_positions = []  

# Button setup
undo_button_color = (255, 0, 0)  
undo_button_rect = pygame.Rect(50, 50, 100, 50)  
font = pygame.font.Font(None, 36)
undo_button_text = font.render("Undo", True, (255, 255, 255))  

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  
                if undo_button_rect.collidepoint(event.pos):
                    if sprite_positions:  
                        sprite_positions.pop()
                else:
                    sprite_positions.append((current_sprite, event.pos))
            elif event.button == 3:  
                image_path_index = (image_path_index + 1) % len(image_paths)
                current_sprite = pygame.image.load(image_paths[image_path_index])

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, undo_button_color, undo_button_rect)
    screen.blit(undo_button_text, undo_button_rect.move(10, 10))

    for sprite, pos in sprite_positions:
        rect = sprite.get_rect(center=pos)
        screen.blit(sprite, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()