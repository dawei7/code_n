import sys

def earliest(n, shots):
    a_score = b_score = 0
    a_left = b_left = n
    for i, ch in enumerate(shots, start=1):
        if i % 2:
            a_left -= 1
            a_score += ch == '1'
        else:
            b_left -= 1
            b_score += ch == '1'
        if a_score > b_score + b_left or b_score > a_score + a_left:
            return i
    return 2 * n

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        shots = data[idx + 1].decode()
        idx += 2
        out.append(str(earliest(n, shots)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
