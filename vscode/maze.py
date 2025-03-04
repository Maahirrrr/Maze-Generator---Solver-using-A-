import random
import pygame
import heapq

# Maze dimensions (Can be adjusted for different sizes)
WIDTH, HEIGHT = 51, 51  # Must be odd for proper maze generation
CELL_SIZE = 15  # Size of each cell in pixels
SCREEN_SIZE = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)

# Colors for visualization
WHITE = (255, 255, 255)  # Open paths
BLACK = (0, 0, 0)  # Walls
GREEN = (0, 255, 0)  # Start point
RED = (255, 0, 0)  # End point
BLUE = (0, 0, 255)  # Final path found by A*
YELLOW = (255, 255, 0)  # Explored nodes during search

# Possible movement directions (right, left, down, up)
MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Maze Solver")

# Initialize the maze as a grid full of walls
maze = [[1] * WIDTH for _ in range(HEIGHT)]

def generate_maze(x, y):
    """Recursive Backtracking Algorithm to generate a perfect maze."""
    maze[y][x] = 0  # Mark current cell as a passage
    random.shuffle(MOVES)  # Shuffle move directions for randomness

    for dx, dy in MOVES:
        nx, ny = x + dx * 2, y + dy * 2  # Move two steps ahead
        if 1 <= nx < WIDTH - 1 and 1 <= ny < HEIGHT - 1 and maze[ny][nx] == 1:
            maze[y + dy][x + dx] = 0  # Remove wall between cells
            generate_maze(nx, ny)  # Recursively generate the maze

# Start maze generation from (1,1)
generate_maze(1, 1)

def draw_maze(explored=set(), path=None):
    """Draws the maze and visualization of the search algorithm."""
    screen.fill(BLACK)  # Clear the screen
    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = WHITE if maze[y][x] == 0 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, GREEN, (start[0] * CELL_SIZE, start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (end[0] * CELL_SIZE, end[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Highlight explored nodes
    for x, y in explored:
        pygame.draw.rect(screen, YELLOW, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the final path if found
    if path is not None:
        for x, y in path:
            pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def astar(start, end):
    """A* algorithm for shortest pathfinding in the maze."""
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

    open_set = []  # Priority queue for A*
    heapq.heappush(open_set, (0, start))  # Push the starting node with f-score 0
    came_from = {}  # Track path
    g_score = {start: 0}  # Cost from start to current node
    f_score = {start: heuristic(start, end)}  # Estimated total cost to end
    explored_nodes = set()  # Track explored nodes

    while open_set:
        _, current = heapq.heappop(open_set)  # Get node with lowest f-score
        explored_nodes.add(current)  # Mark as explored

        if current == end:  # If goal is reached, reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1], explored_nodes  # Return reversed path

        for dx, dy in MOVES:
            neighbor = (current[0] + dx, current[1] + dy)

            # Check if neighbor is within bounds and is a walkable path
            if 0 <= neighbor[0] < WIDTH and 0 <= neighbor[1] < HEIGHT and maze[neighbor[1]][neighbor[0]] == 0:
                temp_g_score = g_score[current] + 1

                if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current  # Track the path
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))  # Push neighbor with priority

        # Visualize search process
        draw_maze(explored_nodes, None)  # Show explored nodes
        pygame.display.flip()
        pygame.time.delay(13)  # Delay for animation effect

    return None, explored_nodes  # Return if no path found

# Define start and end points
start = (1, 1)
end = (WIDTH - 2, HEIGHT - 2)

# Run A* algorithm to find path
path, explored_nodes = astar(start, end)

# Game loop to display the solved maze
running = True
while running:
    draw_maze(explored_nodes, path)  # Draw maze with final path
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit loop when window is closed

pygame.quit()  # Quit pygame when loop ends
