# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        d = list(map(int,input().split()))

        winner = -1
        for i in range(n):
            if i==0:
                attack = (a[i+1], a[-1], a[i+1]+a[-1])

            elif i==(n-1):
                attack = (a[i-1], a[0], a[i-1]+a[0])

            else:
                attack = (a[i-1], a[i+1], a[i-1]+a[i+1])

            if d[i] > max(attack):
                winner = max(winner, d[i])

        print(winner)


if __name__ == "__main__":
    solve()
