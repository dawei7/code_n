import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n, eggs, bars, cost_om, cost_milk, cost_cake = data[idx:idx + 6]
        idx += 6
        best = None

        max_cakes = min(n, eggs, bars)
        for cakes in range(max_cakes + 1):
            rem = n - cakes
            max_om = (eggs - cakes) // 2
            max_milk = (bars - cakes) // 3

            low_om = max(0, rem - max_milk)
            high_om = min(rem, max_om)
            if low_om > high_om:
                continue

            if cost_om <= cost_milk:
                omelettes = high_om
            else:
                omelettes = low_om
            milkshakes = rem - omelettes
            total = (
                omelettes * cost_om
                + milkshakes * cost_milk
                + cakes * cost_cake
            )
            if best is None or total < best:
                best = total

        out.append(str(best if best is not None else -1))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
