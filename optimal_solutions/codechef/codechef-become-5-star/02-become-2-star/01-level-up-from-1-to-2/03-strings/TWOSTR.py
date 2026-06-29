


def solve():
    t = int(input())

    while t > 0:
        x = input()
        y = input()

        match = True

        for j in range(len(x)):
            if x[j] != '?' and y[j] != '?' and x[j] != y[j]:
                match = False
                break

        print("Yes" if match else "No")
        t -= 1


if __name__ == "__main__":
    solve()
