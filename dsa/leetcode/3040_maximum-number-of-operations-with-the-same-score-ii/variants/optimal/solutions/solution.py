class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        choices = [
            (nums[0] + nums[1], 2),
            (nums[-2] + nums[-1], 0),
            (nums[0] + nums[-1], 1),
        ]
        answer = 0

        for target in {score for score, _ in choices}:
            base_length = n % 2
            previous = [0] * (n - base_length + 1)

            for length in range(base_length + 2, n - 1, 2):
                current = [0] * (n - length + 1)

                for start in range(n - length + 1):
                    end = start + length - 1
                    best = 0

                    if nums[start] + nums[start + 1] == target:
                        best = max(best, 1 + previous[start + 2])
                    if nums[end - 1] + nums[end] == target:
                        best = max(best, 1 + previous[start])
                    if nums[start] + nums[end] == target:
                        best = max(best, 1 + previous[start + 1])

                    current[start] = best

                previous = current

            for score, start in choices:
                if score == target:
                    answer = max(answer, 1 + previous[start])

        return answer
