


def solve():
    t = int(input())

    while t > 0:
        s = input()
        x = int(s[0:2])
        y = int(s[3:5])

        if x <= 12 and y <= 12:
            print("BOTH")
        elif y <= 12:
            print("DD/MM/YYYY")
        else:
            print("MM/DD/YYYY")
        t -= 1


if __name__ == "__main__":
    solve()
