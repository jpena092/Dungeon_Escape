from collections import deque
import pygame
from settings import WIDTH, HEIGHT

#small steps for planning, the enemys still move at their normal speed
GRID_SIZE = 15
grid_key = None
open_spots = set()
goal_key = None
distances = {}


def reset_paths():
    global grid_key, open_spots, goal_key, distances
    grid_key = None
    open_spots = set()
    goal_key = None
    distances = {}


def clear_turn(start, finish, size, walls):
    x, y = start
    next_x, next_y = finish
    width, height = size

    #check the whole space we would cross, not just the end position
    horizontal_first = [
        pygame.Rect(min(x, next_x), y, width + abs(next_x - x), height),
        pygame.Rect(next_x, min(y, next_y), width, height + abs(next_y - y)),
    ]
    vertical_first = [
        pygame.Rect(x, min(y, next_y), width, height + abs(next_y - y)),
        pygame.Rect(min(x, next_x), next_y, width + abs(next_x - x), height),
    ]

    turns = [(horizontal_first, (next_x, y)), (vertical_first, (x, next_y))]
    if abs(next_y - y) >= abs(next_x - x):
        turns.reverse()

    for spaces, corner in turns:
        if spaces[0].collidelist(walls) == -1 and spaces[1].collidelist(walls) == -1:
            if corner != start:
                return corner
            return finish

    return None


def get_distances(enemy, player, walls):
    global grid_key, open_spots, goal_key, distances
    wall_positions = tuple(tuple(wall) for wall in walls)
    new_grid_key = (enemy.size, wall_positions)

    if new_grid_key != grid_key:
        #mark spots where the whole enemy fits
        open_spots = set()
        test_enemy = pygame.Rect(0, 0, enemy.width, enemy.height)
        for x in range(0, WIDTH - enemy.width + 1, GRID_SIZE):
            for y in range(0, HEIGHT - enemy.height + 1, GRID_SIZE):
                test_enemy.topleft = (x, y)
                if test_enemy.collidelist(walls) == -1:
                    open_spots.add((x, y))
        grid_key = new_grid_key
        goal_key = None

    #player movement is not locked to the grid, check the nearby spots
    player_x = player.x // GRID_SIZE * GRID_SIZE
    player_y = player.y // GRID_SIZE * GRID_SIZE
    goals = []
    for x in (player_x, player_x + GRID_SIZE):
        for y in (player_y, player_y + GRID_SIZE):
            spot = (x, y)
            if spot in open_spots:
                if clear_turn(player.topleft, spot, enemy.size, walls) is not None:
                    goals.append(spot)

    if tuple(goals) != goal_key:
        #work out from the player, so both enemys can share these directions
        distances = {}
        checking = deque(goals)
        for spot in goals:
            distances[spot] = 0

        while checking:
            x, y = checking.popleft()
            for dx, dy in [(GRID_SIZE, 0), (-GRID_SIZE, 0),
                           (0, GRID_SIZE), (0, -GRID_SIZE)]:
                next_spot = (x + dx, y + dy)
                if next_spot in open_spots and next_spot not in distances:
                    distances[next_spot] = distances[(x, y)] + 1
                    checking.append(next_spot)
        goal_key = tuple(goals)

    return distances


def find_next_step(enemy, player, walls):
    #use a clear direct route when there is one
    direct_step = clear_turn(enemy.topleft, player.topleft, enemy.size, walls)
    if direct_step is not None:
        return direct_step

    routes = get_distances(enemy, player, walls)
    enemy_x = enemy.x // GRID_SIZE * GRID_SIZE
    enemy_y = enemy.y // GRID_SIZE * GRID_SIZE
    best_score = None
    best_step = None

    #join a nearby route without snapping or teleporting onto the grid
    for x in range(enemy_x - GRID_SIZE, enemy_x + GRID_SIZE * 3, GRID_SIZE):
        for y in range(enemy_y - GRID_SIZE, enemy_y + GRID_SIZE * 3, GRID_SIZE):
            spot = (x, y)
            if spot not in routes:
                continue
            corner = clear_turn(enemy.topleft, spot, enemy.size, walls)
            if corner is None:
                continue

            distance_to_spot = abs(x - enemy.x) + abs(y - enemy.y)
            score = (routes[spot] * GRID_SIZE + distance_to_spot, routes[spot])
            if best_score is None or score < best_score:
                best_score = score
                best_step = corner

    #no route means wait, dont try to push through a wall
    return best_step
