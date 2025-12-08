import math

def dist(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(3)))    

def merge_until(points, n_merges: int = -1, one_circuit: bool = False):
    circuits = []
    connected = [[False for i in range(len(points))] for j in range(len(points))]
    point_in_circuit = [False] * len(points)
    circuit_of_point = [-1] * len(points)
    connection_order = []

    distances = []
    for i in range(len(points)):
        for j in range(i):
            d = dist(points[i], points[j])
            distances.append((i, j, d))
    distances = sorted(distances, key=lambda p: p[2])
 
    n = 0
    while True:
        if n_merges != -1 and n == n_merges:
            break
        elif one_circuit:
            if len(circuits) == 1 and len(circuits[0]) == len(points):
                break
        p1, p2, _ = distances[0]
        merged = False

        for i in range(len(circuits)):
            if p1 in circuits[i] and p2 in circuits[i]:
                merged = True
                break
            elif p1 in circuits[i] and not point_in_circuit[p2]:
                circuits[i].append(p2)
                merged = True
                break
            elif p2 in circuits[i] and not point_in_circuit[p1]:
                circuits[i].append(p1)
                merged = True
                break

        if not merged:
            for i in range(len(circuits)):
                for j in range(i):
                    if (p1 in circuits[i] and p2 in circuits[j]) or (p2 in circuits[i] and p1 in circuits[j]):
                        circuits[i].extend(circuits[j])
                        circuits.pop(j)
                        merged = True
                        break
                if merged:
                    break

        if not merged:
            circuits.append([p1, p2])
            circuit_of_point[p1] = len(circuits)
            circuit_of_point[p2] = len(circuits)
        connected[p1][p2] = True
        connected[p2][p1] = True
        connection_order.append((p1, p2))
        point_in_circuit[p1] = True
        point_in_circuit[p2] = True
        distances.pop(0)
        n += 1


    circuits = sorted(circuits, key=lambda c: -len(c))
    return circuits, connection_order

def solve(part1: bool):
    points = []
    for line in open("input.txt"):
        points.append(tuple(int(v) for v in line.strip().split(",")))

    if part1:
        circuits, _ = merge_until(points, 1000, False)
        result = len(circuits[0])*len(circuits[1])*len(circuits[2])
    else:
        _, connected_order = merge_until(points, -1, True)
        result = points[connected_order[-1][0]][0] * points[connected_order[-1][1]][0]

    print(result)


if __name__ == '__main__':
    solve(True)
    solve(False)
