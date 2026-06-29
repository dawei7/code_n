# cook your dish here


def solve():
    for T in range(int(input())):

        L = int(input())
        S = input()

        try:
            print(S.index('0'))
        except:
            print(L)


if __name__ == "__main__":
    solve()
