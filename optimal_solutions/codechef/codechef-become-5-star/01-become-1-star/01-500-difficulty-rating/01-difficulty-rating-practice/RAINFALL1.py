


def solve():
    for _ in range(int(input())):
        x = int(input())
        print('Light' if x < 3 else ('Moderate' if x < 7 else 'Heavy'))


if __name__ == "__main__":
    solve()
