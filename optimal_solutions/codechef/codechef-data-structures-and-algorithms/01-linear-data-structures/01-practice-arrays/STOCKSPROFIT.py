


def solve():
    def findMaxProfit(prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price   # update minimum seen so far
            elif price - min_price > max_profit:
                max_profit = price - min_price  # update max profit
        return max_profit


if __name__ == "__main__":
    solve()
