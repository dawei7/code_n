import sys

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for token in data[1:1 + t]:
        zeros = token.count(b'0')
        ones = len(token) - zeros
        out.append('Yes' if zeros == 1 or ones == 1 else 'No')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
