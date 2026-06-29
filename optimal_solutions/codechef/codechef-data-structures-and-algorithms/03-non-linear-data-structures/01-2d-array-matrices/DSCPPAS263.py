def solve():
    n, m = list(map(int, input().split()))
    total_elements = n * m
    if total_elements % 2 != 0:
        print(-1)
    else:
        for i in range(n):
            for j in range(m):
                print(1, end=' ')
            print()


if __name__ == "__main__":
    solve()
