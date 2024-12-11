from collections import deque, defaultdict

def read(input):
    with open(input, 'r') as f:
        lines = [l.strip() for l in f]
    return lines

def add_neighbours(map, x, y, node, next, visited, dfs=True):
    added  = 0
    if x > 0 and int(map[y][x - 1]) == node + 1 and not (x - 1, y) in visited:
        next.appendleft((x - 1, y)) if dfs else next.append((x - 1, y))
        added += 1
    if y > 0 and int(map[y - 1][x]) == node + 1 and not (x, y - 1) in visited:
        next.appendleft((x, y - 1)) if dfs else next.append((x, y - 1))
        added += 1
    if x < len(map[0]) - 1 and int(map[y][x + 1]) == node + 1 and not (x + 1, y) in visited:
        next.appendleft((x + 1, y)) if dfs else next.append((x + 1, y))
        added += 1
    if y < len(map) - 1 and int(map[y + 1][x]) == node + 1 and not (x, y + 1) in visited:
        next.appendleft((x, y + 1)) if dfs else next.append((x, y + 1))
        added += 1
    return added

def score_trailhead(map, x, y, trails):
    score = 0
    visited = set()
    que = deque()
    node = int(map[y][x])
    visited.add((x, y))
    add_neighbours(map, x, y, node, que, visited)
    while len(que) > 0:
        next = que.pop()
        if (next[0], next[1]) in visited:
            continue
        visited.add((next[0], next[1]))
        node = int(map[next[1]][next[0]])
        if node == 9:
            score += 1
            trails[(x, y)].append((next[0], next[1]))
            continue
        add_neighbours(map, next[0], next[1], node, que, visited)
    return score

def count_ways(map, target, node, x, y):
    ways = 0
    if x == target[0] and y == target[1]:
        return 1
    if x < len(map[0]) - 1 and int(map[y][x + 1]) == node - 1:
        ways += count_ways(map, target, node - 1, x + 1, y)
    if y < len(map) - 1 and int(map[y + 1][x]) == node - 1:
        ways += count_ways(map, target, node - 1, x, y + 1)
    if x > 0 and int(map[y][x - 1]) == node - 1:
        ways += count_ways(map, target, node - 1, x - 1, y)
    if y > 0 and int(map[y - 1][x]) == node - 1:
        ways += count_ways(map, target, node - 1, x, y - 1)
    return ways

def rate_trailhead(map, trailhead, trails):
    rating = 0
    for trail in trails:
        rating += count_ways(map, trailhead, 9, trail[0], trail[1])
    return rating

def main(input):
    sum = 0
    trails = defaultdict(list)
    for y in range(len(input)):
        for x in range(len(input[0])):
            if int(input[y][x]) == 0:
                sum += score_trailhead(input, x, y, trails)
    print(sum)
    sum = 0
    for trailhead, ends in trails.items():
        sum += rate_trailhead(input, trailhead, ends)
    print(sum)

import sys
if __name__ == "__main__":
    input = "example" if len(sys.argv) > 1 else "input"
    main(read(input))
