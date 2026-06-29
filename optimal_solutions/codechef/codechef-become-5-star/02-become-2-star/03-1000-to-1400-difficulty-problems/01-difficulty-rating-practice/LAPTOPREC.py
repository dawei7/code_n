# cook your dish here
from collections import Counter


def solve():
    for _ in range(int(input())):
        n = int(input())
        t = Counter(input().split()).most_common(2)
        if len(t) == 2:
            print(t[0][0] if t[0][1]>t[1][1] else 'CONFUSED')
        else:
            print(t[0][0])


if __name__ == "__main__":
    solve()
