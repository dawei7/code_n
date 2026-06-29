# cook your dish here


def solve():
    for i in range(int(input())):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))

        if k not in a:
            print('No')             #not at all possible

        else:       #k in a
            if n%2 == 0 and a[(n-1)//2] == k:
                print('Yes')

            elif n%2 != 0 and a[n//2] == k:
                print('Yes')

            elif a.index(k) != (n-1):
                print('Yes')

            else:
                print('No')


if __name__ == "__main__":
    solve()
