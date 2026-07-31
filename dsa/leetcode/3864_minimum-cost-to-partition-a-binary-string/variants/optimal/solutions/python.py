def solve(s: str, encCost: int, flatCost: int) -> int:
    def evaluate(left: int, length: int) -> tuple[int, int]:
        if length % 2 == 1:
            ones = s.count("1", left, left + length)
            cost = flatCost if ones == 0 else length * ones * encCost
            return ones, cost

        half = length // 2
        left_ones, left_cost = evaluate(left, half)
        right_ones, right_cost = evaluate(left + half, half)
        ones = left_ones + right_ones
        unsplit_cost = flatCost if ones == 0 else length * ones * encCost
        return ones, min(unsplit_cost, left_cost + right_cost)

    return evaluate(0, len(s))[1]
