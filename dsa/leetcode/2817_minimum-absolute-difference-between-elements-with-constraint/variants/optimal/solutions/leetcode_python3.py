from bisect import bisect_left


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        values = sorted(set(nums))
        size = len(values)
        tree = [0] * (size + 1)

        def add(index: int) -> None:
            index += 1
            while index <= size:
                tree[index] += 1
                index += index & -index

        def prefix(end: int) -> int:
            count = 0
            while end:
                count += tree[end]
                end -= end & -end
            return count

        def kth(order: int) -> int:
            index = 0
            step = 1 << (size.bit_length() - 1)
            while step:
                candidate = index + step
                if candidate <= size and tree[candidate] < order:
                    index = candidate
                    order -= tree[candidate]
                step >>= 1
            return index

        answer = float("inf")
        inserted = 0

        for right, value in enumerate(nums):
            if right < x:
                continue

            add(bisect_left(values, nums[right - x]))
            inserted += 1
            position = bisect_left(values, value)
            before = prefix(position)

            if before:
                answer = min(answer, value - values[kth(before)])
            if before < inserted:
                answer = min(answer, values[kth(before + 1)] - value)

        return answer
