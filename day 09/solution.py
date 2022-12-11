from dataclasses import dataclass


def q1():
    with open('day 09\input.txt', 'r') as f:
        input = f.read().splitlines()

    visited = set()

    head = [0, 0]
    tail = [0, 0]
    visited.add(tuple(tail))

    for l in input:
        direction, amount = l.split()
        amount = int(amount)

        for _ in range(amount):
            old_head = head.copy()
            match direction:
                case 'R':
                    head[0] += 1
                case 'L':
                    head[0] -= 1
                case 'U':
                    head[1] += 1
                case 'D':
                    head[1] -= 1

            if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
                tail = old_head

            visited.add(tuple(tail))

    return len(visited)


def q2():
    with open('day 09\input.txt', 'r') as f:
        input = f.read().splitlines()

    visited = set()
    visited.add(0)
    rope = [0]*10

    for line in input:
        direction, amount = line.split()
        amount = int(amount)
        for _ in range(int(amount)):
            for i in range(10):
                if i == 0:
                    match direction:
                        case 'R':
                            rope[i] += 1
                        case 'L':
                            rope[i] -= 1
                        case 'U':
                            rope[i] += 1j
                        case 'D':
                            rope[i] -= 1j

                    continue

                distance = rope[i-1] - rope[i]
                if abs(distance) >= 2:
                    rope[i] += complex((distance.real > 0) - (distance.real < 0),
                                       (distance.imag > 0) - (distance.imag < 0))

            visited.add(rope[-1])

    return len(visited)


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
