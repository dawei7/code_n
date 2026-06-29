def solve():
    m, n, k = map(int, input().split())
    v = []
    v_first = list(map(int, input().split()))
    v_second = list(map(int, input().split()))
    for i in range(m):
        v.append([v_first[i], v_second[i]])
    ans = -1
    low, high = (0, int(1000000000.0))
    while low <= high:
        mid = low + (high - low) // 2
        vv = []
        for i in range(m):
            if v[i][0] > mid:
                vv.append(0)
                continue
            p = mid - v[i][0]
            q = p // v[i][1]
            vv.append(q + 1)
        vv.sort(reverse=True)
        c = 0
        for i in range(min(m, n)):
            c += vv[i]
        if c >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)


if __name__ == "__main__":
    solve()
