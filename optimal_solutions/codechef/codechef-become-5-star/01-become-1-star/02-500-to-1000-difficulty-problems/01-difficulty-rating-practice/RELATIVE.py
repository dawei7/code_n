# cook your dish here


def solve():
    for _ in range(int(input())):
        g,c = map(int, input().split())
        x = c*c
        y = 2*g
        z = x//y
        print(z)


if __name__ == "__main__":
    solve()
