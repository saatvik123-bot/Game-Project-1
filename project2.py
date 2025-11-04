import pygame                                                            

pygame.init()

# Corrected variable names
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Create display
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

# Load and scale background image
background_image = pygame.transform.scale(
    pygame.image.load('Codingal Cirtificate.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Load and scale penguin image
penguin_image = pygame.transform.scale(
    pygame.image.load('Codingal Cirtificate.png').convert_alpha(),
    (200, 200)
)
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))   

# Create text
font = pygame.font.Font(None, 36)
text = font.render('Hello World', True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw background, image, and text
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Run the game
if __name__ == '__main__':
    game_loop()
