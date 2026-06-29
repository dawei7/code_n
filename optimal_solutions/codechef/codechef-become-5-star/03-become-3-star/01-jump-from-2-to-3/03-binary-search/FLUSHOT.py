def check(positions, N, T, mid):
    currPos = positions[N - 1] + mid
    for i in range(N - 2, -1, -1):
        currPos -= T
        if currPos > positions[i] + mid:
            currPos = positions[i] + mid
        elif currPos < positions[i] - mid:
            return False
    if currPos >= 0.0:
        return True
    return False

def solve(positions, N, T):
    low, high, ans = (0.0, 10000000000.0, 0.0)
    while high - low > 5e-05:
        mid = (low + high) / 2.0
        if check(positions, N, T, mid) == True:
            ans = mid
            high = mid
        else:
            low = mid
    print('%.4f' % ans)


if __name__ == "__main__":
    solve()
