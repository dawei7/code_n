from typing import List

def accumulate_counts(n: int, arr: List[int], k: int) -> List[int]:
    count = [0] * k
    for num in arr:
        count[num] += 1
    accumulated_count = [0] * k
    accumulated_count[0] = count[0]
    for i in range(1, k):
        accumulated_count[i] = accumulated_count[i - 1] + count[i]
    return accumulated_count

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:n + 1]))
    k = int(data[n + 1])
    result = accumulate_counts(n, arr, k)
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    solve()
