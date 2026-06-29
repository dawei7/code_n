


def solve():
    for _ in range(int(input())):
        N,Q=map(int, input().split())
        floor=0
        current=0
        for i in range(Q):
            s,d=map(int, input().split())
            floor += abs(current-s) + abs(d-s)
            current=d
        print(floor)


if __name__ == "__main__":
    solve()
