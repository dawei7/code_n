# cook your dish here


def solve():
    x,y=map(str,input().split())
    if x=="R" or y=="R":
        print("R")
    elif x=="B" or y=="B":
        print("B")
    else:
        print("G")


if __name__ == "__main__":
    solve()
