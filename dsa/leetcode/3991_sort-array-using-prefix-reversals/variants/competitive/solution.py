from collections import deque


class Solution:
    def sortArray(self, nums: List[int], pre: List[int]) -> int:
        start = tuple(nums)
        target = tuple(range(len(nums)))
        if start == target:
            return 0

        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            current, distance = queue.popleft()
            for length in pre:
                next_state = current[:length][::-1] + current[length:]
                if next_state == target:
                    return distance + 1
                if next_state not in seen:
                    seen.add(next_state)
                    queue.append((next_state, distance + 1))

        return -1
