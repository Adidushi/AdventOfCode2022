def includes(s1, s2):
    return set(s1).issubset(set(s2)) or set(s2).issubset(set(s1))


def overlaps(s1, s2):
    return bool(set(s1) & set(s2))


def q1():
    with open('day 04\input.txt', 'r') as f:
        input = f.read().splitlines()

    counter = 0

    for line in input:
        first_range, second_range = line.split(',')
        l1 = map(int, first_range.split('-'))
        l1 = range(next(l1), next(l1)+1)

        l2 = map(int, second_range.split('-'))
        l2 = range(next(l2), next(l2)+1)

        if includes(l1, l2):
            counter += 1

    return counter


def q2():
    with open('day 04\input.txt', 'r') as f:
        input = f.read().splitlines()

    counter = 0

    for line in input:
        first_range, second_range = line.split(',')
        l1 = map(int, first_range.split('-'))
        l1 = range(next(l1), next(l1)+1)

        l2 = map(int, second_range.split('-'))
        l2 = range(next(l2), next(l2)+1)

        if overlaps(l1, l2):
            counter += 1

    return counter


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
