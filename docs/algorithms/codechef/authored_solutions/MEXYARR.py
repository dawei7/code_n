import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        b = data[idx:idx + n]
        idx += n
        constrained = [(i, value) for i, value in enumerate(b) if value >= 0]
        ok = True
        prev = -1
        for _, value in constrained:
            if value < prev or value > n:
                ok = False
                break
            prev = value
        if not ok:
            out.append("-1")
            continue

        max_mex = max([value for _, value in constrained], default=0)
        last_equal = [-1] * (max_mex + 1)
        first_greater = [None] * max_mex
        filled_until = 0
        for pos, value in constrained:
            if value <= max_mex:
                last_equal[value] = pos
            while filled_until < min(value, max_mex):
                first_greater[filled_until] = pos
                filled_until += 1
        intervals = []
        for value in range(max_mex):
            release = last_equal[value] + 1
            deadline = first_greater[value]
            if deadline is None:
                ok = False
                break
            intervals.append((deadline, release, value))
        if not ok:
            out.append("-1")
            continue

        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        ans = [10**9] * n
        for deadline, release, value in sorted(intervals):
            pos = find(release)
            if pos > deadline:
                ok = False
                break
            ans[pos] = value
            parent[pos] = find(pos + 1)
        if ok:
            seen = [False] * (n + 2)
            mex = 0
            for i, value in enumerate(ans):
                if value <= n:
                    seen[value] = True
                    while seen[mex]:
                        mex += 1
                if b[i] >= 0 and mex != b[i]:
                    ok = False
                    break
        out.append(" ".join(map(str, ans)) if ok else "-1")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
