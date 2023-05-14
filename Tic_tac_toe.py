import pygame

# Initialize pygame
pygame.init()

# Set the size of the window
WINDOW_SIZE = (300, 300)

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the window
pygame.display.set_caption("Tic Tac Toe")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define the size of the board
BOARD_SIZE = 3

# Define the size of each cell
CELL_SIZE = 100

# Define the size of the margin
MARGIN_SIZE = 10

# Define the font
FONT_SIZE = 40
FONT = pygame.font.Font(None, FONT_SIZE)

# Define the game board
board = [['', '', ''], ['', '', ''], ['', '', '']]

# Define the player
player = 'X'

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse
            pos = pygame.mouse.get_pos()
            # Calculate the row and column of the cell
            row = pos[1] // (CELL_SIZE + MARGIN_SIZE)
            col = pos[0] // (CELL_SIZE + MARGIN_SIZE)
            # Check if the cell is empty
            if board[row][col] == '':
                # Set the value of the cell to the player's mark
                board[row][col] = player
                # Switch the player
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'

    # Clear the screen
    screen.fill(WHITE)

    # Draw the cells
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Calculate the position of the cell
            x = col * (CELL_SIZE + MARGIN_SIZE) + MARGIN_SIZE
            y = row * (CELL_SIZE + MARGIN_SIZE) + MARGIN_SIZE
            # Draw the cell
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 2)
            # Draw the mark
            mark = board[row][col]
            if mark == 'X':
                text = FONT.render(mark, True, RED)
                screen.blit(text, (x + CELL_SIZE // 2 - FONT_SIZE // 2, y + CELL_SIZE // 2 - FONT_SIZE // 2))
            elif mark == 'O':
                pygame.draw.circle(screen, RED, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - FONT_SIZE // 2, 2)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
