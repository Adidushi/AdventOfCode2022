def halve_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def triwise(iterable):
    for i in range(0, len(iterable), 3):
        yield iterable[i:i+3]


def priority(character):
    val = ord(character)
    return val - 38 if val < 97 else val - 96


def common_2(lower, upper):
    return next(iter(set(lower) & set(upper)))


def common_3(a, b, c):
    return next(iter(set(a) & set(b) & set(c)))


def q1():
    with open('day 03\input.txt', 'r') as f:
        input = f.read().splitlines()
    return sum(priority(common_2(*halve_list(sack))) for sack in input)


def q2():
    with open('day 03\input.txt', 'r') as f:
        input = f.read().splitlines()
    return sum(priority(common_3(*triplet)) for triplet in triwise(input))


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
