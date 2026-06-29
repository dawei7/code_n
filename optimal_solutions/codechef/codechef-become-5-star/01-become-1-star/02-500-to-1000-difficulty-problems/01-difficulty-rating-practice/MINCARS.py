# cook your dish here


def solve():
    for _ in range(int(input())):
        n=int(input())
        print(int(n/4)) if (n%4==0) else print(int((n/4)+1))


if __name__ == "__main__":
    solve()
