# Dungeon Escape
import pygame
# Making the game window dimensions
pygame.init()
WIDTH= 800
HEIGHT =600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Escape")
clock = pygame.time.Clock()
#PLAYER VARIABLES

player = pygame.Rect(100, 100, 40, 40)
player_speed = 5
current_floor = 1
has_key = False
def create_floor(floor):
    walls = [
            # Outer walls
        pygame.Rect(0, 0, 800, 20),
        pygame.Rect(0, 580, 800, 20),
        pygame.Rect(0, 0, 20, 600),
        pygame.Rect(780, 0, 20, 600),
        ]
    if floor == 1:
        walls.extend([
        pygame.Rect(300, 150, 30, 250),
        pygame.Rect(300, 400, 200, 30),
        pygame.Rect(500, 250, 30, 180),
        ])
        key = pygame.Rect(650, 100, 30, 30)
        door = pygame.Rect(720, 500, 40, 80)
    elif floor == 2:
        walls.extend([
        pygame.Rect(200, 100, 30, 400),
        pygame.Rect(200, 100, 400, 30),
        pygame.Rect(570, 100, 30, 400),
        ])
        key = pygame.Rect(600, 100, 30, 30)
        door = pygame.Rect(720, 500, 40, 80)
    else:
        walls.extend([
        pygame.Rect(150, 150, 30, 300),
        pygame.Rect(150, 150, 300, 30),
        pygame.Rect(400, 150, 30, 300),
        pygame.Rect(300, 420, 300, 30),
        ])
        key = pygame.Rect(600, 100, 30, 30)
        door = pygame.Rect(720, 500, 40, 80)
    return walls, key, door
walls, key, door = create_floor(current_floor)

#walls = [
    # Outer walls
    #pygame.Rect(0, 0, 800, 20),
    #pygame.Rect(0, 580, 800, 20),
    #pygame.Rect(0, 0, 20, 600),
   # pygame.Rect(780, 0, 20, 600),
    # Inner walls
    #pygame.Rect(300, 150, 30, 250),
   # pygame.Rect(300, 400, 200, 30),
  #  pygame.Rect(500, 250, 30, 180),
#] 
#key = pygame.Rect(650, 100, 30, 30)
#has_key = False
#door = pygame.Rect(720, 500, 40, 80)

def move_player(dx, dy):
    player.x += dx
    for wall in walls:
        if player.colliderect(wall):
            if dx > 0:  # Moving right; Hit the left side of the wall
                player.right = wall.left
            elif dx < 0:  # Moving left; Hit the right side of the wall
                player.left = wall.right
    player.y += dy
    for wall in walls:
        if player.colliderect(wall):
            if dy > 0:  # Moving down; Hit the top side of the wall
                player.bottom = wall.top
            elif dy < 0:  # Moving up; Hit the bottom side of the wall
                player.top = wall.bottom
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Key inputs for player movement
    keys = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if keys[pygame.K_a]:
        dx = -player_speed
    if keys[pygame.K_d]:
        dx = player_speed
    if keys[pygame.K_w]:
        dy = -player_speed
    if keys[pygame.K_s]:
        dy = player_speed
    move_player(dx, dy)

    if key is not None and player.colliderect(key):
        has_key = True
        key = None  # Remove the key from the floor
    if player.colliderect(door):
        if has_key:
            if current_floor < 3:
                current_floor += 1
                has_key = False
                walls, key, door = create_floor(current_floor)
                player.x = 100 
                player.y = 100
            else:
                print("Congratulations! You've escaped the dungeon!")
                running = False
        else:
                if player.centerx < door.centerx:
                    player.right = door.left
                else:
                    player.left = door.right

                #walls, key, door = create_floor(current_floor)
                #player.x, player.y = 100, 100
                #has_key = False

    # Draw Background and Player
    screen.fill((30, 30, 30))
    for wall in walls:
        pygame.draw.rect(screen, (90, 90, 90), wall) 
    if key is not None:
        pygame.draw.rect(screen, (255, 215, 0), key)
    #Draw door
    pygame.draw.rect(screen, (120, 70, 30), door)    
    #Draw Player
    pygame.draw.rect(screen, (50, 150, 255), player)
    #Update the screen
    pygame.display.flip()
    #Control game speed
    clock.tick(60)
pygame.quit()
