


def solve():
    t = int(input())

    while t > 0:
        s = input()
        s = "0" + s
        s = s[-2:]  # Get the last two characters
        n = int(s)  # Convert to integer
        print(n % 20)
        t -= 1


if __name__ == "__main__":
    solve()
