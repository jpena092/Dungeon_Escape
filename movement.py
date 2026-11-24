def move_character(character, walls, dx, dy):
    
   
    y_step = 0

    if dx > 0:
        x_step = 1
    if dx < 0:
        x_step = -1
    if dy > 0:
        y_step = 1
    if dy < 0:
        y_step = -1

    #x-axis horizontal plane
    for step in range(abs(dx)):
        character.x += x_step
        hit_wall = False

        for wall in walls:
            if character.colliderect(wall):
                hit_wall = True
                break

        if hit_wall:
    
            character.x -= x_step
            break

    #y-axis vertical plane
    for step in range(abs(dy)):
        character.y += y_step
        hit_wall = False

        for wall in walls:
            if character.colliderect(wall):
                hit_wall = True
                break

        if hit_wall:
            character.y -= y_step
            break


def move_player(player, walls, door, has_key, dx, dy):
    solid_walls = walls.copy()

  #  to prevent door from being able to be phase through 
    if not has_key:
        solid_walls.append(door)

    move_character(player, solid_walls, dx, dy)
