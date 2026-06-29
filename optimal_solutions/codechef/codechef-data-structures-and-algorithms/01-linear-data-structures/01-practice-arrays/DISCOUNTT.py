


def solve():
    class Solution:
        def check_coupon(self, n, x, y, prices):
            save = 0
            for price in prices:
                if price >= y:
                    save += y
                else:
                    save += price

            if save > x:
                return "COUPON"
            else:
                return "NO COUPON"


if __name__ == "__main__":
    solve()
