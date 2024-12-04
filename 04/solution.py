def load_puzzle() -> list:
    lines = []
    with open('input', 'r') as f:
        for line in f:
            lines.append(line)
    return lines

def count_in_rows(rows):
    count = 0
    for row in rows:
        count += row.count("XMAS") + row.count("SAMX")
    return count

def count_in_cols(puzzle):
    flip = [*zip(*puzzle)]
    flip = [''.join(s) for s in flip]
    count = 0
    for col in flip:
        count += col.count("XMAS") + col.count("SAMX")
    return count

def count_diagonals(puzzle):
    count = 0
    i = 0
    while i < len(puzzle):
        j = 0
        while j < len(puzzle[i]):
            if puzzle[i][j] == 'X':
                if i + 3 < len(puzzle):
                    if (j + 3 < len(puzzle[i]) and
                    puzzle[i+1][j+1] == 'M' and
                    puzzle[i+2][j+2] == 'A' and
                    puzzle[i+3][j+3] == 'S'):
                        count += 1
                    if (j > 2 and
                    puzzle[i+1][j-1] == 'M' and
                    puzzle[i+2][j-2] == 'A' and
                    puzzle[i+3][j-3] == 'S'):
                        count += 1
                if i > 2:
                    if (j + 3 < len(puzzle[i]) and
                    puzzle[i-1][j+1] == 'M' and
                    puzzle[i-2][j+2] == 'A' and
                    puzzle[i-3][j+3] == 'S'):
                        count += 1
                    if (j > 2 and
                    puzzle[i-1][j-1] == 'M' and
                    puzzle[i-2][j-2] == 'A' and
                    puzzle[i-3][j-3] == 'S'):
                        count += 1
            j += 1
        i += 1
    return count

def count_x_mas(puzzle):
    count = 0
    i = 1
    while i + 1 < len(puzzle):
        j = 1
        while j + 1 < len(puzzle[i]):
            if puzzle[i][j] == 'A':
                one = ((puzzle[i-1][j-1] == 'M' and puzzle[i+1][j+1] == 'S') or
                        (puzzle[i-1][j-1] == 'S' and puzzle[i+1][j+1] == 'M'))
                two = ((puzzle[i-1][j+1] == 'M' and puzzle[i+1][j-1] == 'S') or
                        (puzzle[i-1][j+1] == 'S' and puzzle[i+1][j-1] == 'M'))
                if one and two:
                    count += 1
            j += 1
        i += 1
    return count

def main() -> None:
    puzzle = load_puzzle()
    count = count_in_rows(puzzle) + count_in_cols(puzzle) + count_diagonals(puzzle)
    print(count)
    count = count_x_mas(puzzle)
    print(count)

if __name__ == "__main__":
    main()

