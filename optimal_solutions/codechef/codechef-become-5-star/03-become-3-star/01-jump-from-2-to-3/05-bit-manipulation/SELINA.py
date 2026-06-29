


def solve():
    t = int(input())

    for _ in range(t):
        s = input()

        d = dict()
        for _ in range(len(s)):
            if s[_] in d:
                d[s[_]] += 1
            else:
                d[s[_]] = 1

        found = False
        for key, value in d.items():
            if value % 2 != 0:
                found = True
                print(key)
                break

        if not found:
            print(-1)


if __name__ == "__main__":
    solve()
