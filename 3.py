def solve_1():
    result = 0
    for line in open("simple.txt"):
        bank = line.strip()
        best = -1
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                joltage = int(bank[i] + bank[j])
                best = max(best, joltage)

        result += best
    print(result)

def best_jolt(s, cur, pos):
    if pos >= len(s):
        ints = [int(v) for v in cur if len(v) > 0]
        return max(ints)

    results = []
    for i in range(len(cur)):
        if len(cur[i]) + len(s) - pos < 12:
            continue
        if len(cur[i]) < 12:
            results.append(cur[i] + s[pos])
            results.append(cur[i])
        else:
            results.append(cur[i])

    results = list(set(results))
    
    if True:
        d = {}
        for r in results:
            l = len(r)
            if l in d:
                d[l].add(r)
            else:
                d[l] = set()
                d[l].add(r)

        final = []
        for k in d:
            if k == 0:
                final.append("")
            else:
                final.append(str(max(int(v) for v in d[k])))
    
    return best_jolt(s, final, pos+1)


def solve_2():
    result = 0
    for line in open("input.txt"):
        bank = line.strip()
        best = best_jolt(bank, [""], 0)
        result += best
    print(result)

if __name__ == '__main__':
    solve_1()
    solve_2()
