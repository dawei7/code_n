def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        total_sum = sum(arr)
        arr.sort()
        sum_of_k_smallest = sum(arr[:k])
        sum_of_k_largest = sum(arr[-k:])
        diff1 = abs(sum_of_k_smallest - (total_sum - sum_of_k_smallest))
        diff2 = abs(sum_of_k_largest - (total_sum - sum_of_k_largest))
        print(max(diff1, diff2))


if __name__ == "__main__":
    solve()
