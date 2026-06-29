import sys


def next_without_digit(number, digit):
    s = list(str(number))
    for i, ch in enumerate(s):
        if int(ch) == digit:
            if digit == 9:
                prefix = str(int("".join(s[:i]) or "0") + 1)
                candidate = prefix + "0" * (len(s) - i)
            else:
                s[i] = str(int(ch) + 1)
                candidate = "".join(s[:i + 1]) + "0" * (len(s) - i - 1)
            return next_without_digit(int(candidate), digit)
    return number


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        number, digit = data[idx], data[idx + 1]
        idx += 2
        out.append(str(next_without_digit(number, digit) - number))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
