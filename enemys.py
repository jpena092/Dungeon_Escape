import pygame
from movement import move_character

#enemy variables
basic_enemy = pygame.Rect(975, 675, 60, 60)  #(X,Y,W,H)
#xy are the starting positions | WH are the width and height
slow_enemy = pygame.Rect(600, 750, 60, 60)

basic_enemy_speed = 2
#enemy will shift 2 pixels per frame
slow_enemy_speed = 1
#this one moves slower but takes 2 hearts


def reset_enemys(floor):
   
    basic_enemy.topleft = (975, 675)
    slow_enemy.topleft = (600, 750)

    if floor == 2:
        basic_enemy.topleft = (975, 600)
        slow_enemy.topleft = (600, 675)

    if floor == 3:
        basic_enemy.topleft = (975, 675)
        slow_enemy.topleft = (750, 750)

    if floor == 4:
        basic_enemy.topleft = (675, 450)
        slow_enemy.topleft = (900, 450)

    if floor == 5:
        basic_enemy.topleft = (690, 450)
        slow_enemy.topleft = (480, 240)

    if floor == 6:
        basic_enemy.topleft = (900, 240)
        slow_enemy.topleft = (360, 450)


def move_enemy(enemy, enemy_speed, player, walls):
    #player control tracking of player to enemy
   
    dx = 0
    dy = 0

    #enemy checking for player on horizontal axis
    if enemy.x < player.x:
        #returns positive if we need to shift right
        dx = min(enemy_speed, player.x - enemy.x)
    if enemy.x > player.x:
        #returns negative if we need to shift left
        dx = -min(enemy_speed, enemy.x - player.x)

    #checking vertical axis
    if enemy.y < player.y:
        dy = min(enemy_speed, player.y - enemy.y)
        #positive shift down
    if enemy.y > player.y:
        dy = -min(enemy_speed, enemy.y - player.y)
        #negative shift up

    x_distance = abs(player.x - enemy.x)
    y_distance = abs(player.y - enemy.y)
    old_x = enemy.x
    old_y = enemy.y

    #try the axis with the bigger distance first
    if x_distance > y_distance:
        move_character(enemy, walls, dx, 0)

        #if x is blocked try y instead
        if enemy.x == old_x:
            move_character(enemy, walls, 0, dy)

    else:
        move_character(enemy, walls, 0, dy)

        #if y is blocked try x instead
        if enemy.y == old_y:
            move_character(enemy, walls, dx, 0)


def movement_enemy(player, walls):
    move_enemy(basic_enemy, basic_enemy_speed, player, walls)
    move_enemy(slow_enemy, slow_enemy_speed, player, walls)
