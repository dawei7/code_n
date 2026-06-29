


def solve():
    t = int(input())
    for _ in range(t):


        n = int(input())
        v = list(map(int, input().split()))

        bit = [0] * 60
        for i in v:
            for j in range(32):
                bit[j] += (i & (1 << j)) != 0

        r = 0
        for j in range(1, 60):
            bit[j] += bit[j - 1] // 2

        # Main part
        #for j in range(60):
            if bit[j]:
                r |= (1 << j)

        if bit[0]:
            r += 1

        print(r)


if __name__ == "__main__":
    solve()
