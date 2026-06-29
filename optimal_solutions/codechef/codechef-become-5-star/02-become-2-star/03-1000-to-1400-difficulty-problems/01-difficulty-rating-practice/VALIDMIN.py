import sys


def solve():
    for _ in range(int(sys.stdin.readline())):
        a=list(map(int,sys.stdin.readline().split()))
        sys.stdout.write('YES\n' if a.count(min(a))>=2 else 'NO\n')


if __name__ == "__main__":
    solve()
