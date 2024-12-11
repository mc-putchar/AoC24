def read(input):
    with open(input, 'r') as f:
        lines = [l.strip() for l in f]
    return lines

def interpret(seq):
    res = []
    id = 0
    for c in seq:
        res += (int(c) * [-1]) if id & 1 else (int(c) * [id // 2])
        id += 1
    return res

def defrag(disk):
    p1 = 0
    p2 = len(disk) - 1
    while p1 < p2:
        while disk[p2] < 0:
            p2 -= 1
        if p2 <= p1:
            break
        if disk[p1] < 0:
            disk[p1], disk[p2] = disk[p2], disk[p1]
            p2 -= 1
        p1 += 1

def find_space(disk, size, limit):
    free_size = 0
    for i in range(limit):
        if disk[i] >= 0:
            free_size = 0
            continue
        free_size += 1
        if free_size >= size:
            return i + 1 - free_size
    return -1

def defrag_file_preserve(disk):
    max_id = disk[-1]
    for id in range(max_id, 0, -1):
        size = 0
        for i in range(len(disk) - 1, -1, -1):
            if disk[i] != id:
                if size > 0:
                    dest = find_space(disk, size, i + 1)
                    if dest >= 0:
                        for b in range(size):
                            disk[i + 1 + b], disk[dest + b] = disk[dest + b], disk[i + 1 + b]
                    break
                continue
            size += 1

def calc_checksum(disk):
    checksum = 0
    pos = 0
    for b in disk:
        pos += 1
        if b < 0:
            continue
        checksum += (pos - 1) * b
    return checksum

def main(input):
    disk = list(interpret(input[0]))
    dummy = disk.copy()
    defrag(dummy)
    print(calc_checksum(dummy))
    defrag_file_preserve(disk)
    #print(''.join(['.' if n < 0 else str(n) for n in disk]))
    print(calc_checksum(disk))

import sys
if __name__ == "__main__":
    input = "example" if len(sys.argv) > 1 else "input"
    main(read(input))
