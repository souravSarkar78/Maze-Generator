import pygame
import time
import random

# initialize pygame

grid_size = int(input('Enter the size of grid: '))

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

hw = int(200/grid_size) #height and width of solution path box |||  

offset = int(hw/2)  #offset for draw solution in grid

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (255, 45, 154)
BLUE = (120, 20, 255)
YELLOW = (200, 200, 0)
w = int(600/grid_size)
lineWidth = 2
grid = []
visited = []
stack = []
solution = {}
sol_delay = 0.00
stack_delay = 0.00
maze_delay = 0.00

screen.fill(BLACK)  # Clearing the Screen


# Drawing Grid Lines
def draw_grid(x, y, w):
    for i in range(grid_size):
        x = w
        y = y + w
        for j in range (grid_size):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])  # Top line
            pygame.draw.line(screen, WHITE, [x, y], [x, y + w])  # left line
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])  # right line
            pygame.draw.line(screen, WHITE, [x, y + w], [x + w, y + w])  # bottom line
            grid.append((x, y))
            x = x + w
        





x = w
y = w


def go_up(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y-w+1,  w-1, (w*2)-1), 0)
    pygame.display.update()


def go_down(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y+1,  w-1, (w*2)-1), 0)
    pygame.display.update()


def go_right(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y+1, (w*2)-1, w-1), 0)
    pygame.display.update()


def go_left(x, y):
    pygame.draw.rect(screen, BLUE, (x-w+1, y +1,   (w*2)-1, w-1), 0)
    pygame.display.update()


def single_cell(x, y):
    pygame.draw.rect(screen, GREEN, (x + 1, y + 1, w - 1, w - 1), 0)
    pygame.display.update()


def backtrack_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, w - 1, w - 1), 0)
    pygame.display.update()


def solution_cell(x, y):
    pygame.draw.rect(screen, YELLOW, (x + int(w/2)-offset, y + int(w/2)-offset, hw,  hw), 0)
    pygame.display.update()


def draw_maze(x, y):
    single_cell(x, y)
    visited.append((x, y))
    stack.append((x, y))

    while len(stack) > 0:
        print(x, y)
        pygame.event.pump()
        cell = []

        if (x+w, y) not in visited and (x+w, y) in grid:
            cell.append('right')
        if (x-w, y) not in visited and (x-w, y) in grid:
            cell.append('left')
        if (x, y-w) not in visited and (x, y-w) in grid:
            cell.append('up')
        if (x, y+w) not in visited and (x, y+w) in grid:
            cell.append('down')

        if len(cell)>0:
            cell_choosen = random.choice(cell)

            if cell_choosen == 'up':
                go_up(x, y)
                solution[(x, y-w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
            elif cell_choosen == 'down':
                go_down(x, y)
                solution[(x, y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))
            elif cell_choosen == 'left':
                go_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))
            elif cell_choosen == 'right':
                go_right(x, y)
                solution[(x + w, y)] = x, y
                x = x + w
                visited.append((x, y))
                stack.append((x, y))

        else:
            x, y = stack.pop()
            single_cell(x, y)
            time.sleep(stack_delay)
            backtrack_cell(x, y)


def draw_solution(x, y):
    solution_cell(x,y)
    while (x, y) != (w, w):
        x, y = solution[x, y]
        #print(x, y)
        solution_cell(x, y)


draw_grid(0, 0, w)
draw_maze(w, w)
draw_solution(w*grid_size, w*grid_size)

pygame.display.flip()

# Game Loop
running = True
s = 0

name = str(grid_size) + "-size" + str(time.time()) + '.jpg'

while running:

    if s == 0:
        pygame.image.save(screen, name)
        s += 1
    clock.tick(30)
    # Quit Condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()

