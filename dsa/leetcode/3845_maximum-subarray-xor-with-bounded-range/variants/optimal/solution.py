from collections import deque


class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_xor = [0] * (n + 1)
        for index, value in enumerate(nums):
            prefix_xor[index + 1] = prefix_xor[index] ^ value

        zero_child = [-1]
        one_child = [-1]
        count = [0]

        def update(value: int, delta: int) -> None:
            node = 0
            count[node] += delta

            for bit in range(14, -1, -1):
                branch = (value >> bit) & 1
                child = zero_child[node] if branch == 0 else one_child[node]

                if child == -1:
                    child = len(count)
                    zero_child.append(-1)
                    one_child.append(-1)
                    count.append(0)
                    if branch == 0:
                        zero_child[node] = child
                    else:
                        one_child[node] = child

                node = child
                count[node] += delta

        def maximum_xor(value: int) -> int:
            node = 0
            result = 0

            for bit in range(14, -1, -1):
                branch = (value >> bit) & 1
                preferred = one_child[node] if branch == 0 else zero_child[node]

                if preferred != -1 and count[preferred] > 0:
                    result |= 1 << bit
                    node = preferred
                else:
                    node = zero_child[node] if branch == 0 else one_child[node]

            return result

        maximum_indices: deque[int] = deque()
        minimum_indices: deque[int] = deque()
        left = 0
        answer = 0

        for right, value in enumerate(nums):
            update(prefix_xor[right], 1)

            while maximum_indices and nums[maximum_indices[-1]] <= value:
                maximum_indices.pop()
            maximum_indices.append(right)

            while minimum_indices and nums[minimum_indices[-1]] >= value:
                minimum_indices.pop()
            minimum_indices.append(right)

            while nums[maximum_indices[0]] - nums[minimum_indices[0]] > k:
                update(prefix_xor[left], -1)
                if maximum_indices[0] == left:
                    maximum_indices.popleft()
                if minimum_indices[0] == left:
                    minimum_indices.popleft()
                left += 1

            answer = max(answer, maximum_xor(prefix_xor[right + 1]))

        return answer
