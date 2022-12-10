
from dataclasses import dataclass, field


@dataclass
class Device:
    cycle: int = 0
    x: int = 1
    signal_strengths: list = field(default_factory=list)
    sprite_positions: list = field(default_factory=lambda: [1, 2, 3])
    screen: str = ''

    def noop(self):
        self.advance_cycle()

    def addx(self, value):
        self.advance_cycle()
        self.advance_cycle()
        self.x += value
        self.sprite_positions = [self.x-1, self.x, self.x+1]

    def advance_cycle(self):
        if self.cycle % 40 in self.sprite_positions:
            self.screen += '█'
        else:
            self.screen += ' '

        self.cycle += 1
        if self.cycle % 40 == 20:
            self.signal_strengths.append(self.cycle*self.x)


def q1():
    with open('day 10\input.txt', 'r') as f:
        input = f.read().splitlines()

    device = Device()

    for command in input:
        if len(device.signal_strengths) == 6:
            return sum(device.signal_strengths)

        if command[:4] == 'noop':
            device.noop()
        else:
            device.addx(int(command.split()[1]))


def q2():
    with open('day 10\input.txt', 'r') as f:
        input = f.read().splitlines()

    device = Device()

    for command in input:
        if command[:4] == 'noop':
            device.noop()
        else:
            device.addx(int(command.split()[1]))
    split_printable = [device.screen[i:i+40]
                       for i in range(0, len(device.screen), 40)]
    return '\n'+'\n'.join(split_printable)


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
