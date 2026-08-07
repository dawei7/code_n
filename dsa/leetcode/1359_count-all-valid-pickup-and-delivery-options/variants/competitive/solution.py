class Solution:
    def countOrders(self, n: int) -> int:
        modulus = 1_000_000_007
        count = 1

        for orders in range(1, n + 1):
            count = count * orders * (2 * orders - 1) % modulus

        return count
