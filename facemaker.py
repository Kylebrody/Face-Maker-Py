import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT

pygame.init()

# Window and clock setup
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Sprites
nose_image_paths = ["images/n1.png", "images/n2.png", "images/n3.png", "images/n4.png"]
eye_image_paths = ["images/e1.png", "images/e2.png", "images/e3.png", "images/e4.png"]
image_path_index = 0
current_sprite = pygame.image.load(nose_image_paths[image_path_index])
sprite_positions = []  

# Button setup
undo_button_color = (255, 0, 0)  
undo_button_rect = pygame.Rect(50, 50, 100, 50)

eye_button_color = (0, 255, 0)
eye_button_rect = pygame.Rect(50, 100, 100, 50)

nose_button_color = (0, 0, 255)
nose_button_rect = pygame.Rect(50, 150, 100, 50)

font = pygame.font.Font(None, 36)
undo_button_text = font.render("Undo", True, (255, 255, 255))  
eye_button_text = font.render("Eyes", True, (255, 255, 255))
nose_button_text = font.render("Nose", True, (255, 255, 255))

sprite_type = 0  # 0 for nose, 1 for eyes

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                # Check for Undo button click
                if undo_button_rect.collidepoint(event.pos):
                    if sprite_positions:  # Remove the last sprite
                        sprite_positions.pop()
                
                # Check for Eye button click
                elif eye_button_rect.collidepoint(event.pos):
                    sprite_type = 1
                    image_path_index = 0  # Reset index when switching
                    current_sprite = pygame.image.load(eye_image_paths[image_path_index])
                
                # Check for Nose button click
                elif nose_button_rect.collidepoint(event.pos):
                    sprite_type = 0
                    image_path_index = 0  # Reset index when switching
                    current_sprite = pygame.image.load(nose_image_paths[image_path_index])
                
                # Otherwise, place a sprite at the mouse position
                else:
                    sprite_positions.append((current_sprite, event.pos))
            
            elif event.button == 3:  # Right click
                # Change sprite based on sprite_type
                if sprite_type == 0:  # Nose sprite
                    image_path_index = (image_path_index + 1) % len(nose_image_paths)
                    current_sprite = pygame.image.load(nose_image_paths[image_path_index])
                elif sprite_type == 1:  # Eye sprite
                    image_path_index = (image_path_index + 1) % len(eye_image_paths)
                    current_sprite = pygame.image.load(eye_image_paths[image_path_index])

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the Undo button
    pygame.draw.rect(screen, undo_button_color, undo_button_rect)
    screen.blit(undo_button_text, undo_button_rect.move(10, 10))

    # Draw the Eye button
    pygame.draw.rect(screen, eye_button_color, eye_button_rect)
    screen.blit(eye_button_text, eye_button_rect.move(10, 10))

    # Draw the Nose button
    pygame.draw.rect(screen, nose_button_color, nose_button_rect)
    screen.blit(nose_button_text, nose_button_rect.move(10, 10))

    # Draw all sprites
    for sprite, pos in sprite_positions:
        rect = sprite.get_rect(center=pos)
        screen.blit(sprite, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
