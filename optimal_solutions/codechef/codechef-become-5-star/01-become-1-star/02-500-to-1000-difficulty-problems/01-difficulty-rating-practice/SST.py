# cook your dish here


def solve():
    for _ in range(int(input())):
        a,b = map(int,input().split())
        print("First") if (2*a)>b else print("second") if (2*a)<b else print("Any")


if __name__ == "__main__":
    solve()
