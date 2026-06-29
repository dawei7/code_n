import math

# Function to calculate LCM of 2 integers


def solve():
    def lcm_of_two_nums(a, b):
        return (a * b) // math.gcd(a, b)

    # Function to calculate LCM of 3 integers
    def lcm_of_three_nums(a, b, c):
        return lcm_of_two_nums(a, lcm_of_two_nums(b, c))

    t = int(input())

    for _ in range(t):
        n, a, b, c = map(int, input().split())

        s_a = n // a
        s_b = n // b
        s_c = n // c

        s_ab = n // lcm_of_two_nums(a, b)
        s_bc = n // lcm_of_two_nums(b, c)
        s_ac = n // lcm_of_two_nums(a, c)

        s_abc = n // lcm_of_three_nums(a, b, c)

        s = s_a + s_b + s_c - s_ab - s_bc - s_ac + s_abc

        print(s)


if __name__ == "__main__":
    solve()
