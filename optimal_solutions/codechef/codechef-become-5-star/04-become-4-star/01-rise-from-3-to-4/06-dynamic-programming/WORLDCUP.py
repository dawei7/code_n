import sys
MOD = 1000000007
MAX_B = 300
FACT = [1] * (MAX_B + 1)
for i in range(1, MAX_B + 1):
    FACT[i] = FACT[i - 1] * i % MOD
INV_FACT = [1] * (MAX_B + 1)
INV_FACT[MAX_B] = pow(FACT[MAX_B], MOD - 2, MOD)
for i in range(MAX_B, 0, -1):
    INV_FACT[i - 1] = INV_FACT[i] * i % MOD

def count_scores(runs: int, balls: int, wickets_limit: int) -> int:
    if runs % 2:
        return 0
    answer = 0
    max_wickets = min(wickets_limit, balls)
    for wickets in range(max_wickets + 1):
        remaining_balls = balls - wickets
        ways_place_wickets = FACT[balls] * INV_FACT[wickets] % MOD
        max_sixes = min(remaining_balls, runs // 6)
        for sixes in range(max_sixes + 1):
            rest = runs - 6 * sixes
            if rest % 4:
                continue
            fours = rest // 4
            if fours + sixes > remaining_balls:
                continue
            zeros = remaining_balls - fours - sixes
            ways = ways_place_wickets
            ways = ways * INV_FACT[fours] % MOD
            ways = ways * INV_FACT[sixes] % MOD
            ways = ways * INV_FACT[zeros] % MOD
            answer = (answer + ways) % MOD
    return answer

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        runs, balls, wickets_limit = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        out.append(str(count_scores(runs, balls, wickets_limit)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
