from functools import cache

def rect_area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

def in_rect(p1, p2, p) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    x, y = p

    return min(x1, x2) < x < max(x1, x2) and min(y1, y2) < y < max(y1, y2)

def edge_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # it is enough to check the middle of the edge
    if x1 == x2:
        return [(x1, (y1 + y2) / 2)]
    elif y1 == y2:
        return [((x1 + x2) / 2, y1)]

def edge_in_rect(p1, p2, edges):
    for e in edges:
        ep = edge_points(*e)
        if not ep:
            continue
        if any(in_rect(p1, p2, p) for p in ep):
            return True
    return False

def solve(part1:  bool):
    points = [tuple(int(v) for v in line.strip().split(",")) for line in open("input.txt")]

    if part1:
        result = max(rect_area(p1, p2) for p1 in points for p2 in points)
        print(result)
        return

    edges = tuple((points[i], points[(i + 1) % len(points)]) for i in range(len(points)))
    
    result = 0
    for i in range(len(points)):
        for j in range(i + 1):
            p1 = points[i]
            p2 = points[j % len(points)]
            if edge_in_rect(p1, p2, edges):
                continue
            a = rect_area(p1, p2)
            if a > result:
                result = a

    print(result)
    
 
if __name__ == '__main__':
    solve(True)
    solve(False)
