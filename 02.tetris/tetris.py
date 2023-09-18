import pygame


def shapes():
    # SHAPE FORMATS
    S =[['.....',
        '.....',
        '..00.',
        '.00..',
        '.....'],
        ['.....',
        '..0..',
        '..00.',
        '...0.',
        '.....']]

    Z = [['.....',
        '.....',
        '.00..',
        '..00.',
        '.....'],
        ['.....',
        '..0..',
        '.00..',
        '.0...',
        '.....']]

    I = [['.....',
        '..0..',
        '..0..',
        '..0..',
        '..0..'],
        ['.....',
        '0000.',
        '.....',
        '.....',
        '.....']]

    O = [['.....',
        '.....',
        '.00..',
        '.00..',
        '.....']]

    J = [['.....',
        '.0...',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..00.',
        '..0..',
        '..0..',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '...0.',
        '.....'],
        ['.....',
        '..0..',
        '..0..',
        '.00..',
        '.....']]

    L = [['.....',
        '...0.',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..0..',
        '..0..',
        '..00.',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '.0...',
        '.....'],
        ['.....',
        '.00..',
        '..0..',
        '..0..',
        '.....']]

    T = [['.....',
        '..0..',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..0..',
        '..00.',
        '..0..',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '..0..',
        '.....'],
        ['.....',
        '..0..',
        '.00..',
        '..0..',
        '.....']]

    shapes = [S, Z, I, O, J, L, T]
    shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255),
                    (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


def init():
    pygame.init()
    global SCREEN
    global WINDOW_WIDTH, WINDOW_HEIGHT
    global COLORWHITE

    # configuracion de la pantalla
    WINDOW_WIDTH, WINDOW_HEIGHT = 440, 600
    COLORWHITE = (200, 200, 200)
    COLORBLUE = (0, 0, 128)

    # iniciamos nuestra pantalla
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Juega tetris')
    pygame.display.flip()
    # añadimos el texto
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render('Juega tetris', True, COLORBLUE, COLORWHITE)
    SCREEN.blit(text, ((320), (150)))

    running = True

    while running:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


def drawGrid():
    blockSize = 40
    for x in range(0, round(WINDOW_WIDTH * 0.7), blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            square = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, COLORWHITE, square, 1)


init()
