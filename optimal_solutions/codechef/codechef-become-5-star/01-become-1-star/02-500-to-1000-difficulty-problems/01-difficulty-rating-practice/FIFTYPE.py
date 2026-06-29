# cook your dish here


def solve():
    x = (2,-3)
    for _ in range(int(input())):
        n = int(input())
        a = 0
        while n != 50:
            n += x[n>50]
            a+=1
        print(a)


if __name__ == "__main__":
    solve()
