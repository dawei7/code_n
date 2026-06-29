# cook your dish here


def solve():
    t=int(input())
    for i in range(t):
            x,y,z=map(int,input().split())
            print(z-(y//x)) if (z-(y//x))>0 else print(0)


if __name__ == "__main__":
    solve()
