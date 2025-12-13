from functools import cache

def count(graph, current):
    if current == "out":
        return 1

    return sum(count(graph, child) for child in graph[current])


def solve(part1: bool):
    @cache
    def count_part2(current, dac, fft):
        if current == "out":
            if dac and fft:
                return 1
            else:
                return 0
        cur_dac = dac
        if not dac and current == "dac":
            cur_dac = True
        cur_fft = fft
        if not fft and current == "fft":
            cur_fft = True

        return sum(count_part2(child, cur_dac, cur_fft) for child in graph[current])


    graph = dict()
    for line in open("input.txt"):
        source, targets = line.strip().split(":")
        targets = [v.strip() for v in targets.strip().split()]
        graph[source] = targets

    if part1:
        result = count(graph, "you")
        print(result)
    else:
        result = count_part2("svr", False, False)
        print(result)




if __name__ == '__main__':
    solve(True)
    solve(False)
