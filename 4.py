def neighbors(i, j, m):
    for ii in [i - 1, i, i + 1]:
        if ii < 0 or ii >= len(m):
            continue
        for jj in [j - 1, j, j + 1]:
            if ii == i and jj == j:
                continue
            if jj < 0 or jj >= len(m[i]):
                continue
            yield ii, jj

def solve_1(m):
    result = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1 and sum(m[ii][jj] for ii, jj in neighbors(i, j, m)) < 4:
                result += 1
    print(result)

def solve_2(m):
    result = 0
    while True:
        changed = False
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 1 and sum(m[ii][jj] for ii, jj in neighbors(i, j, m)) < 4:
                    result += 1
                    m[i][j] = 0
                    changed = True
        if not changed:
            break
    print(result)





if __name__ == '__main__':
    m = [[0 if c == "." else 1 for c in line.strip().replace("\n", "")] for line in open("input.txt")]
 
    solve_1(m)
    solve_2(m)
