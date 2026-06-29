# cook your dish here


def solve():
    for _ in range(int(input())):
        n =int(input())
        goals=list(map(int, input().split()))
        min_goal=goals[0]
        max_goal=0
        for i in range(n):
            if goals[i] < min_goal:
                min_goal = goals[i]
            elif goals[i] - min_goal > max_goal:
                 max_goal = goals[i] - min_goal
        if max_goal > 0:
            print(max_goal)
        else:
            print("UNFIT")


if __name__ == "__main__":
    solve()
