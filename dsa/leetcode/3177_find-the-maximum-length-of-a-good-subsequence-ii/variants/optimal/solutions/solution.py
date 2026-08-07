class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        best_by_value = {}
        best_for_budget = [0] * (k + 1)

        for value in nums:
            ending_at_value = best_by_value.setdefault(value, [0] * (k + 1))

            for changes in range(k, -1, -1):
                length = ending_at_value[changes] + 1
                if changes > 0:
                    length = max(length, best_for_budget[changes - 1] + 1)

                ending_at_value[changes] = length
                best_for_budget[changes] = max(best_for_budget[changes], length)

        return best_for_budget[k]
