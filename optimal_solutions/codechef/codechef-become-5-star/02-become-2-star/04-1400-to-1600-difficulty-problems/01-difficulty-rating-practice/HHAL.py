


def solve():
    def Solve(s):
        return 1 if(s==s[::-1]) else 2 
    for _ in range(int(input())):
        s=input()
        print(Solve(s))


if __name__ == "__main__":
    solve()
