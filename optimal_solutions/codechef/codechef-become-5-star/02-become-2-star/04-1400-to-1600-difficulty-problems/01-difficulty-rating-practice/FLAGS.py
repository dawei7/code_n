


def solve():
    for _ in range(int(input())):
        n=int(input())
        pattern1=n*(n-1)*(n-1)
        pattern2=n*(n-1)*(n-1)
        pattern3=n*(n-1)*(n-2)
        pattern4=n*(n-1)*(n-2)*(n-2)
        pattern5=n*(n-1)*(n-2)*(n-2)
        print(pattern1+pattern2+pattern3+pattern4+pattern5)


if __name__ == "__main__":
    solve()
