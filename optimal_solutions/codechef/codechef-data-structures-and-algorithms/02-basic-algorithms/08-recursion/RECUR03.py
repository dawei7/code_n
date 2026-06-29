


def solve():
    def Factorial(n):
        if n==0 or n==1:
            return 1
        return n*Factorial(n-1)

    n = int(input())
    print(Factorial(n))


if __name__ == "__main__":
    solve()
