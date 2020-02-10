import math
import random
import pygame
import sys

#########################################
# Define logic for movement. Allow movement
# even to occur only when barrier is not
# detected.
#
# Return position of new x and y coords
# given button press detected using event.
#########################################

def move(x_pos, y_pos, dist, grid, grid_size, sq_num):
    """

    :param x_pos:
    :param y_pos:
    :param dist:
    :param grid:
    :param grid_size:
    :param sq_num:
    :return:
    """
    # Calculate some helpful values
    sq_size = grid_size / sq_num
    cell_row_col = get_cell(grid_size, sq_num, x_pos, y_pos)
    # Pixel edges of the grid cell
    left_pixel = cell_row_col[1] * sq_size
    right_pixel = cell_row_col[1] * sq_size + sq_size
    top_pixel = cell_row_col[0] * sq_size
    bottom_pixel = cell_row_col[0] * sq_size + sq_size

    # Left logic
    if event.key == pygame.K_LEFT:
        # Set boolean value of whether the player is on-screen
        will_move = x_pos > 0
        # If player is on-screen and touching left pixel of cell
        if (will_move and x_pos == left_pixel):
            # Set boolean value of whether the cell is not a barrier
            will_move = (grid[cell_row_col[0]][cell_row_col[1] - 1] == 0
                         or grid[cell_row_col[0]][cell_row_col[1] - 1] == 2)
            # If player doesn't have barrier and not touching top pixel of cell
            if (will_move and not (y_pos == top_pixel)):
                # Set boolean value of whether the cell is not a barrier
                will_move = (grid[cell_row_col[0] + 1][cell_row_col[1] - 1] == 0
                             or grid[cell_row_col[0] + 1][cell_row_col[1] - 1] == 2)
        # Move only if final flag is true
        if (will_move):
            x_pos -= dist

    # Right logic
    if event.key == pygame.K_RIGHT:
        will_move = x_pos < grid_size - sq_size
        if will_move and x_pos == left_pixel:
            will_move = (grid[cell_row_col[0]][cell_row_col[1] + 1] == 0
                         or grid[cell_row_col[0]][cell_row_col[1] + 1] == 2)
            if (will_move and not (y_pos == top_pixel)):
                will_move = (grid[cell_row_col[0] + 1][cell_row_col[1] + 1] == 0
                             or grid[cell_row_col[0] + 1][cell_row_col[1] + 1] == 2)
        if (will_move):
            x_pos += dist

    # Up logic
    if event.key == pygame.K_UP:
        will_move = y_pos > 0
        if (will_move and y_pos == top_pixel):
            will_move = (grid[cell_row_col[0] - 1][cell_row_col[1]] == 0
                         or grid[cell_row_col[0] - 1][cell_row_col[1]] == 2)
            if (will_move and not (x_pos == left_pixel)):
                will_move = (grid[cell_row_col[0] - 1][cell_row_col[1] + 1] == 0
                             or grid[cell_row_col[0] - 1][cell_row_col[1] + 1] == 2)
        if (will_move):
            y_pos -= dist

    # Down logic
    if event.key == pygame.K_DOWN:
        will_move = y_pos < grid_size - sq_size
        if (will_move and y_pos == top_pixel):
            will_move = (grid[cell_row_col[0] + 1][cell_row_col[1]] == 0
                         or grid[cell_row_col[0] + 1][cell_row_col[1]] == 2)
            if (will_move and not (x_pos == left_pixel)):
                will_move = (grid[cell_row_col[0] + 1][cell_row_col[1] + 1] == 0
                             or grid[cell_row_col[0] + 1][cell_row_col[1] + 1] == 2)
        if (will_move):
            y_pos += dist

    return x_pos, y_pos


def enemy_move(enemy_x, enemy_y, player_x, player_y, dist, grid, grid_size, sq_num):
    """

    :param enemy_x:
    :param enemy_y:
    :param player_x:
    :param player_y:
    :param dist:
    :param grid:
    :param grid_size:
    :param sq_num:
    :return:
    """
    # Calculate best direction
    global direction
    d_left = calculate_distance(player_x, enemy_x - dist, player_y, enemy_y)
    d_right = calculate_distance(player_x, enemy_x + dist, player_y, enemy_y)
    d_up = calculate_distance(player_x, enemy_x, player_y, enemy_y - dist)
    d_down = calculate_distance(player_x, enemy_x - dist, player_y, enemy_y + dist)
    if min(d_left, d_right, d_up, d_down) == d_left:
        direction = 'L'
    elif min(d_left, d_right, d_up, d_down) == d_right:
        direction = 'R'
    elif min(d_left, d_right, d_up, d_down) == d_up:
        direction = 'U'
    elif min(d_left, d_right, d_up, d_down) == d_down:
        direction = 'D'

    # Calculate some helpful values
    sq_size = grid_size / sq_num
    cell_row_col = get_cell(grid_size, sq_num, enemy_x, enemy_y)
    # Pixel edges of the grid cell
    left_pixel = cell_row_col[1] * sq_size
    right_pixel = cell_row_col[1] * sq_size + sq_size
    top_pixel = cell_row_col[0] * sq_size
    bottom_pixel = cell_row_col[0] * sq_size + sq_size

    # Left logic
    if direction == 'L':
        # Set boolean value of whether the enemy is on-screen
        will_move = enemy_x > 0
        # If enemy is on-screen and touching left pixel of cell
        if (will_move and enemy_x == left_pixel):
            # Set boolean value of whether the cell is not a barrier
            will_move = (grid[cell_row_col[0]][cell_row_col[1] - 1] == 0
                         or grid[cell_row_col[0]][cell_row_col[1] - 1] == 2)
            # If enemy doesn't have barrier and not touching top pixel of cell
            if (will_move and not (enemy_y == top_pixel)):
                # Set boolean value of whether the cell is not a barrier
                will_move = (grid[cell_row_col[0] + 1][cell_row_col[1] - 1] == 0
                             or grid[cell_row_col[0] + 1][cell_row_col[1] - 1] == 2)
        # Move only if final flag is true
        if (will_move):
            enemy_x -= dist

    # Right logic
    if direction == 'R':
        will_move = enemy_x < grid_size - sq_size
        if (will_move and enemy_x == left_pixel):
            will_move = (grid[cell_row_col[0]][cell_row_col[1] + 1] == 0
                         or grid[cell_row_col[0]][cell_row_col[1] + 1] == 2)
            if (will_move and not (enemy_y == top_pixel)):
                will_move = (grid[cell_row_col[0] + 1][cell_row_col[1] + 1] == 0
                             or grid[cell_row_col[0] + 1][cell_row_col[1] + 1] == 2)
        if (will_move):
            enemy_x += dist

    # Up logic
    if direction == 'U':
        will_move = enemy_y > 0
        if (will_move and enemy_y == top_pixel):
            will_move = (grid[cell_row_col[0] - 1][cell_row_col[1]] == 0
                         or grid[cell_row_col[0] - 1][cell_row_col[1]] == 2)
            if (will_move and not (enemy_x == left_pixel)):
                will_move = (grid[cell_row_col[0] - 1][cell_row_col[1] + 1] == 0
                             or grid[cell_row_col[0] - 1][cell_row_col[1] + 1] == 2)
        if (will_move):
            enemy_y -= dist

    # Down logic
    if direction == 'D':
        will_move = enemy_y < grid_size - sq_size
        if (will_move and enemy_y == top_pixel):
            will_move = (grid[cell_row_col[0] + 1][cell_row_col[1]] == 0
                         or grid[cell_row_col[0] + 1][cell_row_col[1]] == 2)
            if (will_move and not (enemy_x == left_pixel)):
                will_move = (grid[cell_row_col[0] + 1][cell_row_col[1] + 1] == 0
                             or grid[cell_row_col[0] + 1][cell_row_col[1] + 1] == 2)
        if (will_move):
            enemy_y += dist

    return enemy_x, enemy_y


def calculate_distance(x_1, x_2, y_1, y_2):
    """

    :param x_1:
    :param x_2:
    :param y_1:
    :param y_2:
    :return:
    """
    return math.sqrt((math.pow((y_2 - y_1), 2)) + (math.pow((x_2 - x_1), 2)))


#########################################
# Generates a grid as a list structure
# with squares being placed randomly

# prob is the probability that a 1 shows up
# sq_num is the number of square in each row and column
#########################################

def generate_grid(prob, sq_num):
    """

    :param prob:
    :param sq_num:
    :return:
    """
    grid = []

    # Your code here
    for rows in range(0, sq_num):
        grid.append(sq_num * [0])

    for list1 in range(0, sq_num):
        for element in range(0, sq_num):
            if (random.random() <= prob):
                grid[list1][element] = 1
    # clear barrier at player start location
    grid[0][0] = 0

    return grid


#########################################
# Use the grid generated by generate_grid()
# and draw on the display surface

# grid is the list structure with 1 if a barrier will be plotted there, 0 otherwise
# sq_size is the length and width of each cell within the grid
# sq_num is the number of squares in each row and column
# surf is the name of the display surface to which we are plotting in pygame
# im is the name of the image representing the barrier image
#########################################

def draw_barrier(grid, sq_size, sq_num, surf, im):
    """

    :param grid:
    :param sq_size:
    :param sq_num:
    :param surf:
    :param im:
    """
    # Your code here
    for row in range(0, sq_num):
        for col in range(0, sq_num):
            if grid[row][col] == 1:
                surf.blit(im, (sq_size * col, sq_size * row))


#########################################
# Given the player's current location as
# the coordinate (x_player,y_player),
# returns the cell row/column pair
# corresponding to its location in the grid

# m is the length and width of the game window
# cell_num is the number of cells in each row and column
#########################################
def get_cell(m, cell_num, x_player, y_player):
    """

    :param m:
    :param cell_num:
    :param x_player:
    :param y_player:
    :return:
    """
    # Your code here
    sq_size = m / cell_num

    row = int(y_player / sq_size)
    col = int(x_player / sq_size)

    return (row, col)


#########################################
# Given knowledge of an x position and y position
# produces a 4-tuple of the physical coordinates of each of the
# four corners of the square

# m is the length and width of the game window
# cell_num is the number of cells in each row and column
# x is the current x position
# y is the current y position
#########################################

def corner_points(m, cell_num, x, y):
    """

    :param m:
    :param cell_num:
    :param x:
    :param y:
    :return:
    """
    # Your code here
    sq_size = m / cell_num

    top_left = (x, y)
    top_right = (x + sq_size, y)
    bottom_left = (x, y + sq_size)
    bottom_right = (x + sq_size, y + sq_size)

    return [top_left, top_right, bottom_left, bottom_right]


####################################################
####################################################
# Begin procedure for main game loop
####################################################
####################################################

# Define some constants
x_pos = 0  # Player initial x position
y_pos = 0  # Player initial y position
GRID_SIZE = 600  # Pixels x Pixels of console size
SQ_NUM = 10  # Number of squares in grid
SQ_SIZE = int(GRID_SIZE / SQ_NUM)  # Dimension of each square
score = 0
lives = 3

# Boiler plate startup
pygame.init()
DISPLAYSURF = pygame.display.set_mode((GRID_SIZE, GRID_SIZE))
FPS = 60
fpsClock = pygame.time.Clock()
pygame.display.set_caption('Extinction II: Renegade')

# Generate the grid to be used in the game loop
SQ_NUM = 10
grid = generate_grid(0.2, SQ_NUM)

# Define initial enemy locations - set them randomly in the game frame, but avoid cells with barriers
empty_cells = []
for row in range(0, SQ_NUM):
    for col in range(0, SQ_NUM):
        if grid[row][col] == 0:
            empty_cells.append((row, col))

enemy1_start_cell = random.choice(empty_cells)
enemy2_start_cell = random.choice(empty_cells)
enemy1_x = enemy1_start_cell[1] * SQ_SIZE
enemy1_y = enemy1_start_cell[0] * SQ_SIZE
enemy2_x = enemy2_start_cell[1] * SQ_SIZE
enemy2_y = enemy2_start_cell[0] * SQ_SIZE

####################################################
# Planting Treasures
####################################################
show_treasure1 = True
show_treasure2 = True

treasure1_start_cell = random.choice(empty_cells)
treasure2_start_cell = random.choice(empty_cells)

treasure1_x = treasure1_start_cell[1] * SQ_SIZE
treasure1_y = treasure1_start_cell[0] * SQ_SIZE
treasure2_x = treasure2_start_cell[1] * SQ_SIZE
treasure2_y = treasure2_start_cell[0] * SQ_SIZE

grid[treasure1_start_cell[0]][treasure1_start_cell[1]] = 2
grid[treasure2_start_cell[0]][treasure2_start_cell[1]] = 2

treasure_im = pygame.image.load("t.png")
treasure_im = pygame.transform.scale(treasure_im, (SQ_SIZE, SQ_SIZE))

####################################################
# Picking up Treasures
####################################################

font = pygame.font.Font('freesansbold.ttf', 16)
score_text = "Score: " + str(score)
text = font.render(score_text, True, (25, 25, 25), (100, 100, 100))
textRect = text.get_rect()
textRect.center = (300, 9)


####################################################
# Player Enemy Collision
####################################################
def collided(player_x, player_y, enemy_x, enemy_y):
    """

    :param player_x:
    :param player_y:
    :param enemy_x:
    :param enemy_y:
    :return:
    """
    # Get all sides of player
    pl = player_x
    pr = player_x + SQ_SIZE
    pt = player_y
    pb = player_y + SQ_SIZE

    # Get all sides of enemy
    el = enemy_x
    er = enemy_x + SQ_SIZE
    et = enemy_y
    eb = enemy_y + SQ_SIZE

    # Return if any of the sides of the player are between the sides the enemy
    # in BOTH axes x and y. X and y axes are separated by the 'and'.
    return ((((pl > el) and (pl < er)) or ((pr > el) and (pr < er)))
            and
            (((pt > et) and (pt < eb)) or ((pb > et) and (pb < eb))))


####################################################
# Load game assets from same directory.
####################################################
player_im = pygame.image.load("p.png")
player_im = pygame.transform.scale(player_im, (SQ_SIZE, SQ_SIZE))
enemy_im = pygame.image.load("e.png")
enemy_im = pygame.transform.scale(enemy_im, (SQ_SIZE, SQ_SIZE))
barrier_im = pygame.image.load("b.png")
barrier_im = pygame.transform.scale(barrier_im, (SQ_SIZE, SQ_SIZE))

# Main game loop
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Fill the surface background with the RGB color
        DISPLAYSURF.fill((204, 255, 153))

        # Draw the barriers based on values in the grid list
        # created before the game loop
        draw_barrier(grid, 60, SQ_NUM, DISPLAYSURF, barrier_im)

        # Check to see if a button has been pressed.
        # If an arrow key has been pressed, call the move() function and determine new x and y coordinates.

        # During the game press 'H' key to view coordinate info
        # Useful for debugging purposes
        if event.type == pygame.KEYDOWN:
            x_pos, y_pos = move(x_pos, y_pos, 5, grid, GRID_SIZE, SQ_NUM)
            if event.key == pygame.K_h:
                print(x_pos)
                print(y_pos)
                print(enemy1_x)
                print(enemy1_y)
                print(collided(x_pos, y_pos, enemy1_x, enemy1_y))
                print(enemy2_x)
                print(enemy2_y)
                print(collided(x_pos, y_pos, enemy2_x, enemy2_y))

        # Get new coordinates the enemies will move to
        enemy1_x, enemy1_y = enemy_move(enemy1_x, enemy1_y, x_pos, y_pos, 1, grid, GRID_SIZE, SQ_NUM)
        enemy2_x, enemy2_y = enemy_move(enemy2_x, enemy2_y, x_pos, y_pos, 1, grid, GRID_SIZE, SQ_NUM)

        # Draw player and both enemy images to the screen using the blit() function
        DISPLAYSURF.blit(player_im, (x_pos, y_pos))
        DISPLAYSURF.blit(enemy_im, (enemy1_x, enemy1_y))
        DISPLAYSURF.blit(enemy_im, (enemy2_x, enemy2_y))

        if (get_cell(GRID_SIZE, SQ_NUM, x_pos, y_pos) == get_cell(GRID_SIZE, SQ_NUM, treasure1_x,
                                                                  treasure1_y)) and show_treasure1:
            # When food is gotten, remove it from grid and set boolean to false
            # and increase score
            show_treasure1 = False
            grid[treasure1_start_cell[0]][treasure1_start_cell[1]] = 0
            score += 50
        if (get_cell(GRID_SIZE, SQ_NUM, x_pos, y_pos) == get_cell(GRID_SIZE, SQ_NUM, treasure2_x,
                                                                  treasure2_y)) and show_treasure2:
            show_treasure2 = False
            grid[treasure2_start_cell[0]][treasure2_start_cell[1]] = 0
            score += 50

        # Treasure draw
        if (show_treasure1):
            DISPLAYSURF.blit(treasure_im, (treasure1_x, treasure1_y))
        if (show_treasure2):
            DISPLAYSURF.blit(treasure_im, (treasure2_x, treasure2_y))

        # Lives Update
        if (collided(x_pos, y_pos, enemy1_x, enemy1_y)) or (collided(x_pos, y_pos, enemy2_x, enemy2_y)):
            lives -= 1
            # Reset player position if s/he loses a life
            x_pos = 0
            y_pos = 0

        # Text Draw
        score_text = "Score: " + str(score) + " Lives: " + str(lives)
        text = font.render(score_text, True, (25, 25, 25), (100, 100, 100))
        DISPLAYSURF.blit(text, textRect)

        # Reset logic for treasure capture and zero lives
        if (((not show_treasure1) and (not show_treasure2)) or (lives <= 0)):
            grid = generate_grid(0.2, SQ_NUM)

            # Reset score only if 0 lives
            if (lives <= 0):
                score = 0

            lives = 3

            # Define initial enemy locations - set them randomly in the game frame, but avoid cells with barriers
            empty_cells = []
            for row in range(0, SQ_NUM):
                for col in range(0, SQ_NUM):
                    if grid[row][col] == 0:
                        empty_cells.append((row, col))

            # Reset enemy positions
            enemy1_start_cell = random.choice(empty_cells)
            enemy2_start_cell = random.choice(empty_cells)
            enemy1_x = enemy1_start_cell[1] * SQ_SIZE
            enemy1_y = enemy1_start_cell[0] * SQ_SIZE
            enemy2_x = enemy2_start_cell[1] * SQ_SIZE
            enemy2_y = enemy2_start_cell[0] * SQ_SIZE

            ####################################################
            # Reset Planting Treasures
            ####################################################
            show_treasure1 = True
            show_treasure2 = True

            treasure1_start_cell = random.choice(empty_cells)
            treasure2_start_cell = random.choice(empty_cells)

            treasure1_x = treasure1_start_cell[1] * SQ_SIZE
            treasure1_y = treasure1_start_cell[0] * SQ_SIZE
            treasure2_x = treasure2_start_cell[1] * SQ_SIZE
            treasure2_y = treasure2_start_cell[0] * SQ_SIZE

            grid[treasure1_start_cell[0]][treasure1_start_cell[1]] = 2
            grid[treasure2_start_cell[0]][treasure2_start_cell[1]] = 2

            # reset player position
            x_pos = 0
            y_pos = 0

    # Advance the game counter
    pygame.display.update()
    fpsClock.tick(FPS)
