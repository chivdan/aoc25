import sympy
import itertools
from functools import cache

def apply_indicators(current, button):
    result = list(current[:])
    for light in button:
        result[light] = not result[light]
    return tuple(result)


@cache
def solve_case_indicators(target, buttons, current, cnt):
    if target == current:
        return cnt
    if cnt >= len(target) * 2:
        return 1e10
    return min(solve_case_indicators(target, buttons, apply_indicators(current, b), cnt + 1) for b in buttons)

def solve_case_joltage(target, buttons):
    x = []
    for i in range(len(buttons)):
        x.append(sympy.symbols(f"x_{i}", integer=True, nonnegative=True))

    equations = []
    # build equation for every target element
    for i in range(len(target)):
        lhs = 0
        for j in range(len(buttons)):
            if i in buttons[j]:
                 lhs += x[j]

        equations.append(sympy.Eq(lhs, target[i]))
  
   
    solution = sympy.solve(equations, x)
    free_vars = set()
    for k, v in solution.items():
        for i in range(len(buttons)):
            if f"x_{i}" in str(v):
                free_vars.add(f"x_{i}")

    free_symbols = set()
    for _, expr in solution.items(): 
        free_symbols = free_symbols.union(expr.free_symbols)
    free_symbols = sorted(list(free_symbols), key=lambda x: str(x))

    min_result = 1e10

    s_expr = 0
    for v in solution.values():
        s_expr += v
    for v in free_symbols:
        s_expr += v
    total_expr = 0
    for v in x:
        total_expr += v

    with open("f.mzn", "w") as f:
        # write minizinc problem
        for v in set(free_symbols).union(solution.keys()):
            f.write(f"var 0..200: {v};\n")
            
        # write constraints
        for v, expr in solution.items():
            simp = sympy.simplify(8*3*7*5*expr)
            f.write(f"constraint {8*3*7*5*v} = {simp};\n")
        
        # write goal
        f.write(f"solve minimize {total_expr};\n")

    minizinc_str = open("f.mzn").read()
    import minizinc
    model = minizinc.Model()
    model.add_string(minizinc_str)
    chuffed = minizinc.Solver.lookup("chuffed")
    inst = minizinc.Instance(chuffed, model)
    result = inst.solve()
    return result.objective

def solve(part1: bool):
    result = 0
    ndone = 0
    for line in open("input.txt"):
        target = None
        buttons = []
        joltage = []

        for v in line.strip().split():
            if "[" in v:
                target = [False if c == "." else True for c in v[1:-1]]
            elif "(" in v:
                buttons.append(tuple([int(c) for c in v[1:-1].split(",")]))
            else:
                joltage = [int(c) for c in v[1:-1].split(",")]
        target = tuple(target)
        buttons = tuple(buttons)
        joltage = tuple(joltage)
        if part1:
            result += solve_case_indicators(target, buttons, tuple([False] * len(target)), 0)
        else:
            result += solve_case_joltage(joltage, buttons)
        ndone += 1
    print(result)

if __name__ == '__main__':
    solve(True)
    solve(False)
