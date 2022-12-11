from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    items: list[int]
    operation: Callable
    test_div: int
    next_monkey: dict
    inspected: int = 0


monkeys: list[Monkey] = [Monkey([78, 53, 89, 51, 52, 59, 58, 85], lambda old: old * 3, 5, {True: 2, False: 7}),
                         Monkey([64], lambda old: old + 7,
                                2, {True: 3, False: 6}),
                         Monkey([71, 93, 65, 82], lambda old: old +
                                5, 13, {True: 5, False: 4}),
                         Monkey([67, 73, 95, 75, 56, 74], lambda old: old +
                                8, 19, {True: 6, False: 0}),
                         Monkey([85, 91, 90], lambda old: old +
                                4, 11, {True: 3, False: 1}),
                         Monkey([67, 96, 69, 55, 70, 83, 62],
                                lambda old: old * 2, 3, {True: 4, False: 1}),
                         Monkey([53, 86, 98, 70, 64], lambda old: old +
                                6, 7, {True: 7, False: 0}),
                         Monkey([88, 64], lambda old: old * old, 17, {True: 2, False: 5})]


#test_monkeys: list[Monkey] = [Monkey([79, 98], lambda old: old * 19, 23, {True: 2, False: 3}),
#                         Monkey([54, 65, 75, 74], lambda old: old +
#                                6, 19, {True: 2, False: 0}),
#                         Monkey([79, 60, 97], lambda old: old *
#                                old, 13, {True: 1, False: 3}),
#                         Monkey([74], lambda old: old + 3, 17, {True: 0, False: 1})]


def q1():
    for _ in range(20):
        for monkey in monkeys:
            new_worry_values = list(map(lambda x: monkey.operation(x)//3, monkey.items))
            monkey.inspected += len(new_worry_values)
            for item in new_worry_values:
                monkeys[monkey.next_monkey[item %
                                           monkey.test_div == 0]].items.append(item)
            monkey.items = list()

    sorted_monkeys = sorted([monkey.inspected for monkey in monkeys])
    print(sorted_monkeys)
    return sorted_monkeys[-1]*sorted_monkeys[-2]

monkeys: list[Monkey] = [Monkey([78, 53, 89, 51, 52, 59, 58, 85], lambda old: old * 3, 5, {True: 2, False: 7}),
                         Monkey([64], lambda old: old + 7,
                                2, {True: 3, False: 6}),
                         Monkey([71, 93, 65, 82], lambda old: old +
                                5, 13, {True: 5, False: 4}),
                         Monkey([67, 73, 95, 75, 56, 74], lambda old: old +
                                8, 19, {True: 6, False: 0}),
                         Monkey([85, 91, 90], lambda old: old +
                                4, 11, {True: 3, False: 1}),
                         Monkey([67, 96, 69, 55, 70, 83, 62],
                                lambda old: old * 2, 3, {True: 4, False: 1}),
                         Monkey([53, 86, 98, 70, 64], lambda old: old +
                                6, 7, {True: 7, False: 0}),
                         Monkey([88, 64], lambda old: old * old, 17, {True: 2, False: 5})]

def q2():
    for _ in range(10000):
        for monkey in monkeys:
            monkey.inspected += len(monkey.items)
            new_worry_values = list(map(lambda x: monkey.operation(x), monkey.items))
            for item in new_worry_values:
                monkeys[monkey.next_monkey[item %
                                           monkey.test_div == 0]].items.append(item)
            monkey.items = list()

    sorted_monkeys = sorted([monkey.inspected for monkey in monkeys], reverse=True)
    print(sorted_monkeys)
    return sorted_monkeys[0]*sorted_monkeys[-1]


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
