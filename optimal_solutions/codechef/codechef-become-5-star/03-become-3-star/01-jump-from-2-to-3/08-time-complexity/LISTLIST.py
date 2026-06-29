def find_min_operations(n, arr):
    frequency_map = {}
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    if len(frequency_map) == 1:
        return 0
    if len(frequency_map) == n:
        return -1
    max_frequency = max(frequency_map.values())
    return n - (max_frequency - 1)

def solve():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        result = find_min_operations(n, arr)
        print(result)


if __name__ == "__main__":
    solve()
