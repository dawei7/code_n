


def solve():
    for i in range(int(input())):
        n = int(input())
        inx = iter(map(int, input().split()))
        n = next(inx)
        a = [(x, 0, -y) for x, y in zip(inx, inx)]
        inx = iter(map(int, input().split()))
        n = next(inx)
        a.extend(zip(inx, inx, inx))
        a.sort()
        def check(x):
            for _, k, v in a:
                if x >= k:
                    x += v
                if x <= 0:
                    return False
            return True

        n = len(a)
        lb, ub = 0, 1 << 63
        while ub - lb > 1:
            mid = (ub + lb) // 2
            if check(mid):
                ub = mid
            else:
                lb = mid
        print(ub)# cook your dish here


if __name__ == "__main__":
    solve()
