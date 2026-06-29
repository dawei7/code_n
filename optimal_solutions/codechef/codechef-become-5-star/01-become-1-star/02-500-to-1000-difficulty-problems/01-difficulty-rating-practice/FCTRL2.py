


def solve():
    def multiply(x, res, res_size):
        carry = 0
        for i in range(res_size):
            prod = res[i] * x + carry
            res[i] = prod % 10
            carry = prod // 10

        while carry != 0:
            res[res_size] = carry % 10
            carry = carry // 10
            res_size += 1
        return res_size

    def factorial(n):
        MAX = 500
        res = [0] * MAX
        res[0] = 1
        res_size = 1

        for x in range(2, n + 1):
            res_size = multiply(x, res, res_size)

        # print("Factorial of given number is")
        for i in range(res_size - 1, -1, -1):
            print(res[i], end="")
        print()

    if __name__ == "__main__":
        t = int(input())
        for _ in range(t):
            n = int(input())
            factorial(n)


if __name__ == "__main__":
    solve()
