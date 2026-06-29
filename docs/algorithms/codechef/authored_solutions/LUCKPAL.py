import sys

LUCKY = "lucky"


def candidate(original: str, start: int) -> tuple[int, str] | None:
    n = len(original)
    forced: dict[int, str] = {start + i: ch for i, ch in enumerate(LUCKY)}
    result = [""] * n
    cost = 0

    for i in range((n + 1) // 2):
        j = n - 1 - i
        left_forced = forced.get(i)
        right_forced = forced.get(j)

        if i == j:
            chosen = left_forced or right_forced or original[i]
            cost += original[i] != chosen
            result[i] = chosen
            continue

        if left_forced and right_forced:
            if left_forced != right_forced:
                return None
            chosen = left_forced
        elif left_forced:
            chosen = left_forced
        elif right_forced:
            chosen = right_forced
        elif original[i] == original[j]:
            chosen = original[i]
        else:
            chosen = min(original[i], original[j])

        cost += original[i] != chosen
        cost += original[j] != chosen
        result[i] = result[j] = chosen

    text = "".join(result)
    if LUCKY not in text:
        return None
    return cost, text


def solve_one(text: str) -> str:
    n = len(text)
    if n < len(LUCKY):
        return "unlucky"

    best: tuple[int, str] | None = None
    for start in range(n - len(LUCKY) + 1):
        cur = candidate(text, start)
        if cur is None:
            continue
        if best is None or cur[0] < best[0] or (cur[0] == best[0] and cur[1] < best[1]):
            best = cur

    if best is None:
        return "unlucky"
    return f"{best[1]} {best[0]}"


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    out = [solve_one(tokens[i].decode()) for i in range(1, t + 1)]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
