import pygame
import random

# SHAPE FORMATS
S = [['.....',
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

# declaramos nuestras variables globales
global WINDOW_WIDTH, WINDOW_HEIGHT, PLAY_WIDTH, PLAY_HEIGHT, BLOCK_SIZE
global COLORWHITE, COLORBLUE
global TOP_LEFT_X, TOP_LEFT_Y

# configuracion de la pantalla
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
PLAY_WIDTH, PLAY_HEIGHT = 400, 800
BLOCK_SIZE = 40

# usamos el "//" para que nos retorne un int
TOP_LEFT_X = (WINDOW_WIDTH - PLAY_WIDTH) // 2
TOP_LEFT_Y = (WINDOW_HEIGHT - PLAY_HEIGHT)
COLORWHITE = (200, 200, 200)
COLORBLUE = (0, 0, 128)

# controlador principal
def main_controller(screen):
    init(screen)

# clase para la estructura


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0
        pass


def create_grid(locked_pos={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                d = locked_pos[(j, i)]
                grid[i][j] = d
    return grid

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] -2, pos[1] -4)

    return positions


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def init(screen):


    locked_positions = {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    fall_speed = 0.27


    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.rotation -= 1

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

        if check_lost(locked_positions):
            run = False
            pygame.display.quit()

        drawWindow(screen, grid)


def drawGrid(screen, grid):
    sx = TOP_LEFT_X
    sy = TOP_LEFT_Y

    for i in range(len(grid)):
        pygame.draw.line(screen, (128, 128, 128), (sx, sy + i * BLOCK_SIZE), (sx + PLAY_WIDTH, sy + i * BLOCK_SIZE))
        for j in range(len(grid[i])):
            pygame.draw.line(screen, (128, 128, 128), (sx + j * BLOCK_SIZE, sy), (sx + j * BLOCK_SIZE, sy + PLAY_HEIGHT))


def drawWindow(screen, grid):
    screen.fill((0,0,0))
    pygame.font.init()  # iniciamos los fonts de pygame
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Juega tetris', 1, (255, 255, 255))

    screen.blit(label, (TOP_LEFT_X + PLAY_WIDTH //
                2 - (label.get_width()), 30))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(screen, grid[i][j], (TOP_LEFT_X + j * BLOCK_SIZE,
                             TOP_LEFT_Y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    pygame.draw.rect(screen, (255, 0, 0), (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 4)


    drawGrid(screen, grid)
    pygame.display.update()


def valid_space(current_piece, grid):
    accepted_pos = [[(j, i) for j in range(10)] for i in range(20)]
    accepted_pos = [ j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(current_piece)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y <  1:
            return True

    return False


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tetris game')


main_controller(window)
