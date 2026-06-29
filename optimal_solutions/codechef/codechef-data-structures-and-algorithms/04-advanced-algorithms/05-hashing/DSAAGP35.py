def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        for i in range(n):
            count = 0
            for j in range(n):
                if arr[i] == arr[j]:
                    count += 1
            print(count, end=' ')
        print()


if __name__ == "__main__":
    solve()
