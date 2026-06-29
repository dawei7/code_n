# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        if n%4:
            print('not good')
        else:
            print('good')


if __name__ == "__main__":
    solve()
