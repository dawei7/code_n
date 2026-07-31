class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        full_mask = (1 << length) - 1
        order = sorted(range(length), key=lambda index: nums[index])
        shifts = [pow(10, len(str(value)), k) for value in nums]
        memo = bytearray((1 << length) * k)

        def can_finish(mask, remainder):
            if mask == full_mask:
                return remainder == 0

            state = mask * k + remainder
            if memo[state]:
                return memo[state] == 2

            for index in order:
                bit = 1 << index
                if not mask & bit:
                    next_remainder = (remainder * shifts[index] + nums[index]) % k
                    if can_finish(mask | bit, next_remainder):
                        memo[state] = 2
                        return True

            memo[state] = 1
            return False

        if not can_finish(0, 0):
            return []

        answer = []
        mask = 0
        remainder = 0

        while mask != full_mask:
            for index in order:
                bit = 1 << index
                if not mask & bit:
                    next_remainder = (remainder * shifts[index] + nums[index]) % k
                    if can_finish(mask | bit, next_remainder):
                        answer.append(nums[index])
                        mask |= bit
                        remainder = next_remainder
                        break

        return answer
