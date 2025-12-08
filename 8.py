import math

def dist(p1, p2):
    return math.sqrt(sum((p1[i] - p3[i])**2 for i in range(3))    

def closest_pair(points):
    min_dist = 1e20
    best_pair = None
    for i in range(len(points)):
        for j in range(i):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                best_pair = (points[i], points[j])
    return best_pair
                     
def solve():
    points = []
    for line in open("simple.txt"):
        points.append((int(v) for v in line.strip().split(",")))

    circuits = []

    for n in range(10):
        best_pair = closest_pair(points)
        p1, p2 = best_pair
        merged = False
        for i in range(len(circuits)):
            if p1 in circuits[i] and p2 in circuits[i]:
                merged = True
                break
            elif p1 in circuits[i] and not p2 in circuits[i]:
                circuits[i].append(p2)
                merged = True
                break
            elif p1 not in circuits[i] and p2 not in circuits[i]:
                circuits[i].append(p1)
                merged = True
                break
        if not merged:
            circuits.append(list(best_pair))

    circuits = sorted(circuits, key=lambda c: -len(c))

    result = len(circuits[0)*len(circuits[1])*len(circuits[2]))
    print(result)


    

    
        

if __name__ == '__main__':
    solve()
