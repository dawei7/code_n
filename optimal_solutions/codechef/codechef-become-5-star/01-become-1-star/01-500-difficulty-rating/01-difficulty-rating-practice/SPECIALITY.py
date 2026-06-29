


def solve():
    for _ in range(int(input())):
        x, y, z = map(int, input().split())
        if x > max(y, z):
            print('Setter')
        elif y > max(x, z):
            print('Tester')
        else:
            print('Editorialist')


if __name__ == "__main__":
    solve()
