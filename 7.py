
from functools import cache

def solve(part1: bool):
    @cache
    def count(beam, row):
        if row == len(m) - 1:
            return 1
        if m[row][beam] == "^":
            result = 0
            if beam - 1 >= 0:
                result += count(beam - 1, row + 1)
            if beam + 1 <= len(m[row]):
                result += count(beam + 1, row + 1)
            return result
        else:
            return count(beam, row + 1)
        

    m = []
    for line in open("input.txt"):
        m.append([v for v in line.strip()])

    s_col = m[0].index("S")

    if part1:
        beams = {s_col}
        n_splits = 0
        for i in range(1, len(m)):
            next_beams = set()
            for j in range(len(m[i])):
                if m[i][j] == "." and j in beams:
                    next_beams.add(j)
                elif m[i][j] == "^" and j in beams:
                    if j - 1 >= 0:
                        next_beams.add(j - 1)
                    if j + 1 < len(m[i]):
                        next_beams.add(j + 1)
                    n_splits += 1
            beams = next_beams

        print(n_splits)

    else:
        print(count(s_col, 1))


            



if __name__ == '__main__':
    solve(True)
    solve(False)
