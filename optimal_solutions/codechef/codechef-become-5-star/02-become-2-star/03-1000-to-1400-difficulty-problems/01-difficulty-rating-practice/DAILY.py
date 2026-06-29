# cook your dish here

from math import comb


def solve():
    def fun():
        X, N = map(int,input().strip().split())

        A = []
        for i in range(N):

            wagon  = input().strip()
            for j in range(9):
                packed = wagon[4*j:4*j+4]+wagon[53-2*j]+wagon[52-2*j]
                A.append(packed)

        count = 0
        for pack in A:
            zeros = pack.count('0')
            if zeros < X:
                continue
            else:
                count += comb(zeros,X)

        print(count)


    fun()


if __name__ == "__main__":
    solve()
