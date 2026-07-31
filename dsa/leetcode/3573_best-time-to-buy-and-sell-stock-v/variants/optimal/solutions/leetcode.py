class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        neg = -(10**30)
        flat = [neg] * (k + 1)
        long = [neg] * k
        short = [neg] * k
        flat[0] = 0

        for price in prices:
            next_flat = flat[:]
            next_long = long[:]
            next_short = short[:]
            for done in range(k):
                next_long[done] = max(long[done], flat[done] - price)
                next_short[done] = max(short[done], flat[done] + price)
                next_flat[done + 1] = max(
                    flat[done + 1],
                    long[done] + price,
                    short[done] - price,
                )
            flat, long, short = next_flat, next_long, next_short

        return max(flat)
