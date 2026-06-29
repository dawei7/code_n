


def solve():
    def calculate_streak(arr, n):
        streak = 0
        max_streak = 0
        for i in range(n):
            if arr[i] > 0:
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 0
        return max_streak

    t = int(input())

    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        om = calculate_streak(a, n)
        addy = calculate_streak(b, n)

        if om > addy:
            print("OM")
        elif om < addy:
            print("ADDY")
        else:
            print("DRAW")

        t -= 1


if __name__ == "__main__":
    solve()
