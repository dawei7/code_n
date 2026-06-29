


def solve():
    def upper_bound(array, key):
        low = 0
        high = len(array)
        while low < high:
            mid = low + (high - low) // 2
            if array[mid] <= key:
                low = mid + 1
            else:
                high = mid
        return low

    t = int(input())
    for _ in range(t):
        n = int(input())
        v = list(map(int, input().split()))
        v.sort()
        ans = 0
        for i in range(n):
            d = upper_bound(v, v[i])
            if d > (n - d):
                ans += 1
        print(ans)


if __name__ == "__main__":
    solve()
