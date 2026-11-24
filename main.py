# Dungeon Escape
import pygame
from enemys import basic_enemy, slow_enemy, movement_enemy, reset_enemys
from floors import create_floor
from movement import move_player
from health import check_damage, draw_hearts
from settings import WIDTH, HEIGHT, PLAYER_SIZE, PLAYER_START, PLAYER_SPEED, FPS, TOTAL_FLOORS
from settings import MAX_HEALTH, DAMAGE_COOLDOWN
from menu import main_menu

def main():
    #making the game window dimensions
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon Escape")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    big_font = pygame.font.Font(None, 64)

    # Show main menu
    menu_choice = main_menu(screen, clock)

    if menu_choice == "quit":
        pygame.quit()
        return

    #PLAYER VARIABLES
    player = pygame.Rect(PLAYER_START, (PLAYER_SIZE, PLAYER_SIZE))
    player_speed = PLAYER_SPEED
    current_floor = 1
    has_key = False
    health = MAX_HEALTH
    last_hit = -DAMAGE_COOLDOWN
    game_over = False
    escaped = False

    walls, key, door = create_floor(current_floor)
    reset_enemys(current_floor)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                #press r after dying or winning to start again
                if event.key == pygame.K_r and (game_over or escaped):
                    player.topleft = PLAYER_START
                    current_floor = 1
                    has_key = False
                    health = MAX_HEALTH
                    last_hit = -DAMAGE_COOLDOWN
                    game_over = False
                    escaped = False
                    walls, key, door = create_floor(current_floor)
                    reset_enemys(current_floor)

        if not running:
            break

        current_time = pygame.time.get_ticks()

        if not game_over and not escaped:
            #key inputs for player movement
            keys = pygame.key.get_pressed()
            dx = 0
            dy = 0
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                dx = -player_speed
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                dx = player_speed
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                dy = -player_speed
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                dy = player_speed

            move_player(player, walls, door, has_key, dx, dy)

            movement_enemy(player, walls + [door])

            #player enemy interaction
            health, last_hit = check_damage(
                player, basic_enemy, slow_enemy, health, last_hit, current_time
            )
            if health == 0:
                game_over = True

            if not game_over:
                if key is not None and player.colliderect(key):
                    has_key = True
                    key = None  #remove the key from the floor

                if has_key and player.colliderect(door):
                    if current_floor < TOTAL_FLOORS:
                        current_floor += 1
                        has_key = False
                        walls, key, door = create_floor(current_floor)
                        player.topleft = PLAYER_START
                        reset_enemys(current_floor)
                        #health carries over  new floor needs a new key
                    else:
                        escaped = True

        #draw background and walls
        screen.fill((30, 30, 30))
        for wall in walls:
            pygame.draw.rect(screen, (90, 90, 90), wall)

        if key is not None:
            pygame.draw.rect(screen, (255, 215, 0), key)

        # to change color door once you have key 
        door_color = (120, 70, 30)
        if has_key:
            door_color = (55, 150, 85)
        pygame.draw.rect(screen, door_color, door)

        #draw player, flash a little while the damage cooldown is on
        if current_time - last_hit >= DAMAGE_COOLDOWN or current_time // 100 % 2 == 0:
            pygame.draw.rect(screen, (50, 150, 255), player)

        # enemy damage values purple takes two heart and red takes one 
        pygame.draw.rect(screen, (200, 50, 50), basic_enemy)
        pygame.draw.rect(screen, (155, 75, 200), slow_enemy)

        draw_hearts(screen, health)
        floor_text = font.render("Floor " + str(current_floor) + " / " + str(TOTAL_FLOORS), True, (240, 240, 240))
        screen.blit(floor_text, (220, 55))

        key_message = "Find the gold key"
        if has_key:
            key_message = "Key collected - find the green door"
        key_text = font.render(key_message, True, (255, 215, 0))
        screen.blit(key_text, (WIDTH - key_text.get_width() - 50, 55))

        if game_over or escaped:

            message = "YOU DIED"
            if escaped:
                message = "You escaped the dungeon!"
            end_text = big_font.render(message, True, (255, 255, 255))
            restart_text = font.render("R to restart  or   Esc to quit", True, (230, 230, 230))
            screen.blit(end_text, end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
            screen.blit(restart_text, restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 35)))

        #update the screen and control game speed
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
