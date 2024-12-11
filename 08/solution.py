def read():
    lines = []
    with open('input', 'r') as f:
        lines = [l.strip() for l in f]
    return lines

def place_antinode(nodes, x, y):
    if x < 0 or x >= len(nodes[0]) or y < 0 or y >= len(nodes):
        return False
    nodes[y][x] = True
    return True

def find_nodes(map, freq, ox, oy, antinodes, harmonics):
    resonances = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == freq and not (x == ox and y == oy):
                resonances.append((x - ox, y - oy))
    for res in resonances:
        nx, ny = ox - res[0], oy - res[1]
        place_antinode(antinodes, nx, ny)
        if harmonics:
            while nx >= 0 and nx < len(map[0]) and ny >= 0 and ny < len(map):
                place_antinode(antinodes, nx, ny)
                nx, ny = nx - res[0], ny - res[1]
    if harmonics:
        place_antinode(antinodes, ox, oy)

def antinodes(map, nodes, freq, harm=False):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == freq:
                find_nodes(map, freq, x, y, nodes, harm)

def main():
    map = read()
    nodes = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
    freqs = list(set(''.join([l for l in map])))
    [antinodes(map, nodes, freq) for freq in freqs if freq.isalnum()]
    print(sum([node.count(True) for node in nodes]))
    [antinodes(map, nodes, freq, harm=True) for freq in freqs if freq.isalnum()]
    print(sum([node.count(True) for node in nodes]))

if __name__ == "__main__":
    main()
