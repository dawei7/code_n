# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int , input().split()))
        se = []
        so = []

        for i in a:
            if(i%2 == 0):
                se.append(i)
            else:
                so.append(i)

        se.sort(reverse = True)
        so.sort()

        do = 0
        de = 0

        for i in so:
            do += so[-1] - i
        for i in se:
            de += i-se[-1]

        if(do == de):
            print("YES")
        elif(abs(do-de)%n == 0):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
