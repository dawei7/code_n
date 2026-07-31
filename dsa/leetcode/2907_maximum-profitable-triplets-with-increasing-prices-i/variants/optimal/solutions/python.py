def solve(prices: list[int], profits: list[int]) -> int:
    answer = -1

    for middle in range(1, len(prices) - 1):
        left_profit = -1
        for left in range(middle):
            if prices[left] < prices[middle]:
                left_profit = max(left_profit, profits[left])

        right_profit = -1
        for right in range(middle + 1, len(prices)):
            if prices[middle] < prices[right]:
                right_profit = max(right_profit, profits[right])

        if left_profit != -1 and right_profit != -1:
            answer = max(answer, left_profit + profits[middle] + right_profit)

    return answer

