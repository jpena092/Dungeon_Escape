import pygame
from settings import WIDTH, HEIGHT

# Colors
WHITE = (245, 245, 245)
DARK = (22, 24, 32)
GOLD = (255, 215, 0)
BUTTON_COLOR = (65, 75, 95)
BUTTON_HOVER = (95, 115, 145)


def draw_button(screen, font, text, rect, mouse_pos):

    color = BUTTON_HOVER if rect.collidepoint(mouse_pos) else BUTTON_COLOR

    pygame.draw.rect(screen, color, rect, border_radius=12)
    pygame.draw.rect(screen, WHITE, rect, 2, border_radius=12)

    label = font.render(text, True, WHITE)
    screen.blit(label, label.get_rect(center=rect.center))

def main_menu(screen, clock):

    title_font = pygame.font.Font(None, 92)
    font = pygame.font.Font(None, 38)

    # Four menu buttons
    start_button = pygame.Rect(450, 300, 300, 65)
    instructions_button = pygame.Rect(450, 390, 300, 65)
    credits_button = pygame.Rect(450, 480, 300, 65)
    quit_button = pygame.Rect(450, 570, 300, 65)

    while True:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return "quit"

                if event.key == pygame.K_RETURN:
                    return "start"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if start_button.collidepoint(event.pos):
                    return "start"

                elif instructions_button.collidepoint(event.pos):
                    show_instructions(screen, clock)

                elif credits_button.collidepoint(event.pos):
                    show_credits(screen, clock)

                elif quit_button.collidepoint(event.pos):
                    return "quit"

        screen.fill(DARK)

        title = title_font.render("DUNGEON ESCAPE", True, GOLD)
        subtitle = font.render(
            "Find the keys. Survive the floors. Escape.",
            True,
            WHITE
        )

        screen.blit(title, title.get_rect(center=(WIDTH // 2, 150)))
        screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 230)))

        # Draw all four buttons
        draw_button(screen, font, "START GAME", start_button, mouse_pos)
        draw_button(screen, font, "HOW TO PLAY", instructions_button, mouse_pos)
        draw_button(screen, font, "CREDITS", credits_button, mouse_pos)
        draw_button(screen, font, "QUIT", quit_button, mouse_pos)

        pygame.display.flip()
        clock.tick(60)

def show_instructions(screen, clock):

    title_font = pygame.font.Font(None, 64)
    font = pygame.font.Font(None, 32)

    instructions = [
        "WASD or arrow keys: Move",
        "Find the gold key on each floor.",
        "Unlock the door to progress.",
        "Avoid enemies and protect your hearts.",
        "Red enemy: 1 heart of damage.",
        "Purple enemy: 2 hearts of damage.",
        "Escape all 6 floors to win."
    ]

    back_button = pygame.Rect(WIDTH // 2 - 150, 530, 300, 55)

    while True:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                    return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if back_button.collidepoint(event.pos):
                    return

        screen.fill(DARK)

        title = title_font.render("HOW TO PLAY", True, GOLD)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 130)))

        for i, line in enumerate(instructions):

            text = font.render(line, True, WHITE)

            screen.blit(
                text,
                text.get_rect(center=(WIDTH // 2, 220 + i * 40))
            )

        draw_button(screen, font, "BACK TO MENU", back_button, mouse_pos)

        pygame.display.flip()
        clock.tick(60)


def show_credits(screen, clock):

    title_font = pygame.font.Font(None, 72)
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 28)

    back_button = pygame.Rect(WIDTH // 2 - 150, 510, 300, 55)

    credits = [
        "Developed by:",
        "Jesse Pena",
        "Ryan Garcia",
        "",
        "Programming Languages Project",
        "Dungeon Escape - 2026"
    ]

    while True:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                    return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if back_button.collidepoint(event.pos):
                    return

        screen.fill(DARK)

        title = title_font.render("CREDITS", True, GOLD)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 110)))

        for i, line in enumerate(credits):

            current_font = small_font if i >= 4 else font

            text = current_font.render(line, True, WHITE)

            screen.blit(
                text,
                text.get_rect(center=(WIDTH // 2, 200 + i * 45))
            )

        draw_button(screen, font, "BACK TO MENU", back_button, mouse_pos)

        pygame.display.flip()
        clock.tick(60)
