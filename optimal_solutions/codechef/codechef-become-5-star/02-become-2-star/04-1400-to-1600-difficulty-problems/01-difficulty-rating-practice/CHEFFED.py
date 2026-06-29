


def solve():
    def sum_digit(n):
        n = str(n)
        s = 0
        for i in n:
            i = int(i)
            s += i
        return s


    n = int(input())
    res = 0
    if n <= 200:
        for i in range(n):
            s = i + sum_digit(i) + sum_digit(sum_digit(i))
            if s == n:
                 res += 1
    else:
        for i in range(n-200, n):
            s = i + sum_digit(i) + sum_digit(sum_digit(i))
            if s == n:
                res += 1
    print(res)


if __name__ == "__main__":
    solve()
