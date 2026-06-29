# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input()
        if a == "1" or a == "10":
            print("No\n")
        else:
            num = 0
            for i in range(n):
                if a[i] == '1':
                    num += 1
            if num <= 3:
                print("Yes\n")
            else:
                print("No\n")


if __name__ == "__main__":
    solve()
