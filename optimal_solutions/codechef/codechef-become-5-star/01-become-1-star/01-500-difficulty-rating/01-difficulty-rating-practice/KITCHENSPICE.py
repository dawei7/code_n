


def solve():
    for _ in range(int(input())):
        x = int(input())
        if x < 4: print('Mild')
        elif x < 7: print('Medium')
        else: print('Hot')


if __name__ == "__main__":
    solve()
