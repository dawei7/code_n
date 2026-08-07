class Solution(object):
    def countBlocks(self, nums):
        length = nums.size()
        blocks = 0
        start = 0

        while start < length:
            blocks += 1
            value = nums.at(start)
            equal = start
            step = 1

            while start + step < length and nums.at(start + step) == value:
                equal = start + step
                step *= 2

            different = min(length, start + step)
            while equal + 1 < different:
                middle = (equal + different) // 2
                if nums.at(middle) == value:
                    equal = middle
                else:
                    different = middle

            start = different

        return blocks
