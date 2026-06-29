import sys


def minimum_toll(tolls: list[list[int]], switch: list[list[int]]) -> int:
    roads = len(tolls)
    booths = len(tolls[0])
    for k in range(roads):
        for i in range(roads):
            dik = switch[i][k]
            for j in range(roads):
                value = dik + switch[k][j]
                if value < switch[i][j]:
                    switch[i][j] = value

    dp = [tolls[r][0] for r in range(roads)]
    for booth in range(1, booths):
        best = [10**18] * roads
        for prev in range(roads):
            base = dp[prev]
            for cur in range(roads):
                value = base + switch[prev][cur] + tolls[cur][booth]
                if value < best[cur]:
                    best[cur] = value
        dp = best
    return min(dp)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        budget, booths, roads = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        tolls = []
        for _ in range(roads):
            tolls.append(data[idx : idx + booths])
            idx += booths
        switch = []
        for _ in range(roads):
            switch.append(data[idx : idx + roads])
            idx += roads
        toll = minimum_toll(tolls, switch)
        out.append(str(budget - toll if toll <= budget else -1))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
