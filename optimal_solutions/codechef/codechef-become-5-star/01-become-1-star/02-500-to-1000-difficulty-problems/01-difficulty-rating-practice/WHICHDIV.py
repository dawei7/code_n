import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for rating in data[1:1 + t]:
        if rating >= 2000:
            out.append('1')
        elif rating >= 1600:
            out.append('2')
        else:
            out.append('3')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
