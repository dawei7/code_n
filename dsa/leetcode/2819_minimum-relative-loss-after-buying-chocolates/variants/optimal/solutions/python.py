from bisect import bisect_right


def solve(prices: list[int], queries: list[list[int]]) -> list[int]:
    prices.sort()
    length = len(prices)
    prefix = [0] * (length + 1)

    for index, price in enumerate(prices):
        prefix[index + 1] = prefix[index] + price

    answer: list[int] = []

    for threshold, count in queries:
        affordable = bisect_right(prices, threshold)
        low = max(0, count - (length - affordable))
        high = min(count, affordable)

        while low < high:
            chosen_low = (low + high) // 2
            paired_high = length - count + chosen_low
            if prices[chosen_low] + prices[paired_high] < 2 * threshold:
                low = chosen_low + 1
            else:
                high = chosen_low

        chosen_low = low
        chosen_high = count - chosen_low
        high_sum = prefix[length] - prefix[length - chosen_high]
        loss = prefix[chosen_low] + 2 * threshold * chosen_high - high_sum
        answer.append(loss)

    return answer
