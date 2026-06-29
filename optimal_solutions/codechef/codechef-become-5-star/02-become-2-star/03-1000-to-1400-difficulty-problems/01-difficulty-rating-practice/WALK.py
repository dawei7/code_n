


def solve():
    goals = int(input())
    for distractions in range(goals):
        wife = int(input())
        life = list(map(int, input().split()))
        aim = life[0]
        for success in range(1, wife):
            if aim < life[success] + success:
                aim = life[success] + success
        print(aim)


if __name__ == "__main__":
    solve()
