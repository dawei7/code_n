# cook your dish here


def solve():
    T = int(input())
    for i in range(T):
        x, y, z = map(int, input().split())
        c = z-y
        print(c//x)


if __name__ == "__main__":
    solve()
