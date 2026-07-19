def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    sorted_nums = sorted(nums)
    ordered_queries = sorted(
        (limit, value, index)
        for index, (value, limit) in enumerate(queries)
    )

    trie = [[-1, -1]]

    def insert(number: int) -> None:
        node = 0
        for bit_index in range(29, -1, -1):
            bit = (number >> bit_index) & 1
            child = trie[node][bit]
            if child == -1:
                child = len(trie)
                trie[node][bit] = child
                trie.append([-1, -1])
            node = child

    def maximum_xor(value: int) -> int:
        node = 0
        result = 0
        for bit_index in range(29, -1, -1):
            bit = (value >> bit_index) & 1
            preferred = bit ^ 1
            if trie[node][preferred] != -1:
                result |= 1 << bit_index
                node = trie[node][preferred]
            else:
                node = trie[node][bit]
        return result

    answers = [-1] * len(queries)
    inserted = 0
    for limit, value, query_index in ordered_queries:
        while inserted < len(sorted_nums) and sorted_nums[inserted] <= limit:
            insert(sorted_nums[inserted])
            inserted += 1
        if inserted > 0:
            answers[query_index] = maximum_xor(value)

    return answers
