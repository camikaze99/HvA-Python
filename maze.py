#/usr/bin/env python3
# (c) 2019 Camille Molenaar IC102
# Character Maze
import sys
def read():
    # Opens the text file containing the maze
    f = open(sys.argv[1], "r")

    # Properties
    width = 0
    height = 0
    finish = (0, 0)
    tiles = []

    # Keeps track of x and y coordinates
    x = 0
    y = 0

    # Goes over every character in every line
    for line in f:
        x = 0
        y += 1

        height += 1
        width = len(line)

        for char in line:
            x+= 1

            # Floor tiles, walls are irrelevant
            if char == '-':
                tiles.append((x, y))
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

def getValidCenter(meta_tuple):
    width, height, finish, tiles = meta_tuple
    x = width / 2
    y = height / 2

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

def solve(meta_tuple, visited, position, path):
    # Finish is reached
    if position == meta_tuple[2]:
        print(path)
        return True

    tiles = meta_tuple[3]

    # Current coordinates
    x, y = position

    # Add current position to path and mark it as visited
    path.append(position)
    visited[x][y] = True

    solved = False

    # Check all directions (up, down, left, right)
    # Right
    if (x+1, y) in tiles and not visited[x+1][y]:
        visited[x+1][y] = True
        position = (x+1, y)
        solved = solve(meta_tuple, visited, position, path)
    # Left
    if (x-1, y) in tiles and not visited[x-1][y]:
        visited[x-1][y] = True
        position = (x-1, y)
        solved = solve(meta_tuple, visited, position, path)
    # Down
    if (x, y+1) in tiles and not visited[x][y+1]:
        visited[x][y+1] = True
        position = (x, y+1)
        solved = solve(meta_tuple, visited, position, path)
    # Up
    if (x, y-1) in tiles and not visited[x][y-1]:
        visited[x][y-1] = True
        position = (x, y-1)
        solved = solve(meta_tuple, visited, position, path)

    # Remove the visited position from the path
    if not solved:
        del path[-1]

    return solved


solve(meta_tuple, visited, center, [])
