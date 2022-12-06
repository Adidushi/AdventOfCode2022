def is_unique(s: str) -> bool:
    return len(set(s)) == len(s)

def q1():
    with open('day 06\input.txt', 'r') as f:
        input = f.read()
    
    counter = 4
    while not is_unique(input[:4]):
        counter += 1
        input = input[1:]

    return counter
    
def q2():
    with open('day 06\input.txt', 'r') as f:
        input = f.read()

    counter = 14
    while not is_unique(input[:14]):
        counter += 1
        input = input[1:]

    return counter

if __name__ == '__main__':
    from time import perf_counter as  pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')