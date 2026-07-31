class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        answer = float("inf")
        previous = set()

        for number in nums:
            current = {number}
            for value in previous:
                current.add(value | number)

            for value in current:
                answer = min(answer, abs(value - k))
            if answer == 0:
                return 0

            previous = current

        return int(answer)
