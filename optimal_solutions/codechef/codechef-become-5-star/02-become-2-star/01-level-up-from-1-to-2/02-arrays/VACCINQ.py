# cook your dish here


def solve():
    for t in range(int(input())):
        n, p, x, y = map(int, input().split())

        a = list(map(int, input().split()))

        c, child, elder = 0, 0, 0

        for i in a:
            c += 1;
            if (c <= p):
                if i:
                    elder += 1 
                else:
                    child += 1 
            else:
                break
        print((child*x) + (elder*y))


if __name__ == "__main__":
    solve()
