def is_valid_parentheses(s):
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            if balance == 0:
                return False
            balance -= 1
    return balance == 0

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        s = input_data[i]
        if is_valid_parentheses(s):
            results.append('1')
        else:
            results.append('0')
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
