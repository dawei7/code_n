# cook your dish here


def solve():
    if __name__=="__main__":
        t = int(input())
        while t:

            N, A, B = map(int, input().strip().split())
            X = 0
            for i in range(N):
                temp = X
                temp |= (1<<i)
                if (A^(temp))*(B^(temp)) > (A^X)*(B^X):
                    X |= (1<<i)
            print(X)

            t -= 1


if __name__ == "__main__":
    solve()
