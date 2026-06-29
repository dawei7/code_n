# cook your dish here


def solve():
    N = int(input())
    for i in range(N):
        P = list(map(int, input().split()))
        s = {
            0: "Beginner",
            1: "Junior Developer",
            2: "Middle Developer",
            3: "Senior Developer",
            4: "Hacker",
            5: "Jeff Dean"
        }
        Sum = sum(P)
        print(s[Sum])


if __name__ == "__main__":
    solve()
