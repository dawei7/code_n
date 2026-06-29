def solve():
    n = int(input())
    s = list(map(int, input().split()))
    prev_one, curr_zero, next_one = (0, 0, 0)
    ans, zero, i = (0, 0, 0)
    while i < n:
        while i < n and s[i] == 0:
            zero += 1
            curr_zero += 1
            i += 1
        while i < n and s[i] == 1:
            next_one += 1
            i += 1
        ans = max(ans, prev_one + curr_zero + next_one)
        prev_one, curr_zero, next_one = (next_one, 0, 0)
    if ans == n and zero == 0:
        print(ans - 1)
    else:
        print(ans)


if __name__ == "__main__":
    solve()
