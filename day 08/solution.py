import math


def parse(input):
    tree_lines = list()

    for line in input.splitlines():
        tree_lines.append(list(map(int, line)))

    tree_cols = [_ for _ in zip(*tree_lines)]

    return tree_lines, tree_cols


def flip_index(iter, index):
    return len(iter) - index - 1


def count_scenic_in_direction(l, height):
    count = 0

    for h in iter(l):
        if h < height:
            count += 1
        else:
            return count+1
    return count


def get_scenic_score(tree_lines, tree_cols, row, col):
    height = tree_lines[row][col]
    tree_lists = list()

    tree_lists.append(tree_lines[row][:col][::-1])
    tree_lists.append(tree_lines[row][col+1:])
    tree_lists.append(tree_cols[col][:row][::-1])
    tree_lists.append(tree_cols[col][row+1:])

    return math.prod([count_scenic_in_direction(l, height) for l in tree_lists])


def q1():
    with open('day 08\input.txt', 'r') as f:
        input = f.read()

    tree_lines, tree_cols = parse(input)

    visible_trees = set()

    for row, line in enumerate(tree_lines):
        biggest = -1
        for col, tree in enumerate(line):
            if tree > biggest:
                visible_trees.add((col, row))
                biggest = tree

    for row, line in enumerate(tree_lines):
        biggest = -1
        for col, tree in enumerate(line[::-1]):
            if tree > biggest:
                visible_trees.add((flip_index(line, col), row))
                biggest = tree

    for col, line in enumerate(tree_cols):
        biggest = -1
        for row, tree in enumerate(line):
            if tree > biggest:
                visible_trees.add((col, row))
                biggest = tree

    for col, line in enumerate(tree_cols):
        biggest = -1
        for row, tree in enumerate(line[::-1]):
            if tree > biggest:
                visible_trees.add((col, flip_index(line, row)))
                biggest = tree

    return len(visible_trees)


def q2():
    with open('day 08\input.txt', 'r') as f:
        input = f.read()

    tree_lines, tree_cols = parse(input)

    most_scenic = -1

    for row, line in enumerate(tree_lines):
        for col, tree in enumerate(line):
            most_scenic = max(most_scenic, get_scenic_score(
                tree_lines, tree_cols, row, col))

    return most_scenic


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
