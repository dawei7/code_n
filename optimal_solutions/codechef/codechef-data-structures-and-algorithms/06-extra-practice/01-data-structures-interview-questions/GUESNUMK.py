import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    result = []
    pos = 1
    for _ in range(t):
        N = int(input_data[pos])
        K = int(input_data[pos + 1])
        pos += 2
        cnt1 = (N - 1) // 3 + 1 if N >= 1 else 0
        cnt2 = (N - 2) // 3 + 1 if N >= 2 else 0
        if K <= cnt1:
            num = 1 + 3 * (K - 1)
        elif K <= cnt1 + cnt2:
            offset = K - cnt1
            num = 2 + 3 * (offset - 1)
        else:
            offset = K - cnt1 - cnt2
            num = 3 + 3 * (offset - 1)
        result.append(str(num))
    sys.stdout.write('\n'.join(result))


if __name__ == "__main__":
    solve()
