def solve(nums: list[int], low: int, high: int) -> int:
    def count_less(limit: int) -> int:
        root = [None, None, 0]
        total = 0

        for value in nums:
            node = root
            for bit in range(14, -1, -1):
                value_bit = (value >> bit) & 1
                limit_bit = (limit >> bit) & 1

                if limit_bit:
                    same = node[value_bit]
                    if same is not None:
                        total += same[2]
                    node = node[value_bit ^ 1]
                else:
                    node = node[value_bit]

                if node is None:
                    break

            node = root
            for bit in range(14, -1, -1):
                value_bit = (value >> bit) & 1
                if node[value_bit] is None:
                    node[value_bit] = [None, None, 0]
                node = node[value_bit]
                node[2] += 1

        return total

    return count_less(high + 1) - count_less(low)
