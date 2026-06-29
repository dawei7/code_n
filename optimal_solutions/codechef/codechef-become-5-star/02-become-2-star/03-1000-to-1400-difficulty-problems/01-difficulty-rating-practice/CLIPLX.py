# cook your dish here


def solve():
    for _ in range(int(input())):
        x, y = map(int,input().split()) 
        print(max(x-y,0))


if __name__ == "__main__":
    solve()
