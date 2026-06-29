# cook your dish here


def solve():
    t = int(input())
    for i in range(t):
        N = int(input())
        count = 0
        # D = list(map(int, input().split())
        D = int(input())
        while D > 0:
            K = D % 10
            if K % 5 == 0:
                count += 1
            D //= 10
        if count == 0:
            print("No")
        elif count > 0:
            print("Yes")


if __name__ == "__main__":
    solve()
