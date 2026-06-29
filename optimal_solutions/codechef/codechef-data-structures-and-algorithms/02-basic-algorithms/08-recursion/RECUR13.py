


def solve():
    def Binary(n):
        if(n==0):
            return ''
        return Binary(n//2) + str(n&1)

    n = int(input())
    print(Binary(n))


if __name__ == "__main__":
    solve()
