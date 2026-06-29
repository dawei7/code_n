import sys

INF = 10**18


def divisible(chars: list[str]) -> bool:
    even = odd = 0
    for i, ch in enumerate(chars):
        if ch == "1":
            if i & 1:
                odd += 1
            else:
                even += 1
    return abs(even - odd) % 3 == 0


def evodd(chars: list[str]) -> tuple[list[str], int]:
    if divisible(chars):
        return chars[:], 0
    seen: dict[str, int] = {}
    prev = after = -1
    best = INF
    for i, ch in enumerate(chars):
        one_based = i + 1
        if i % 2 == 0 and ch == "1" and seen.get("0", 0):
            diff = one_based - seen["0"]
            if diff < best:
                best, prev, after = diff, seen["0"], one_based
        elif i % 2 == 1 and ch == "0" and seen.get("1", 0):
            diff = one_based - seen["1"]
            if diff < best:
                best, prev, after = diff, seen["1"], one_based

        if i % 2 == 0 and ch == "1":
            seen[ch] = one_based
        if i % 2 == 1 and ch == "0":
            seen[ch] = one_based

    result = chars[:]
    if prev >= 1 and after >= 1:
        result[prev - 1], result[after - 1] = result[after - 1], result[prev - 1]
        return result, after - prev
    return result, INF


def oddev(chars: list[str]) -> tuple[list[str], int]:
    if divisible(chars):
        return chars[:], 0
    seen: dict[str, int] = {}
    prev = after = -1
    best = INF
    for i, ch in enumerate(chars):
        one_based = i + 1
        if i % 2 == 1 and ch == "1" and seen.get("0", 0):
            diff = one_based - seen["0"]
            if diff < best:
                best, prev, after = diff, seen["0"], one_based
        elif i % 2 == 0 and ch == "0" and seen.get("1", 0):
            diff = one_based - seen["1"]
            if diff < best:
                best, prev, after = diff, seen["1"], one_based

        if i % 2 == 0 and ch == "0":
            seen[ch] = one_based
        if i % 2 == 1 and ch == "1":
            seen[ch] = one_based

    result = chars[:]
    if prev >= 1 and after >= 1:
        result[prev - 1], result[after - 1] = result[after - 1], result[prev - 1]
        return result, after - prev
    return result, INF


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    out = []
    for raw in tokens[1:1 + t]:
        chars = list(raw.decode())
        if divisible(chars):
            out.append("0")
            continue

        ans = INF
        tmp, moves = evodd(chars)
        tmp, moves2 = evodd(tmp)
        if moves != INF and moves2 != INF:
            ans = min(ans, moves + moves2)

        tmp, moves = oddev(chars)
        tmp, moves2 = oddev(tmp)
        if moves != INF and moves2 != INF:
            ans = min(ans, moves + moves2)

        out.append("-1" if ans == INF else str(ans))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
