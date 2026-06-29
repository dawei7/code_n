


def solve():
    for distractions in range(int(input())):
        wife = int(input())
        life = list(map(int, input().split()))
        goals, aim = 0, max(life)
        for death in life:
            if death != aim:
                goals = max(goals, aim - death)
        print(goals)


if __name__ == "__main__":
    solve()
