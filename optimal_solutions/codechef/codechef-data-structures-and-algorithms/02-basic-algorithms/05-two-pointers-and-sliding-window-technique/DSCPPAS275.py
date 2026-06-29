from collections import defaultdict

def count_subarrays(arr):
    n = len(arr)
    count_map = defaultdict(int)
    i = 0
    j = 0
    count = 0
    while j < n:
        count_map[arr[j]] += 1
        while len(count_map) == 3:
            count += n - j
            count_map[arr[i]] -= 1
            if count_map[arr[i]] == 0:
                del count_map[arr[i]]
            i += 1
        j += 1
    return count

def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    print(count_subarrays(arr))


if __name__ == "__main__":
    solve()
