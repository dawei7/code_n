


def solve():
    def recurrent_sum_of_digits(n):
        if n < 10:
            return n

        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n //= 10

        return recurrent_sum_of_digits(sum_digits)

    if __name__ == "__main__":
        n = int(input())
        print(recurrent_sum_of_digits(n))


if __name__ == "__main__":
    solve()
