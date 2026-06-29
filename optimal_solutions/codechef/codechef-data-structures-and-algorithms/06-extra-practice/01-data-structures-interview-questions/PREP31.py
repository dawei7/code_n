def min_jumps_to_end(n, arr):
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1
    jumps = 1
    current_end = arr[0]
    farthest = arr[0]
    for i in range(1, n):
        if i == n - 1:
            return jumps
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end <= i:
                return -1
    return -1

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        arr = list(map(int, input_data[index:index + n]))
        index += n
        results.append(str(min_jumps_to_end(n, arr)))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
