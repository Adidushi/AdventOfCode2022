def split(sequence, sep):
    chunk = []
    for val in sequence:
        if val == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(int(val))
    yield chunk


def q1():
    with open('day 01\input.txt', 'r') as f:
        input = f.read().splitlines()
    calories_per_elf = [sum(elf) for elf in split(input, '')]
    return max(calories_per_elf)


def q2():
    with open('day 01\input.txt', 'r') as f:
        input = f.read().splitlines()
    calories_per_elf = [sum(elf) for elf in split(input, '')]
    return sum(sorted(calories_per_elf[:3], reverse=True))


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
