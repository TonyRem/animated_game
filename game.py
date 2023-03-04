import pygame
from sys import exit


pygame.init()

# Define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TonyRem RPG-game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

pygame.mixer.music.load('graphic_arts/discovery.mp3')


bulk_surface = pygame.image.load('graphic_arts/swamp.png').convert()
# text_surface = test_font.render('My game', False, 'Blue').convert()
hero_surface = pygame.image.load(
    'graphic_arts/run/running_016.png').convert_alpha()
hero_jump_surface = pygame.image.load(
    'graphic_arts/jump/jump_000.png').convert_alpha()
hero_frames = [pygame.image.load(
    f'graphic_arts/run/running_{i:03d}.png'
).convert_alpha() for i in range(16, 65)]

current_frame = 0
a = 0
b = SCREEN_WIDTH

player_moved = False
animation_time = 30  # Time in milliseconds between animation frames
last_frame_time = pygame.time.get_ticks()
pygame.mixer.music.play(-1)  # -1 means play indefinitely

# Player's attributes
player_x = 10
player_y = 200
player_vel_y = 0
hero_rect = hero_frames[current_frame].get_rect(topleft=(player_x, player_y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    current_time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if player_y == 200:  # Only jump if player is on the ground
            player_vel_y = -10  # Set the hight of the jump

    # Apply gravity to the player's jump
    player_vel_y += 0.5

    # Update the player's position
    player_y += player_vel_y

    if player_y > 200:
        player_y = 200
        player_vel_y = 0

    if keys[pygame.K_d]:
        if current_time - last_frame_time >= animation_time:
            current_frame = (current_frame + 1) % len(hero_frames)
            last_frame_time = current_time
            a -= 10
            b -= 10

    else:
        if current_time - last_frame_time >= animation_time:
            current_frame = 0
            last_frame_time = current_time

    if a < -SCREEN_WIDTH:
        a = b + SCREEN_WIDTH
    if b < -SCREEN_WIDTH:
        b = a + SCREEN_WIDTH

    screen.blit(bulk_surface, (a, 0))
    screen.blit(bulk_surface, (b, 0))
    if player_y < 200:
        screen.blit(hero_jump_surface, (hero_rect))
    else:
        screen.blit(hero_frames[current_frame], (hero_rect))
    hero_rect.topleft = (player_x, player_y)

    pygame.display.update()
    clock.tick(60)
