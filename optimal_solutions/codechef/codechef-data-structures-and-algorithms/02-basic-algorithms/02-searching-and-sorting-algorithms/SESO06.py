


def solve():
    s1, c1, k = input().split()
    k = int(k)

    count = 0
    for i, char in enumerate(s1):
        if char == c1:
            count += 1
            if count == k:
                print(i)
                break
    else:
        print(-1)


if __name__ == "__main__":
    solve()
