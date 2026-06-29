


def solve():
    T = int(input())
    for _ in range(T):
        s = input()
        n = len(s)
        killed = [False] * n

        for i in range(n):
            if s[i] == 'm':
                if i - 1 >= 0 and s[i - 1] == 's' and not killed[i - 1]:
                    killed[i - 1] = True
                    continue
                if i + 1 < n and s[i + 1] == 's':
                    killed[i + 1] = True

        snakes = 0
        mongooses = 0

        for i in range(n):
            if s[i] == 's' and not killed[i]:
                snakes += 1
            if s[i] == 'm':
                mongooses += 1

        ans = "tie"
        if snakes > mongooses:
            ans = "snakes"
        elif mongooses > snakes:
            ans = "mongooses"

        print(ans)


if __name__ == "__main__":
    solve()
