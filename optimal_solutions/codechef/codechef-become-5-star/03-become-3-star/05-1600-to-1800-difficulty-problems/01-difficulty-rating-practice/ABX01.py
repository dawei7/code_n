import sys

def digital_root_mod9(value):
    return 9 if value % 9 == 0 else value % 9

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        base, exponent = (data[idx], data[idx + 1])
        idx += 2
        out.append(str(digital_root_mod9(pow(base % 9, exponent, 9))))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
