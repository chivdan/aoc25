def solve(part1: bool):
    current = 50
    n_zeros = 0
    for line in open("input.txt"):
        l = line.strip()
        direction, value = l[0], int(l[1:])

        if part1:
            if direction == 'L':
                current -= value
            elif direction == 'R':
                current += value

            if current < 0 or current >= 100:
                current = current % 100
            if current == 0:
                n_zeros += 1
        else:
            sign = 1 if direction == 'R' else -1
            while value > 0:
                current += sign
                value -= 1
                if current < 0:
                    current = 99
                elif current >= 100:
                    current = 0
                if current == 0:
                    n_zeros += 1
    print(n_zeros)


if __name__ == "__main__":
    solve(True)
    solve(False)
