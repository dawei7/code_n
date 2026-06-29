


def solve():
    t = int(input())


    while t > 0:

        n,k = map(int,input().split())

        s = input()
        count = 0
        c = 0
        for i in s:

            if i == '0':
                c += 1
            else:
                c = 0

            if c == k:
                c = 0
                count += 1
        print(count)


        t -= 1


if __name__ == "__main__":
    solve()
