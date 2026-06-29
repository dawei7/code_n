


def solve():
    T = int(input())
    for i in range(T):
        n = int(input())
        problems = list(map(int, input().split()))

        sum = 28
        problems_solved = 0
        for x in range(n):
            if problems[x] <= 7:
                sum -= problems[x]
            if sum == 0:
                problems_solved = x + 1
                break   

        print(problems_solved)


if __name__ == "__main__":
    solve()
