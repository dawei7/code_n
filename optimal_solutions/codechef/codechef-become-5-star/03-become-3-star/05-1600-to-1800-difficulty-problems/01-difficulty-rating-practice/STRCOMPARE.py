# www.codechef.com/problems/STRCOMPARE


def solve():
    def suffix_comp():
        N = int(input())
        Astr = input().strip()
        Bstr = input().strip()

        A_first = 0
        ahead = False
        for a, b in zip(reversed(Astr), reversed(Bstr)):
            if a < b:
                ahead = True
            elif a > b:
                ahead = False
            A_first += ahead

        return A_first


    # ======================= #

    if __name__ == "__main__":
        T = int(input())
        for _ in range(T):
            print(suffix_comp())


if __name__ == "__main__":
    solve()
