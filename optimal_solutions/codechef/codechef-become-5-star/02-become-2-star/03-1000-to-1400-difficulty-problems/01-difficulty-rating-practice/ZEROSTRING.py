


def solve():
    for _ in range(int(input())):
        N=int(input())
        s=input()
        one=s.count("1")
        zero=s.count("0")
        if zero>=one:
            val=one
        else:
            val=1+zero
        print(val)


if __name__ == "__main__":
    solve()
