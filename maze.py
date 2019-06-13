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

# Creates a "matrix" and sets the x and y (width, height) values to False so they are marked as unvisited
# These coordinates and attached Boolean will be used in the function solve()
def createMatrix(width, height):
    matrix = []
    for i in range(width):
        matrix.append([])
        for j in range(height):
            matrix[i].append(False)
    return matrix

# Calculates what the coordinates are from the center of the maze
def getValidCenter(meta_tuple):
    width, height, finish, tiles = meta_tuple
    x = width / 2 + 1
    y = height / 2 + 1
    return int(x), int(y)

def solve(meta_tuple, visited, position, path):
    # Instead of having to use meta_tuple[0-2]
    width, height, finish, tiles = meta_tuple
    # If the finish is reached print the path and add/append the coordinates of the finish
    if position == finish:
        path.append(finish)
        print(path)
        return True

    # Current coordinates
    x, y = position

    # Add current position to path and mark it as visited
    path.append(position)
    visited[x][y] = True

    solved = False

    # Check all directions (up, down, left, right) and marks the visited coordinates as True
    # Right
    if (x+1, y) in tiles and not visited[x+1][y]:
        visited[x+1][y] = True
        position = (x+1, y)
        solved = solve(meta_tuple, visited, position, path)
    # Up
    if (x, y-1) in tiles and not visited[x][y-1]:
        visited[x][y-1] = True
        position = (x, y-1)
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

    # Remove the visited position from the path
    if not solved:
        del path[-1]

    return solved

meta_tuple = read()
# Instead of having to use meta_tuple[0-2]
width, height, finish, tiles = meta_tuple
visited = createMatrix(width, height)
center = getValidCenter(meta_tuple)
#print("Start:", center)
#print("Finish", finish)
solve(meta_tuple, visited, center, [])
