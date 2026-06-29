


def solve():
    MOD= 1000000007
    def d(x,y):
        return [[sum(x * y for x, y in zip(x_row,y_col)) % MOD for y_col in zip(*y)] for x_row in x]
    for j in range(int(input())):
        m= int(input())
        x= [[1,4,2], [1,0,0], [0,1,0]]
        res = [[1,0,0], [0,1,0], [0,0,1]]
        while m:
            if m&1:
                res = d(res,x)
            m >>= 1
            x = d(x,x)
        print(res[0][0])


if __name__ == "__main__":
    solve()
