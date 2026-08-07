class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        nums.sort()
        children = [[-1, -1]]
        counts = [0]

        def add(value: int, delta: int) -> None:
            node = 0
            for bit in range(19, -1, -1):
                branch = (value >> bit) & 1
                next_node = children[node][branch]
                if next_node == -1:
                    next_node = len(children)
                    children[node][branch] = next_node
                    children.append([-1, -1])
                    counts.append(0)
                node = next_node
                counts[node] += delta

        def maximum_xor(value: int) -> int:
            node = 0
            result = 0
            for bit in range(19, -1, -1):
                branch = (value >> bit) & 1
                preferred = children[node][branch ^ 1]
                if preferred != -1 and counts[preferred] > 0:
                    result |= 1 << bit
                    node = preferred
                else:
                    node = children[node][branch]
            return result

        answer = 0
        left = 0
        for value in nums:
            add(value, 1)
            while nums[left] * 2 < value:
                add(nums[left], -1)
                left += 1
            answer = max(answer, maximum_xor(value))

        return answer
