import math


def solve(
    num_dice: int = 20, sides: int = 12, top_k: int = 10, target_sum: int = 70
) -> int:
    """Find the number of ways twenty 12-sided dice can be rolled so the top 10 sum to 70.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Partitioning Top-K Dice Outcomes:
       We generate all non-increasing sequences (x_1, x_2, ..., x_K) of length top_k = 10
       where sides >= x_1 >= x_2 >= ... >= x_K >= 1 and sum(x_i) = target_sum = 70.

    2. Remaining Dice Assignment via Multinomial Counting:
       Let m = x_K be the smallest value among the top K dice.
       The remaining (num_dice - top_k) = 10 dice must take values in {1, 2, ..., m}.
       For any frequency assignment (f_1, f_2, ..., f_sides) of all 20 dice:
           Ways = (num_dice)! / (f_1! * f_2! * ... * f_sides!).

    3. Fast Backtracking & Combinatorial Summation:
       We enumerate the valid top partitions and branch over remaining non-increasing
       allocations, summing the exact multinomial coefficient for each complete multiset.

    Complexity:
    -----------
    - Time Complexity: O(P(target_sum, top_k)) where partitions count < 15,000 (< 0.05 seconds).
    - Space Complexity: O(sides) auxiliary frequency arrays.
    """
    valid_top_tuples = []

    def search_top(
        idx: int,
        last_val: int,
        curr_sum: int,
        curr_tuple: list[int],
    ) -> None:
        if idx == top_k:
            if curr_sum == target_sum:
                valid_top_tuples.append(list(curr_tuple))
            return

        rem_dice = top_k - idx
        if curr_sum + rem_dice * 1 > target_sum:
            return
        if curr_sum + rem_dice * last_val < target_sum:
            return

        for val in range(
            min(last_val, target_sum - curr_sum - (rem_dice - 1)), 0, -1
        ):
            curr_tuple.append(val)
            search_top(idx + 1, val, curr_sum + val, curr_tuple)
            curr_tuple.pop()

    search_top(0, sides, 0, [])

    total_ways = 0
    rem_dice_count = num_dice - top_k

    for top_tup in valid_top_tuples:
        min_top_val = top_tup[-1]
        top_freq = [0] * (sides + 1)
        for v in top_tup:
            top_freq[v] += 1

        def search_rem(val: int, rem_left: int, curr_rem_freq: list[int]) -> None:
            nonlocal total_ways
            if val == 1:
                curr_rem_freq[1] = rem_left
                total_freq = [
                    top_freq[i] + curr_rem_freq[i] for i in range(sides + 1)
                ]
                num = math.factorial(num_dice)
                den = 1
                for f in total_freq:
                    den *= math.factorial(f)
                total_ways += num // den
                return

            for cnt in range(rem_left + 1):
                curr_rem_freq[val] = cnt
                search_rem(val - 1, rem_left - cnt, curr_rem_freq)
                curr_rem_freq[val] = 0

        search_rem(min_top_val, rem_dice_count, [0] * (sides + 1))

    return total_ways


if __name__ == "__main__":
    print(solve())
