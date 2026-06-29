# cook your dish here


def solve():
    T = int(input())

    for tc in range (T):
        R,C,K = map(int, input().split())
        c = 0
        for Rd in range (1,9):
            for Cd in range (1,9):
                if (max(abs(Rd-R),abs(Cd-C)) <= K):
                    c += 1
        print(c)


if __name__ == "__main__":
    solve()
