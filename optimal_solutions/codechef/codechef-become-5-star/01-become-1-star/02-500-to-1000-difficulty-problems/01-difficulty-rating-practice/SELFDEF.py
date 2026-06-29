# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        x = list(filter(lambda x: 10 <= x <=60, list(map(int, input().split(' ')))))
        print(len(x))


if __name__ == "__main__":
    solve()
