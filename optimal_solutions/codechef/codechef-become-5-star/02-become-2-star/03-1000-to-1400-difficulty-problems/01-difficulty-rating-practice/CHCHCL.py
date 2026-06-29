# cook your d(ish here


def solve():
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        if n%2!=0 and m%2!=0:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    solve()
