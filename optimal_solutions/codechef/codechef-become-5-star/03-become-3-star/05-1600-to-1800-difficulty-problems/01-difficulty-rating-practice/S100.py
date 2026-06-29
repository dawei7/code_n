


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        arr = []
        for i in s:
            arr += [i]
        act = 0
        for j in range(n-2):
            if arr[j]=='1':
                act = 1
                break
        if not act:
            print(s)
        else:
            print("0"*j + '1' + "0"*(n-j-1))


if __name__ == "__main__":
    solve()
