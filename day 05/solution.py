def parse_line(line):
    # returns amount, from, to
    _, amount, _, origin, _, dest = line.split()
    return int(amount), int(origin) - 1, int(dest) - 1


global_stacks = [
    ['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q'],
    ['W', 'D', 'B', 'G'],
    ['F', 'W', 'R', 'T', 'S', 'Q', 'B'],
    ['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N'],
    ['M', 'P', 'D', 'V', 'F'],
    ['F', 'W', 'J'],
    ['L', 'N', 'Q', 'B', 'J', 'V'],
    ['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N'],
    ['J', 'S', 'Q', 'C', 'W', 'D', 'M']
]


def q1():
    with open('day 05\input.txt', 'r') as f:
        input = f.read().splitlines()

    stacks = [_.copy() for _ in global_stacks]

    for line in input:
        amount, origin, dest = parse_line(line)
        for _ in range(amount):
            stacks[dest].append(stacks[origin].pop())

    return ''.join([stack[-1] for stack in stacks])


def q2():
    with open('day 05\input.txt', 'r') as f:
        input = f.read().splitlines()

    stacks = global_stacks

    for line in input:
        amount, origin, dest = parse_line(line)
        stacks[dest].extend(stacks[origin][-amount:])
        del stacks[origin][-amount:]

    return ''.join([stack[-1] for stack in stacks])


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
