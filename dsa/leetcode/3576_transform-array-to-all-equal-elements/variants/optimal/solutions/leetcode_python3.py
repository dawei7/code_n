class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def operations(target: int) -> int:
            count = 0
            flipped = False
            for value in nums[:-1]:
                effective = -value if flipped else value
                flipped = effective != target
                count += flipped
            last = -nums[-1] if flipped else nums[-1]
            return count if last == target else k + 1

        return min(operations(1), operations(-1)) <= k
