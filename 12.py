import numpy as np
import copy

class Present:
    def __init__(self, m):
        self.m = np.array(m)
        self.area = int(self.m.sum())

    def get_all_options(self):
        options = []
        for rot in [0, -1, -2, -3]:
            transformed = Present(np.rot90(self.m, rot))
            if transformed not in options:
                options.append(transformed)
            for flip in [np.flipud, np.fliplr]:
                flipped = Present(flip(transformed.m))
                if flipped not in options:
                      options.append(flipped)
        return options

    def get_ints(self):
        ones = []
        for i in range(3):
            for j in range(3):
                if self.m[i][j] == 1:
                    ones.append((i, j))
        return ones

    def __str__(self):
        result = ""
        for i in range(3):
            result += "".join([f"{v}" for v in self.m[i]]) + "\n"
        return result

    def __eq__(self, other):
        return str(self) == str(other)

def place_present(orig_field, si, sj, p):
    coords = p.get_ints()
    coords = [(i + si, j + sj) for (i, j) in coords]
    if any(i >= orig_field.shape[0] or j >= orig_field.shape[1] for (i, j) in coords):
        return None
    if all(orig_field[i][j] == 0 for (i, j) in coords):
        field = copy.copy(orig_field)
        for (i, j) in coords:
            field[i][j] = 1
        return field
    return None

def solve():
    def neighbors(i, j):
        result = []
        for ii in [-1, 1]:
            for jj in [-1, 1]:
                if 0 < ii < field.shape[0] and 0 < jj < field.shape[1]:
                    result.append((i - 1, j))
        return result

    def can_place(field, counts):
        if sum(counts) == 0:
            return True
        free_space = field.shape[0] * field.shape[1] - field.sum()
        for i in range(field.shape[0]):
            for j in range(field.shape[1]):
                if field[i][j] == 0:
                    if all(field[ii][jj] == 1 for (ii, jj) in neighbors(i, j)):
                          free_space -= 1
        for count_id, c in enumerate(counts):
            if c > 0:
                if presents[count_id].area > free_space:
                    continue
                for p in presents[count_id].get_all_options():
                    for i in range(field.shape[0]):
                        for j in range(field.shape[1]):
                            if field[i][j] == 0:
                                placed = place_present(field, i, j, p) 
                                if placed is not None:
                                    new_counts = counts[:]
                                    new_counts[count_id] -= 1
                                    if can_place(placed, new_counts):
                                        return True
        return False

    presents = []
    regions = []
    region_counts = []

    present = []
    for line in open("input.txt"):
        if "." in line or "#" in line:
            present.append([0 if v == "." else 1 for v in line.strip()])
        elif not line.strip():
            if present:
                presents.append(Present(present))
                present = []
        elif "x" in line:
            size, counts = line.strip().split(": ")
            regions.append([int(v) for v in size.split("x")])
            region_counts.append([int(v) for v in counts.strip().split()])

    result = 0
    
    for region, counts in zip(regions, region_counts):
        field = np.zeros((region[0], region[1]))
        
        s = sum([p.area * c for c, p in zip(counts, presents)])
        if s > region[0] * region[1]:
            print("cannot fit")
            continue
        # this simple heuristic will provide the same result
        #else:
        #    result += 1

        if can_place(field, counts):
            print("1", flush=True)
            result += 1
    print(result)

if __name__ == '__main__':
    solve()
