import sys


def best_for_type(values, types, chosen_type):
    best = None
    cur = 0
    for value, candy_type in zip(values, types):
        if candy_type != chosen_type:
            continue
        contribution = value
        cur = max(contribution, cur + contribution)
        best = cur if best is None else max(best, cur)
    return best if best is not None else -10**30


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        typ = data[idx:idx + n]
        idx += n

        out.append(str(max(best_for_type(a, typ, 0), best_for_type(a, typ, 1))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
