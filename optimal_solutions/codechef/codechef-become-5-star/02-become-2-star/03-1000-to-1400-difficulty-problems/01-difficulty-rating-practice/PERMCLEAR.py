


def solve():
    for i in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = int(input())
        c = set(map(int, input().split()))  
        d = [item for item in a if item not in c]
        print(*d)


if __name__ == "__main__":
    solve()
