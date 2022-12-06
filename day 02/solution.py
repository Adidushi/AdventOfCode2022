

def q1():
    with open('day 02\input.txt', 'r') as f:
        input = f.read().splitlines()

    decision_tree = {
        'A': {
            'X': 1+3,
            'Y': 2+6,
            'Z': 0+3
        },
        'B': {
            'X': 1+0,
            'Y': 2+3,
            'Z': 3+6
        },
        'C': {
            'X': 1+6,
            'Y': 2+0,
            'Z': 3+3
        }
    }

    return sum(decision_tree[g.split()[0]][g.split()[1]] for g in input)


def q2():
    with open('day 02\input.txt', 'r') as f:
        input = f.read().splitlines()

    decision_tree = {
        'Z': {
            'A': 2+6,
            'B': 3+6,
            'C': 1+6
        },
        'Y': {
            'A': 1+3,
            'B': 2+3,
            'C': 3+3
        },
        'X': {
            'A': 3,
            'B': 1,
            'C': 2
        }
    }

    return sum(decision_tree[g.split()[1]][g.split()[0]] for g in input)


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
