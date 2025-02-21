import pygame, os, sys
from button import Button

# Scaling factor for different monitors
SF = 0.75

# RGB
BLUE = (28, 69, 135)
YELLOW = (255, 217, 102)
WHITE = (255, 255, 255)
HOVER = (215, 252, 212)

# text sizes
TITLE_SIZE = 108
HEADER_SIZE = 64
TEXT_SIZE = 36

# heart sprites
heart = pygame.image.load('assets/heart-resize.png')
heart_icon = pygame.image.load('assets/heart.png')
heart_padding = heart.get_width() + 50

back_arrow = pygame.image.load('assets/back.png')
back_arrow_hover = pygame.image.load('assets/back-hover.png')

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
SCREEN = pygame.display.set_mode((WIDTH-10, HEIGHT-50), pygame.RESIZABLE)

pygame.display.set_icon(heart_icon)
pygame.display.set_caption("The Loyalty Quiz")


def get_font(size):
    return pygame.font.Font("assets/Orbitron-Bold.ttf", size)


def get_bold_font(size):
    return pygame.font.Font("assets/Orbitron-ExtraBold.ttf", size)


def play():
    my_font = get_font(HEADER_SIZE)
    categories_title = my_font.render("CATEGORIES", True, YELLOW)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill(BLUE)

        # Border
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(40, 40, WIDTH-90, HEIGHT-155), 5, 3)

        # Back button
        back_button = Button(image=back_arrow, pos=(100, 100),
                             text_input=None, font=get_font(TEXT_SIZE), base_color=YELLOW, hovering_color=YELLOW)
        back_button.hovering(mouse_pos, back_arrow, back_arrow_hover)
        back_button.update(SCREEN)

        # Categories title
        SCREEN.blit(categories_title, (WIDTH/2 - categories_title.get_width()/2, 100))

        # Category buttons
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(WIDTH/2-175*SF, HEIGHT/2-420*SF, 160*SF, 160*SF), 5, 3)  # Squares were previously 160
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(WIDTH/2+15*SF, HEIGHT/2-420*SF, 160*SF, 160*SF), 5, 3)
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(WIDTH/2-175*SF, HEIGHT/2-235*SF, 160*SF, 160*SF), 5, 3)
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(WIDTH/2+15*SF, HEIGHT/2-235*SF, 160*SF, 160*SF), 5, 3)
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(WIDTH/2-175*SF, HEIGHT/2-50*SF, 160*SF, 160*SF), 5, 3)
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(WIDTH/2+15*SF, HEIGHT/2-50*SF, 160*SF, 160*SF), 5, 3)
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(WIDTH/2-175*SF, HEIGHT/2+135*SF, 160*SF, 160*SF), 5, 3)
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(WIDTH/2+15*SF, HEIGHT/2+135*SF, 160*SF, 160*SF), 5, 3)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_for_input(mouse_pos):
                    main_menu()

        pygame.display.flip()


def main_menu():
    my_font_bold = get_bold_font(TITLE_SIZE)
    game_title = my_font_bold.render("LOYALTY QUIZ", True, YELLOW)

    play_button = Button(image=None, pos=(WIDTH/2, HEIGHT/2+50),
                         text_input="START GAME", font=get_font(TEXT_SIZE), base_color=WHITE, hovering_color=HOVER)
    quit_button = Button(image=None, pos=(WIDTH/2, HEIGHT/2+100),
                         text_input="QUIT", font=get_font(TEXT_SIZE), base_color=WHITE, hovering_color=HOVER)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill(BLUE)

        # Border
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(40, 40, WIDTH-90, HEIGHT-155), 5, 3)

        # Hearts
        SCREEN.blit(heart, heart.get_rect(center=(WIDTH/2 - heart_padding, HEIGHT/4)))
        SCREEN.blit(heart, heart.get_rect(center=(WIDTH/2, HEIGHT/4)))
        SCREEN.blit(heart, heart.get_rect(center=(WIDTH/2 + heart_padding, HEIGHT/4)))

        # Game title
        SCREEN.blit(game_title, (WIDTH/2 - game_title.get_width()/2, HEIGHT/2 - game_title.get_height()))

        # Buttons
        play_button.change_color(mouse_pos)
        play_button.update(SCREEN)
        quit_button.change_color(mouse_pos)
        quit_button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(mouse_pos):
                    play()
                if quit_button.check_for_input(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    main_menu()