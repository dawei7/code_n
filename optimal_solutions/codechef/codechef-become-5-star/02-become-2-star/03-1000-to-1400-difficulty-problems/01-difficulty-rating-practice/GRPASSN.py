


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())

        happy = True
        count = [0] * (n + 1)

        group_sizes = map(int, input().split())
        for group_size_preference in group_sizes:
            count[group_size_preference] += 1

        for j in range(2, n + 1):
            if count[j] % j != 0:
                happy = False
                break

        if happy:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
