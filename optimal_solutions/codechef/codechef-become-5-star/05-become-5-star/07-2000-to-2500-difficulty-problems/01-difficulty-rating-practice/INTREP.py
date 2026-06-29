# cook your dish here


def solve():
    topi = int(input())

    for i in range(topi):
        n = int(input())
        if n % 2 == 0:
            print(2 * n, n)
        elif n == 1:
            print(3, 2)
        else:
            l = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
            for j in l:
                if n % j:
                    print(n * j, n * (j - 1))
                    break


if __name__ == "__main__":
    solve()
