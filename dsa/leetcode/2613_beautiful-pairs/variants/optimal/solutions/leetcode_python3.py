from typing import List


class Solution:
    def beautifulPair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        width = max(nums2) + 1
        trees = {
            -1: [-1] * (2 * width),
            1: [-1] * (2 * width),
        }

        def better(i: int, j: int, sign: int) -> int:
            if i < 0:
                return j
            if j < 0:
                return i
            key_i = (-nums1[i] + sign * nums2[i], i)
            key_j = (-nums1[j] + sign * nums2[j], j)
            return i if key_i <= key_j else j

        def update(position: int, index: int, sign: int) -> None:
            tree = trees[sign]
            position += width
            tree[position] = better(tree[position], index, sign)
            position //= 2
            while position:
                tree[position] = better(tree[2 * position], tree[2 * position + 1], sign)
                position //= 2

        def query(left: int, right: int, sign: int) -> int:
            tree = trees[sign]
            left += width
            right += width
            result = -1
            while left <= right:
                if left & 1:
                    result = better(result, tree[left], sign)
                    left += 1
                if not right & 1:
                    result = better(result, tree[right], sign)
                    right -= 1
                left //= 2
                right //= 2
            return result

        best = (10**30, (n, n))
        for i in sorted(range(n), key=lambda index: (nums1[index], index)):
            y = nums2[i]
            candidates = (query(0, y, -1), query(y, width - 1, 1))
            for j in candidates:
                if j < 0:
                    continue
                pair = (min(i, j), max(i, j))
                distance = abs(nums1[i] - nums1[j]) + abs(nums2[i] - nums2[j])
                best = min(best, (distance, pair))
            update(y, i, -1)
            update(y, i, 1)

        return list(best[1])
