def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    output = []
    pos = 1
    for _ in range(t):
        X = data[pos]
        M = int(data[pos + 1])
        pos += 2
        new_digits = []
        if M == 0:
            new_digits = ['1'] * len(X)
        else:
            for ch in X:
                new_digits.append(str(pow(int(ch), M, 10)))
        reversed_number = int(''.join(new_digits)[::-1])
        output.append('YES' if reversed_number % 7 == 0 else 'NO')
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
