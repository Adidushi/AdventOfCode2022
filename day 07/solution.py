from dataclasses import dataclass, field


DISK_SIZE = 70000000
REQUIRED_SIZE = 30000000


@dataclass
class Directory:
    name: str
    subdirectories: dict = field(default_factory=dict)
    size: int = 0
    parent: 'Directory' = None

    def get_size(self):
        child_sizes = [subdir.get_size()
                       for subdir in self.subdirectories.values()]
        return self.size + sum(child_sizes)

    def get_size_list(self, sizes):
        sizes.append(self.get_size())
        for child in self.subdirectories.values():
            child.get_size_list(sizes)
        return sizes


def parse_input(input: list[str]):
    current_path = '/'
    root_dir = Directory(current_path)
    current_dir = root_dir
    for output_line in input:
        if output_line == '$ cd ..':
            current_path = '/'.join(current_path.split('/')[:-1])
            current_dir = current_dir.parent
        elif output_line.startswith('$ cd'):
            current_path = f'{current_path.rstrip("/")}/{output_line[5:]}'
            current_dir = current_dir.subdirectories[output_line[5:]]
        elif output_line == '$ ls':
            continue
        elif output_line.startswith('dir'):
            new_dir_name = output_line[4:]
            new_dir = Directory(name=new_dir_name, parent=current_dir)
            current_dir.subdirectories[new_dir_name] = new_dir
        elif output_line[0].isdigit():
            size, name = output_line.split()
            current_dir.size += int(size)

    return root_dir


def q1():
    with open('day 07\input.txt', 'r') as f:
        input = f.read().splitlines()
    root_dir = parse_input(input[1:])
    size_list = root_dir.get_size_list([])
    return sum([_ for _ in size_list if _ < 100000])


def q2():
    with open('day 07\input.txt', 'r') as f:
        input = f.read().splitlines()
    root_dir = parse_input(input[1:])
    size_list = root_dir.get_size_list([])

    available_size = DISK_SIZE - root_dir.get_size()
    delete_needed = REQUIRED_SIZE - available_size
    smallest_possible = [_ for _ in size_list if _ > delete_needed]
    return min(smallest_possible)


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
