from itertools import permutations
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        present = {x for x in arr if x}
        missing = [x for x in range(1, n + 1) if x not in present]
        zero_positions = [i for i, x in enumerate(arr) if x == 0]
        count = 0
        for perm in permutations(missing):
            candidate = arr[:]
            for pos, value in zip(zero_positions, perm):
                candidate[pos] = value
            rises = sum((candidate[i] > candidate[i - 1] for i in range(1, n)))
            if rises == k:
                count += 1
        out.append(str(count))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
