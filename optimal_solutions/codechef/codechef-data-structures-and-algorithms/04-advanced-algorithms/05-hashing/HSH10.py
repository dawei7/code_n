


def solve():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))

    mp = {}

    for i, val in enumerate(arr):
        mp[val] = i

    for val in arr:
        print(mp[val], end=" ")
    print()


if __name__ == "__main__":
    solve()
