# cook your dish here


def solve():
    z = 1000001
    a = [0]*z
    a[0] = 0.45
    for i in range(1,z):
        a[i] = 0.45 + 0.1 *a[i - 1]
    for i in range(1,z):
        a[i] = a[i]+a[i-1]
    for i in range(int(input())):
        n = int(input())
        print(a[n-1])


if __name__ == "__main__":
    solve()
