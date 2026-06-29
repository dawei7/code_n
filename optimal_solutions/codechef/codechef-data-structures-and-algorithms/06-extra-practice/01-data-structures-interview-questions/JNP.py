import sys
from bisect import bisect_right


def solve():
    def patternNash(S, T, n):
        # Precompute positions for each character in S
        pos_map = {}
        for i, ch in enumerate(S):
            if ch not in pos_map:
                pos_map[ch] = []
            pos_map[ch].append(i)

        copies = 1
        currentPos = -1
        for ch in T:
            if ch not in pos_map:
                return "NO"
            lst = pos_map[ch]
            idx = bisect_right(lst, currentPos)
            if idx == len(lst):
                copies += 1
                if copies > n:
                    return "NO"
                currentPos = lst[0]
            else:
                currentPos = lst[idx]
        return "YES"

    if __name__ == "__main__":
        data = sys.stdin.read().strip().split()
        if not data:
            sys.exit(0)
        t = int(data[0])
        output = []
        index = 1
        for _ in range(t):
            S = data[index]
            T = data[index + 1]
            n = int(data[index + 2])
            index += 3
            output.append(patternNash(S, T, n))
        sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
