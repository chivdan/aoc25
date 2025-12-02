def is_made_of_repeating_sequences(s):
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

def is_made_of_two_or_more_repeating_sequences(s):
    for size in range(1, len(s) // 2 + 1):
        if len(s) % size == 0:
            sequence = s[:size]
            if sequence * (len(s) //size) == s:
                return True
    return False

def solve(part1: bool):
    result = 0
    for start_end in open('input.txt').read().strip().split(','):
        start, end = start_end.split('-')
        for i in range(int(start), int(end) + 1):
            if part1:
                if is_made_of_repeating_sequences(str(i)):
                    result += i
            else:
                if is_made_of_two_or_more_repeating_sequences(str(i)):
                    result += i
    print(result)
    
if __name__ == '__main__':
    solve(True)
    solve(False)