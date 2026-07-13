def solve(arr):
    mod = 1_000_000_007
    counts = [1, 0]
    parity = 0
    answer = 0
    for value in arr:
        parity ^= value & 1
        answer += counts[parity ^ 1]
        counts[parity] += 1
    return answer % mod
