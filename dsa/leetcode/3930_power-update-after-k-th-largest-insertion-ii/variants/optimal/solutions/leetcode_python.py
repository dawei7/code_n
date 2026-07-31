class Solution:
    def powerUpdate(
        self,
        nums: list[int],
        p: int,
        queries: list[list[int]],
    ) -> list[int]:
        modulus = 1_000_000_007
        values = sorted(set(nums) | {value for value, _ in queries})
        positions = {value: index + 1 for index, value in enumerate(values)}
        tree = [0] * (len(values) + 1)

        def add(index: int) -> None:
            while index < len(tree):
                tree[index] += 1
                index += index & -index

        for value in nums:
            add(positions[value])

        def select(rank: int) -> int:
            index = 0
            step = 1 << (len(values).bit_length() - 1)
            while step:
                next_index = index + step
                if next_index < len(tree) and tree[next_index] < rank:
                    rank -= tree[next_index]
                    index = next_index
                step >>= 1
            return values[index]

        size = len(nums)
        answer = []
        for value, k in queries:
            add(positions[value])
            size += 1
            exponent = select(size - k + 1)
            p = pow(p, exponent, modulus)
            answer.append(p)

        return answer
