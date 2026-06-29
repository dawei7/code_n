import sys
MOD = 1000000007
MAX_N = 100

def build_dp():
    max_hash = [0] * (MAX_N + 1)
    for length in range(1, MAX_N + 1):
        max_hash[length] = length + max_hash[(length + 1) // 2]
    dp = [[[] for _ in range(MAX_N + 1)] for __ in range(MAX_N + 1)]
    pref = [[[] for _ in range(MAX_N + 1)] for __ in range(MAX_N + 1)]

    def set_dist(length: int, count_a: int, dist: list[int]) -> None:
        dp[length][count_a] = dist
        running = 0
        prefix = [0] * len(dist)
        for i, value in enumerate(dist):
            running = (running + value) % MOD
            prefix[i] = running
        pref[length][count_a] = prefix
    set_dist(0, 0, [1])
    set_dist(1, 0, [1, 0])
    set_dist(1, 1, [0, 1])
    for length in range(2, MAX_N + 1):
        left_len = length // 2
        right_len = length - left_len
        bound = max_hash[length]
        for count_a in range(length + 1):
            result = [0] * (bound + 1)
            low_left = max(0, count_a - right_len)
            high_left = min(left_len, count_a)
            for left_a in range(low_left, high_left + 1):
                right_a = count_a - left_a
                left_pref = pref[left_len][left_a]
                right_pref = pref[right_len][right_a]
                limit = min(max(len(left_pref), len(right_pref)), bound - count_a + 1)
                for child_hash in range(limit):
                    left_now = left_pref[child_hash] if child_hash < len(left_pref) else left_pref[-1]
                    right_now = right_pref[child_hash] if child_hash < len(right_pref) else right_pref[-1]
                    current = left_now * right_now
                    if child_hash:
                        left_prev = left_pref[child_hash - 1] if child_hash - 1 < len(left_pref) else left_pref[-1]
                        right_prev = right_pref[child_hash - 1] if child_hash - 1 < len(right_pref) else right_pref[-1]
                        current -= left_prev * right_prev
                    result[count_a + child_hash] = (result[count_a + child_hash] + current) % MOD
            set_dist(length, count_a, result)
    return dp
DP = build_dp()

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, e, value = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        length = a + e
        dist = DP[length][a] if length <= MAX_N else []
        out.append(str(dist[value] if value < len(dist) else 0))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
