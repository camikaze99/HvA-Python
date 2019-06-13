#/usr/bin/env python3
# (c) 2019 Camille Molenaar IC102
# Character Maze
def read():
    # Opens the text file containing the maze
    f = open("maze.txt", "r")

    # Properties
    width = 0
    height = 0
    finish = (0, 0)
    tiles = []

    # Keeps track of x and y coordinates
    x = 0
    y = 0

    # Goes over all characters in every line
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

#            print("x:{} y:{} {}".format(x, y, char))
            # The following conditions hold true if we are at the border of the maze.
            if (y == 0 and char == "-") or ((x == 1 or x == width) and char == '-'):
                finish = (x, y)
#                print("Finish found: {}".format(finish))

    return (width, height, finish, tiles)

def solve(x, y):
    center = (5, 6)
    mazetuple = read()
    finish = mazetuple[2]
    Soln = [center, finish]
    for char in line:
        if (x == 5 and y == 6)
        print("Maze solved")

    print(Soln)


read()
solve()
#print(read())
