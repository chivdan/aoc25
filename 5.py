class Interval:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def is_in(self, other) -> bool:
        return other.l <= self.l <= self.r <= other.r

    def intersects(self, other) -> bool:
        return self.l <= other.l <= self.r <= other.r or other.l <= self.l <= other.r <= self.r

    def merge(self, other):
        self.l = min(self.l, other.l)
        self.r = max(self.r, other.r)

    def __str__(self):
        return f"({self.l}..{self.r})"

def solve(part1: bool):
    intervals = []
    ids = []
    for line in open("input.txt"):
        line = line.strip()
        if "-" in line:
            s, e = (int(v) for v in line.split("-"))
            intervals.append((s, e))
        elif line:
            ids.append(int(line))

    if part1:
        result = 0
        for i in ids:
            if any(s <= i <= e for s, e in intervals):
                result += 1
        print(result)

    else:
        intervals = sorted(intervals)

        intervals = [Interval(i[0], i[1]) for i in intervals]
            
        while True:
            changed = False
            for i in range(len(intervals)):
                if changed:
                    break
                for j in range(len(intervals)):
                    if i == j:
                        continue
                    if intervals[i].intersects(intervals[j]):
                        intervals[i].merge(intervals[j])
                        intervals.pop(j)
                        changed = True
                    elif intervals[i].is_in(intervals[j]):
                        intervals.pop(i)
                        changed = True
                    if changed:
                        break

            if not changed:
                break

        result = 0
        for i in intervals:
            result += i.r - i.l + 1
        
        print(result)


if __name__ == '__main__':
    solve(True)
    solve(False)
