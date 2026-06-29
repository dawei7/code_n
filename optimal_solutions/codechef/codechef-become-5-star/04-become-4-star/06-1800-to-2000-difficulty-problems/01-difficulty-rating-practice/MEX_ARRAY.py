from collections import Counter
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    output = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        freq = Counter(arr)
        result = []
        while freq.get(0, 0) > 0:
            mex = 0
            while freq.get(mex, 0) > 0:
                mex += 1
            result.append(mex)
            for value in range(mex):
                freq[value] -= 1
        remaining = sum(freq.values())
        result.extend([0] * remaining)
        output.append(str(len(result)))
        output.append(' '.join(map(str, result)))
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
