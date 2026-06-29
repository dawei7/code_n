import sys
MOD = 1000000007

def minimum_stop_plans(positions: list[int], max_distance: int) -> tuple[int, int]:
    n = len(positions)
    jumps = [10 ** 9] * n
    ways = [0] * n
    jumps[0] = 0
    ways[0] = 1
    count_by_jump = [0] * (n + 1)
    ways_by_jump = [0] * (n + 1)
    count_by_jump[0] = 1
    ways_by_jump[0] = 1
    min_jump = 0
    left = 0
    for i in range(1, n):
        while left < i and positions[i] - positions[left] > max_distance:
            old = jumps[left]
            count_by_jump[old] -= 1
            ways_by_jump[old] = (ways_by_jump[old] - ways[left]) % MOD
            left += 1
        while min_jump <= n and count_by_jump[min_jump] == 0:
            min_jump += 1
        jumps[i] = min_jump + 1
        ways[i] = ways_by_jump[min_jump] % MOD
        count_by_jump[jumps[i]] += 1
        ways_by_jump[jumps[i]] = (ways_by_jump[jumps[i]] + ways[i]) % MOD
    return (jumps[-1] - 1, ways[-1] % MOD)

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, max_distance = (data[0], data[1])
    positions = data[2:2 + n]
    stops, ways = minimum_stop_plans(positions, max_distance)
    print(stops, ways)


if __name__ == "__main__":
    solve()
