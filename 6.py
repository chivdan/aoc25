from functools import reduce
from operator import add, mul


def solve(part1: bool):
    numbers = []
    ops = []

    input_file = "input.txt"


    if part1:
        for line in open(input_file):
            if any(str(i) in line for i in range(10)):
                numbers.append([int(v.strip()) for v in line.strip().split()])

            else:
                ops = [v.strip() for v in line.strip().split()]
        ops = [add if v == "+" else mul for v in ops]


        result = 0
        for i in range(len(ops)):
            result += reduce(ops[i], [row[i] for row in numbers])
        print(result)

    else:

        for line in open(input_file):
            line = line.replace("\n", "")
            if any(str(i) in line for i in range(10)):
                numbers.append([c for c in line])

            else:
                ops = [v.strip() for v in line.strip().split()]

        result = 0
        ops = [add if v == "+" else mul for v in ops]
        problem = []
        problem_cnt = len(ops) - 1
        for col in range(len(numbers[0]) - 1, -1, -1):
            num = ""
            for row in range(len(numbers)):
                num += numbers[row][col]
            num = num.strip()
            if len(num) == 0:
                result += reduce(ops[problem_cnt], problem)
                problem_cnt -= 1
                problem = []
            else:
                problem.append(int(num))
        if problem:
            result += reduce(ops[problem_cnt], problem)


        print(result)
            



if __name__ == '__main__':
    solve(True)
    solve(False)
