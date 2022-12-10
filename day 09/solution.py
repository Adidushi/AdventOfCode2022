from copy import deepcopy
from dataclasses import dataclass
from itertools import pairwise


backspace = '\b'


class RopeLink:
    def __init__(self, length):
        self.position = [0, 0]
        self.length = length
        if self.length:
            self.child = RopeLink(self.length-1)
        else:
            self.child = None

    def __str__(self):
        return f'{self.position}-{str(self.child) if self.child else backspace} '

    def move(self, direction, first=False):

        if first:
            new_pos = self.position.copy()

            match direction:
                case 'R':
                    new_pos[0] += 1
                case 'L':
                    new_pos[0] -= 1
                case 'U':
                    new_pos[1] += 1
                case 'D':
                    new_pos[1] -= 1

            if abs(self.child.position[0] - new_pos[0]) > 1 or abs(self.child.position[1] - new_pos[1]) > 1:
                self.child.move(self.position)
            self.position = new_pos

        else:
            if self.child:
                if abs(self.child.position[0] - direction[0]) > 1 or abs(self.child.position[1] - direction[1]) > 1:
                    self.child.move(direction)

            self.position = direction

    def get_final_child(self):

        return self.child.get_final_child() if self.child else self


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


@dataclass
class Pos:
    pos: list
    old_pos: list

    def __getitem__(self, index):
        return self.pos[index]

    def __setitem__(self, index, value):
        self.pos[index] = value


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
                    rope[i] += complex((distance.real > 0) - (distance.real < 0), (distance.imag > 0) - (distance.imag < 0))

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
