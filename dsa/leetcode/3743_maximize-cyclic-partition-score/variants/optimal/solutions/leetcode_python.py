class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        limit = min(k, len(nums) // 2)
        if limit == 0:
            return 0

        negative = -10**30

        completed = [negative] * (limit + 1)
        completed[0] = 0
        open_positive = [negative] * limit
        open_negative = [negative] * limit

        for value in nums:
            old_completed = completed
            old_positive = open_positive
            old_negative = open_negative
            completed = old_completed[:]
            open_positive = old_positive[:]
            open_negative = old_negative[:]

            for pairs in range(limit):
                completed[pairs + 1] = max(
                    completed[pairs + 1],
                    old_positive[pairs] - value,
                    old_negative[pairs] + value,
                )
                open_positive[pairs] = max(
                    open_positive[pairs], old_completed[pairs] + value
                )
                open_negative[pairs] = max(
                    open_negative[pairs], old_completed[pairs] - value
                )

        answer = max(completed)

        for outer_sign in (-1, 1):
            outer_open = [negative] * limit
            inner_positive = [negative] * limit
            inner_negative = [negative] * limit
            cyclic_completed = [negative] * (limit + 1)

            for value in nums:
                old_outer = outer_open
                old_positive = inner_positive
                old_negative = inner_negative
                outer_open = old_outer[:]
                inner_positive = old_positive[:]
                inner_negative = old_negative[:]

                for inner_pairs in range(limit):
                    cyclic_completed[inner_pairs + 1] = max(
                        cyclic_completed[inner_pairs + 1],
                        old_outer[inner_pairs] - outer_sign * value,
                    )

                    if inner_pairs + 1 < limit:
                        outer_open[inner_pairs + 1] = max(
                            outer_open[inner_pairs + 1],
                            old_positive[inner_pairs] - value,
                            old_negative[inner_pairs] + value,
                        )
                        inner_positive[inner_pairs] = max(
                            inner_positive[inner_pairs],
                            old_outer[inner_pairs] + value,
                        )
                        inner_negative[inner_pairs] = max(
                            inner_negative[inner_pairs],
                            old_outer[inner_pairs] - value,
                        )

                outer_open[0] = max(outer_open[0], outer_sign * value)

            answer = max(answer, max(cyclic_completed))

        return answer
