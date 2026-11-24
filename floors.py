import pygame
from settings import WIDTH, HEIGHT


def create_floor(floor):
    walls = [
        pygame.Rect(0, 0, WIDTH, 30),
        pygame.Rect(0, HEIGHT - 30, WIDTH, 30),
        pygame.Rect(0, 0, 30, HEIGHT),
        pygame.Rect(WIDTH - 30, 0, 30, HEIGHT),
    ]

    if floor == 1:
        walls.extend([
            pygame.Rect(450, 225, 45, 375),
            pygame.Rect(450, 600, 300, 45),
            pygame.Rect(750, 375, 45, 270),
        ])
        key = pygame.Rect(975, 150, 45, 45)

    elif floor == 2:
        walls.extend([
            pygame.Rect(300, 150, 45, 600),
            pygame.Rect(300, 150, 600, 45),
            pygame.Rect(855, 150, 45, 600),
        ])
        key = pygame.Rect(900, 150, 45, 45)

    elif floor == 3:
        walls.extend([
            pygame.Rect(225, 225, 45, 450),
            pygame.Rect(225, 225, 450, 45),
            pygame.Rect(600, 225, 45, 450),
            pygame.Rect(450, 630, 450, 45),
        ])
        key = pygame.Rect(900, 150, 45, 45)

    elif floor == 4:
        walls.extend([
            pygame.Rect(300, 225, 45, 345),
            pygame.Rect(300, 570, 345, 45),
            pygame.Rect(600, 360, 45, 255),
            pygame.Rect(780, 150, 45, 480),
            pygame.Rect(780, 150, 300, 45),
            pygame.Rect(1035, 150, 45, 480),
            pygame.Rect(510, 735, 390, 45),
        ])
        key = pygame.Rect(915, 240, 45, 45)

    elif floor == 5:
        walls.extend([
            pygame.Rect(300, 150, 705, 45),
            pygame.Rect(300, 150, 45, 210),
            pygame.Rect(300, 510, 45, 300),
            pygame.Rect(300, 765, 705, 45),
            pygame.Rect(960, 150, 45, 435),
            pygame.Rect(960, 720, 45, 90),
            pygame.Rect(480, 360, 525, 45),
            pygame.Rect(600, 360, 45, 285),
            pygame.Rect(600, 600, 225, 45),
            pygame.Rect(120, 600, 45, 135),
            pygame.Rect(120, 690, 180, 45),
        ])
        key = pygame.Rect(825, 240, 45, 45)

    else:
        walls.extend([
            pygame.Rect(255, 150, 780, 45),
            pygame.Rect(255, 150, 45, 615),
            pygame.Rect(255, 720, 270, 45),
            pygame.Rect(690, 720, 345, 45),
            pygame.Rect(990, 150, 45, 615),
            pygame.Rect(420, 315, 450, 45),
            pygame.Rect(420, 315, 45, 285),
            pygame.Rect(420, 555, 285, 45),
            pygame.Rect(825, 315, 45, 120),
            pygame.Rect(690, 600, 45, 120),
            pygame.Rect(630, 360, 45, 105),
        ])
        key = pygame.Rect(510, 420, 45, 45)

    door = pygame.Rect(1080, 750, 60, 120)
    return walls, key, door