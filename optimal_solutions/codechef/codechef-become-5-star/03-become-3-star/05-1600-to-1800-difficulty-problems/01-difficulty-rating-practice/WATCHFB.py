# cook your dish here


def solve():
    SPECIFIC = 1
    UNKNOWN = 2

    T = int(input())
    for _ in range(T):
        N = int(input())
        t1 = 0
        t2 = 0
        for _ in range(N):
            rtype, a, b = map(int, input().split(" "))
            if rtype == SPECIFIC:
                t1, t2 = a, b
                print("YES")
            else:
                way1 = (a >= t1 and b >= t2)
                way2 = (b >= t1 and a >= t2)
                if way1 != way2 or a == b:
                    t1, t2 = (a, b) if way1 else (b, a)
                    print("YES")
                else:
                    print("NO")


if __name__ == "__main__":
    solve()
