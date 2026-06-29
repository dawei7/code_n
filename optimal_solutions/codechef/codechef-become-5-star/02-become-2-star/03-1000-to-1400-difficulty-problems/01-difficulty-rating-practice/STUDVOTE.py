


def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = tuple(map(int, input().split()))
        d, count, j = {i : arr.count(i) for i in range(1, n + 1)}, 0, 1
        for x in d.values():
            if x >= k and arr[j - 1] != j:
                count += 1
            j += 1
        print(count)


if __name__ == "__main__":
    solve()
