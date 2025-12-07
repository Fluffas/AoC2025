import sys
import copy

with open(sys.argv[1]) as f:
    grid = [list(line.strip()) for line in f.readlines()]
    previous_grid = []

    total = 0

    while grid != previous_grid:
        previous_grid = copy.deepcopy(grid)
        new_grid = copy.deepcopy(grid)

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                surrounding = 0
                if grid[y][x] == "@":
                    # Check surrounding cells
                    # Top left
                    if x > 0 and y > 0:
                        if grid[y-1][x-1] == "@":
                            surrounding += 1
                    # Top
                    if y > 0:
                        if grid[y-1][x] == "@":
                            surrounding += 1
                    # Top right
                    if x < len(grid[y])-1 and y > 0:
                        if grid[y-1][x+1] == "@":
                            surrounding += 1
                    # Left
                    if x > 0:
                        if grid[y][x-1] == "@":
                            surrounding += 1
                    # Right
                    if x < len(grid[y])-1:
                        if grid[y][x+1] == "@":
                            surrounding += 1
                    # Bottom left
                    if x > 0 and y < len(grid)-1:
                        if grid[y+1][x-1] == "@":
                            surrounding += 1
                    # Bottom
                    if y < len(grid)-1:     
                        if grid[y+1][x] == "@":
                            surrounding += 1
                    # Bottom right
                    if x < len(grid[y])-1 and y < len(grid)-1:
                        if grid[y+1][x+1] == "@":
                            surrounding += 1 
                
                    if surrounding < 4:
                        new_grid[y][x] = "."
                        total += 1

        grid = copy.deepcopy(new_grid)

    for line in grid:
        print("".join(line))
    print(total)