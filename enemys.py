import pygame
from movement import move_character
from pathfinding import find_next_step, reset_paths

#enemy variables
basic_enemy = pygame.Rect(975, 675, 60, 60)  #(X,Y,W,H)
#xy are the starting positions | WH are the width and height
slow_enemy = pygame.Rect(600, 750, 60, 60)

basic_enemy_speed = 2
#enemy will shift 2 pixels per frame
slow_enemy_speed = 1
#this one moves slower but takes 2 hearts


def reset_enemys(floor):
    reset_paths()
   
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
    #find the next turn, even if we need to move away from the player first
    next_step = find_next_step(enemy, player, walls)
    if next_step is None:
        return

    next_x, next_y = next_step
    dx = 0
    dy = 0

    #checking horizontal axis for the next part of the route
    if enemy.x < next_x:
        dx = min(enemy_speed, next_x - enemy.x)
    if enemy.x > next_x:
        dx = -min(enemy_speed, enemy.x - next_x)

    #checking vertical axis, still only one axis per frame
    if enemy.y < next_y:
        dy = min(enemy_speed, next_y - enemy.y)
    if enemy.y > next_y:
        dy = -min(enemy_speed, enemy.y - next_y)

    move_character(enemy, walls, dx, dy)


def movement_enemy(player, walls):
    move_enemy(basic_enemy, basic_enemy_speed, player, walls)
    move_enemy(slow_enemy, slow_enemy_speed, player, walls)
