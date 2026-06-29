


def solve():
    for _ in range(int(input())):
        n = int(input())
        s = list(input())
        c = 0
        for i in range(n-1):
            j = i + 1
            while j < n and j < i + 10:
                if j - i == abs(int(s[i]) - int(s[j])):
                    c += 1
                j += 1
        print(c)


if __name__ == "__main__":
    solve()
