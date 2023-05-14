import pygame

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# initialize pygame
pygame.init()

# set the dimensions of the window
WINDOW_SIZE = [640, 640]
screen = pygame.display.set_mode(WINDOW_SIZE)

# set the title of the window
pygame.display.set_caption("Chess")

# create the chessboard
board_size = 8
cell_size = 80
board = pygame.Surface((cell_size * board_size, cell_size * board_size))
for row in range(board_size):
    for col in range(board_size):
        if (row + col) % 2 == 0:
            color = WHITE
        else:
            color = BLACK
        pygame.draw.rect(board, color, (col * cell_size, row * cell_size, cell_size, cell_size))

# draw the chessboard on the screen
screen.blit(board, (0, 0))

# update the display
pygame.display.flip()

# run the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the display
    pygame.display.update()

# quit pygame
pygame.quit()
