import sys


COLOR_PRIMES = [2, 3, 5, 7, 11]


def make_cycle_colors(n: int) -> list[int]:
    if n <= 10:
        colors = [-1] * n

        def dfs(pos: int) -> bool:
            if pos == n:
                return all(
                    colors[i] != colors[(i + 1) % n] and colors[i] != colors[(i + 2) % n]
                    for i in range(n)
                )
            for color in range(5):
                if pos >= 1 and colors[pos - 1] == color:
                    continue
                if pos >= 2 and colors[pos - 2] == color:
                    continue
                colors[pos] = color
                if dfs(pos + 1):
                    return True
            colors[pos] = -1
            return False

        dfs(0)
        return colors

    fixed = n - 10
    colors = [i % 5 for i in range(fixed)] + [-1] * 10

    def ok_at(pos: int, color: int) -> bool:
        if pos >= 1 and colors[pos - 1] == color:
            return False
        if pos >= 2 and colors[pos - 2] == color:
            return False
        return True

    def dfs(pos: int) -> bool:
        if pos == n:
            return all(
                colors[i] != colors[(i + 1) % n] and colors[i] != colors[(i + 2) % n]
                for i in range(n - 12, n)
            ) and colors[n - 1] != colors[0] and colors[n - 1] != colors[1] and colors[n - 2] != colors[0]
        for color in range(5):
            if ok_at(pos, color):
                colors[pos] = color
                if dfs(pos + 1):
                    return True
                colors[pos] = -1
        return False

    dfs(fixed)
    return colors


def primes_after_11(count: int) -> list[int]:
    limit = 700_000
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i : limit + 1 : i] = b"\x00" * (((limit - i * i) // i) + 1)
    result = [i for i in range(13, limit + 1) if sieve[i]]
    return result[:count]


UNIQUE_PRIMES = primes_after_11(50_000)


def sequence(n: int) -> list[int]:
    colors = make_cycle_colors(n)
    return [
        UNIQUE_PRIMES[i] * COLOR_PRIMES[colors[i]] * COLOR_PRIMES[colors[(i + 1) % n]]
        for i in range(n)
    ]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    out: list[str] = []
    for n in data[1:]:
        out.append(" ".join(map(str, sequence(n))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
