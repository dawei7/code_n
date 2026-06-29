


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        arr.sort()
        odd = []
        even = []
        left = []
        right = []
        for i in arr:
            if i%2:
                odd += [i]
            else:
                even += [i]
        o = len(odd)
        e = len(even)
        LO = odd[:o//2]
        RO = odd[o//2:]
        LE = even[:e//2]
        RE = even[e//2:]
        if len(LO)!=len(RO) or len(LE)!=len(RE):
            print(-1)
        else:
            for i in range(len(RO)-1,-1,-1):
                a = (RO[i]+LO[i])//2
                b = RO[i] - a
                left += [a]
                right += [b]
            for i in range(len(RE)-1,-1,-1):
                a = (RE[i]-LE[i])//2
                b = RE[i] - a
                left += [a]
                right += [b]
            print(*(left+right))


if __name__ == "__main__":
    solve()
