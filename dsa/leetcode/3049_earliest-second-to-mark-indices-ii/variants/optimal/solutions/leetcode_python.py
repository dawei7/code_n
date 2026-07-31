import heapq


class Solution:
    def earliestSecondToMarkIndices(
        self,
        nums: List[int],
        changeIndices: List[int],
    ) -> int:
        index_count = len(nums)
        baseline_operations = sum(nums) + index_count

        def can_finish(seconds: int) -> bool:
            first_occurrence = [-1] * index_count
            for second in range(seconds - 1, -1, -1):
                first_occurrence[changeIndices[second] - 1] = second

            selected_resets = []
            saved_operations = 0
            free_seconds = 0

            for second in range(seconds - 1, -1, -1):
                index = changeIndices[second] - 1
                value = nums[index]

                if second != first_occurrence[index] or value <= 1:
                    free_seconds += 1
                    continue

                heapq.heappush(selected_resets, value)
                saved_operations += value - 1

                if free_seconds:
                    free_seconds -= 1
                else:
                    removed = heapq.heappop(selected_resets)
                    saved_operations -= removed - 1
                    free_seconds += 1

            return baseline_operations - saved_operations <= seconds

        left = 1
        right = len(changeIndices)
        answer = -1

        while left <= right:
            middle = (left + right) // 2
            if can_finish(middle):
                answer = middle
                right = middle - 1
            else:
                left = middle + 1

        return answer
