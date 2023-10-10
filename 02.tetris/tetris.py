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


# clase para la estructura
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0
        pass

def create_grid(locked_pos = {}):
      grid = [[(0,0,0) for x in range(10)] for x in range(20)]
      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  if (j, i) in locked_pos:
                        d = locked_pos[(j, i)]
                        grid[i][j] = d
      return grid


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def init():
    create_grid()
    pygame.init()
    global SCREEN
    global WINDOW_WIDTH, WINDOW_HEIGHT, PLAY_WIDTH, PLAY_HEIGHT, BLOCK_SIZE
    global COLORWHITE, COLORBLUE
    global TOP_LEFT_X, TOP_LEFT_Y

    # configuracion de la pantalla
    WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
    PLAY_WIDTH, PLAY_HEIGHT = 400, 800
    BLOCK_SIZE = 40

    TOP_LEFT_X = (WINDOW_WIDTH - PLAY_WIDTH) // 2 #usamos el "//" para que nos retorne un int
    TOP_LEFT_Y = (WINDOW_HEIGHT - PLAY_HEIGHT)
    COLORWHITE = (200, 200, 200)
    COLORBLUE = (0, 0, 128)

    # iniciamos nuestra pantalla
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    drawWindow(SCREEN)

    # obtenemos las piezas
    change_piece = False
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:
                        current_piece.x -= 1
                        if not(valid_space(current_piece, True)):
                              continue
                  if event.key == pygame.K_RIGHT:
                        current_piece.x += 1
                  if event.key == pygame.K_DOWN:
                        current_piece.y += 1
                  if event.key == pygame.k_UP:
                        current_piece.rotation += 1


        pygame.display.update()

def drawWindow(screen):
    pygame.display.set_caption('Juega tetris')
    pygame.display.flip()
    # añadimos el texto
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render('Juega tetris', True, COLORBLUE, COLORWHITE)
    SCREEN.blit(text, ((320), (150)))

    drawGrid()

def drawGrid(screen):
    screen.fill((0,0,0))
    pygame.font.init() #iniciamos los fonts de pygame
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Juega tetris', 1, (255, 255, 255))

    screen.blit(label, (TOP_LEFT_X + PLAY_WIDTH // 2 - (label.get_width()), 30))

    blockSize = 40
    for x in range(0, round(WINDOW_WIDTH * 0.7), blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            square = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, COLORWHITE, square, 1)

def valid_space(current_piece, grid):
      return True;

init()
