from collections import defaultdict


def find_start_and_end(matrix):
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col] == 'S':
                start_x, start_y = row, col
            if matrix[row][col] == 'E':
                end_x, end_y = row, col

    return start_x, start_y, end_x, end_y


def find_all_starts(matrix, start_value):
    starts = list()
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col] == start_value:
                starts.append((row, col))

    return starts


def q1():
    with open('day 12\input.txt', 'r') as f:
        input = f.read().splitlines()

    moveable_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    letter_grid = [list(line) for line in input]
    width = len(letter_grid)
    height = len(letter_grid[0])

    start_x, start_y, end_x, end_y = find_start_and_end(letter_grid)

    letter_grid[start_x][start_y] = 'a'
    letter_grid[end_x][end_y] = 'z'

    number_grid = [[ord(character) - ord('a')
                    for character in row] for row in letter_grid]

    distances = defaultdict(lambda: 1000000)

    node_queue = list()
    node_queue.append((start_x, start_y))

    for x, y in node_queue:
        distances[x, y] = 0

    while len(node_queue) > 0:
        current_x, current_y = node_queue.pop(0)

        if (current_x, current_y) == (end_x, end_y):
            return distances[end_x, end_y]

        for direction_x, direction_y in moveable_directions:
            next_x, next_y = current_x + direction_x, current_y + direction_y
            if 0 <= next_x < width and 0 <= next_y < height and number_grid[current_x][current_y] >= number_grid[next_x][next_y] - 1:
                next_distance = distances[current_x, current_y] + 1
                if next_distance < distances[next_x, next_y]:
                    node_queue.append((next_x, next_y))
                    distances[next_x, next_y] = next_distance


def q2():
    with open('day 12\input.txt', 'r') as f:
        input = f.read().splitlines()

    moveable_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    letter_grid = [list(line) for line in input]
    width = len(letter_grid)
    height = len(letter_grid[0])

    start_x, start_y, end_x, end_y = find_start_and_end(letter_grid)

    letter_grid[start_x][start_y] = 'a'
    letter_grid[end_x][end_y] = 'z'

    all_starts = find_all_starts(letter_grid, 'a')

    number_grid = [[ord(character) - ord('a')
                    for character in row] for row in letter_grid]

    distances = defaultdict(lambda: 1000000)

    node_queue = list()
    node_queue.extend(all_starts)

    for x, y in node_queue:
        distances[x, y] = 0

    while len(node_queue) > 0:
        current_x, current_y = node_queue.pop(0)

        if (current_x, current_y) == (end_x, end_y):
            return distances[end_x, end_y]

        for direction_x, direction_y in moveable_directions:
            next_x, next_y = current_x + direction_x, current_y + direction_y
            if 0 <= next_x < width and 0 <= next_y < height and number_grid[current_x][current_y] >= number_grid[next_x][next_y] - 1:
                next_distance = distances[current_x, current_y] + 1
                if next_distance < distances[next_x, next_y]:
                    node_queue.append((next_x, next_y))
                    distances[next_x, next_y] = next_distance


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
