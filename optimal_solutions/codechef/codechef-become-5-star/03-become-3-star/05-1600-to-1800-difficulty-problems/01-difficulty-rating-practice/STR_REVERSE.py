


def solve():
    for _ in range(int(input())):
        s = input()
        srev = s[::-1]
        ini = 0
        for i in s:
            if i == srev[ini]:
                ini += 1
        print(len(s) - ini)


if __name__ == "__main__":
    solve()
