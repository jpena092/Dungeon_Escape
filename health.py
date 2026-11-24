import pygame
from settings import MAX_HEALTH, DAMAGE_COOLDOWN


def check_damage(player, basic_enemy, slow_enemy, health, last_hit, current_time):
    #give the player a little time to get away after being hit
    if current_time - last_hit < DAMAGE_COOLDOWN:
        return health, last_hit

    damage = 0

    #check the stronger enemy first touching both at once will only count the stronger enemy 
    if player.colliderect(slow_enemy):
        damage = 2
    elif player.colliderect(basic_enemy):
        damage = 1

    if damage > 0:
        health -= damage
        if health < 0:
            health = 0
        last_hit = current_time

    return health, last_hit


def draw_hearts(screen, health):
    for heart in range(MAX_HEALTH):
        x = 50 + heart * 50
        y = 62
        color = (80, 65, 65)

        if heart < health:
            color = (230, 55, 65)

        #two circles with a  triangle make the heart adjust if needed 
        pygame.draw.circle(screen, color, (x - 8, y), 10)
        pygame.draw.circle(screen, color, (x + 8, y), 10)
        pygame.draw.polygon(screen, color, [
            (x - 18, y + 2),
            (x + 18, y + 2),
            (x, y + 25),
        ])
