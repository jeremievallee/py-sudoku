import examples


grid = examples.sudoku_2


def showGrid(grid):
    return_string = "--------------------------------\n"
    for line in range(0, 9):
        for column in range(0, 9):
            return_string += "{}  ".format(grid[line][column])
            if not (column + 1) % 3:
                return_string += "| "
        return_string += "\n"
        if not (line + 1) % 3:
            return_string += "--------------------------------\n"
    return return_string


def isValueOnLine(grid, value, line_number):
    if value in grid[line_number]:
        return True
    else:
        return False


def isValueOnColumn(grid, value, column_number):
    for line in grid:
        if line[column_number] == value:
            return True
    return False


def isValueOnSubGrid(grid, value, line_number, column_number):
    _line = line_number - (line_number % 3)
    _colu = column_number - (column_number % 3)
    for k in range(_line, _line + 3):
        for l in range(_colu, _colu + 3):
            if grid[k][l] == value:
                return True
    return False


def isGridValid(grid, position):
    if position == 81:
        return True
    line_number = position / 9
    column_number = position % 9
    if grid[line_number][column_number] != 0:
        return isGridValid(grid, position + 1)
    for i in range(1, 10):
        if not isValueOnLine(
            grid,
            i,
            line_number
        ) and not isValueOnColumn(
            grid,
            i,
            column_number
        ) and not isValueOnSubGrid(
            grid,
            i,
            line_number,
            column_number
        ):
            grid[line_number][column_number] = i
            if isGridValid(grid, position + 1):
                return True
    grid[line_number][column_number] = 0
    return False


print showGrid(grid)
isGridValid(grid, 0)
print showGrid(grid)
