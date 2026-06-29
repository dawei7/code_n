


def solve():
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        n = len(s)
        pass_check = True

        for i in range(0, n - 1, 2):
            if s[i] == s[i + 1]:
                pass_check = False
                break

        if pass_check:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    solve()
