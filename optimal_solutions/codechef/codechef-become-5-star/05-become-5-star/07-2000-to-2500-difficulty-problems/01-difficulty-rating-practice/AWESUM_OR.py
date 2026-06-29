


def solve():
    def count_set_bits(n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

    # cook your dish here
    def power(x, y, p):
        res = 1 # Initialize result

        # Update x if it is
        # more than or equal to p
        x = x % p

        while (y > 0):

            # If y is odd, multiply
            # x with the result
            if (y & 1):
                res = (res * x) % p

            # y must be even now
            y = y >> 1 # y = y/2
            x = (x * x) % p

        return res

    t = int(input())
    while(t>0):
        n = int(input())
        c = count_set_bits(n)
        mod = 1000000007
        ans = ((3**c) + (3-(2**c)*3))
        ans %= mod
        print(ans)

        t-=1


if __name__ == "__main__":
    solve()
