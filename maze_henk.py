def read():
    # Open the maze file.
    f = open("maze.txt", "r")

    # Properties
    width = -1
    height = 0
    finish = (-1, -1)
    tiles = []

    # Keep track of x and y.
    x = 0
    y = 0

    # Go over every character in every line.
    for line in f:
        x = 0
        y += 1

        height += 1
        width = len(line)

        for char in line:
            x+= 1

            # Floor tiles, walls are not relevant
            if char == '-':
                tiles.append((x, y))

            # print("x:{} y:{} {}".format(x, y, char))
            # The following conditions hold true if we are at the border of the maze.
            if (y == 0 and char == "-") or ((x == 1 or x == width) and char == '-'):
                finish = (x, y)

    return width, height, finish, tiles


def createMatrix(width, height):
    matrix = []
    for i in range(width):
        matrix.append([])
        for _ in range(height):
            matrix[i].append(False)
    return matrix

def matrixToPath(matrix):
    tiles_visited = []
    row_number = 0
    for row in matrix:
        # Keep track of column and row. The column is the x the row is the y.
        row_number += 1
        col_number = 0
        for visited_col in row:
            col_number += 1
            if visited_col:
                tiles_visited.append((col_number, row_number))
    return tiles_visited



def getValidCenter(meta_tuple):
    width, height, finish, tiles = meta_tuple
    x = width/2
    y = height/2

    if (round(x), round(y)) in tiles:
        return round(x), round(y)
    if (int(x), int(y)) in tiles:
        return int(x), int(y)
    if (int(x), round(y)) in tiles:
        return int(x), round(y)
    if (round(x), int(y)) in tiles:
        return round(x), int(y)


meta_tuple = read()
visited = createMatrix(meta_tuple[0], meta_tuple[1])
center = getValidCenter(meta_tuple)

print("Start: {} Finish: {}".format(center, meta_tuple[2]))


def solve(meta_tuple, visited, position, path):
    # Base case: we reached the finish. (all mazes are valid, so only this condition is needed)
    if position == meta_tuple[2]:
        print(path)
        return True

    tiles = meta_tuple[3]

    # Get the current position's coordinates
    x, y = position

    # Add current position to the path and mark it visited.
    path.append(position)
    visited[x][y] = True

    solved = False

    # Check all directions: Up, down, left, right
    # Right
    if (x+1, y) in tiles and not visited[x+1][y]:
        visited[x+1][y] = True
        position = (x+1, y)
        solved = solve(meta_tuple, visited, position, path)
    # # Left
    if (x-1, y) in tiles and not visited[x-1][y]:
        visited[x-1][y] = True
        position = (x-1, y)
        solved = solve(meta_tuple, visited, position, path)
    # # Down
    if (x, y+1) in tiles and not visited[x][y+1]:
        visited[x][y+1] = True
        position = (x, y+1)
        solved = solve(meta_tuple, visited, position, path)
    # # Up
    if (x, y-1) in tiles and not visited[x][y-1]:
        visited[x][y-1] = True
        position = (x, y-1)
        solved = solve(meta_tuple, visited, position, path)

    # Nope, nothing here. Remove the visited position from the path.
    if not solved:
        del path[-1]

    return solved


solve(meta_tuple, visited, center, [])
