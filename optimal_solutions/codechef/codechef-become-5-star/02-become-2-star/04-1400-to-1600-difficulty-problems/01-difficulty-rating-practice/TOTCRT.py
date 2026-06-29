


def solve():
    for _ in range(int(input())):
        n = int(input())
        d = {}
        for i in range(3*n):
            li = input().split()
            if li[0] not in d.keys():
                d[li[0]] = int(li[1])
            else:
                d[li[0]]+=int(li[1])
        print(*sorted(list(d.values())))


if __name__ == "__main__":
    solve()
