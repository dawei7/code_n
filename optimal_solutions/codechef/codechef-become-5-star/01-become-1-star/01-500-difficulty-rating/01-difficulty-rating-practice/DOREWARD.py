


def solve():
    t = int(input())
    for t in range(t):
        x = int(input())
        if x <= 3: print('Bronze')
        elif x <= 6: print('Silver')
        else: print('Gold')


if __name__ == "__main__":
    solve()
