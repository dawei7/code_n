from heapq import heapify, heappop, heappush
from math import isqrt


def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    nums = nums[:]
    value_limit = max(max(nums), max(value for _, value in queries))
    is_prime = bytearray(b"\1") * (value_limit + 1)
    is_prime[:2] = b"\0\0"
    for value in range(2, isqrt(value_limit) + 1):
        if is_prime[value]:
            start = value * value
            is_prime[start : value_limit + 1 : value] = b"\0" * ((value_limit - start) // value + 1)

    occurrence_sets: dict[int, set[int]] = {}
    for index, value in enumerate(nums):
        if is_prime[value]:
            occurrence_sets.setdefault(value, set()).add(index)

    occurrences: dict[int, list] = {}
    for value, indices in occurrence_sets.items():
        minimum_heap = list(indices)
        maximum_heap = [-index for index in indices]
        heapify(minimum_heap)
        heapify(maximum_heap)
        occurrences[value] = [indices, minimum_heap, maximum_heap]

    split_count = len(nums) - 1
    maximum_overlap = [0] * (4 * split_count)
    lazy_add = [0] * (4 * split_count)

    def range_add(
        query_left: int,
        query_right: int,
        delta: int,
        node: int = 1,
        left: int = 0,
        right: int = split_count - 1,
    ) -> None:
        if query_left > query_right:
            return
        if query_left <= left and right <= query_right:
            maximum_overlap[node] += delta
            lazy_add[node] += delta
            return

        middle = (left + right) // 2
        if query_left <= middle:
            range_add(query_left, query_right, delta, node * 2, left, middle)
        if middle < query_right:
            range_add(query_left, query_right, delta, node * 2 + 1, middle + 1, right)
        maximum_overlap[node] = lazy_add[node] + max(maximum_overlap[node * 2], maximum_overlap[node * 2 + 1])

    def extreme_indices(value: int) -> tuple[int, int]:
        active, minimum_heap, maximum_heap = occurrences[value]
        while minimum_heap[0] not in active:
            heappop(minimum_heap)
        while -maximum_heap[0] not in active:
            heappop(maximum_heap)
        return minimum_heap[0], -maximum_heap[0]

    def add_prime_interval(value: int, delta: int) -> None:
        if occurrences[value][0]:
            first, last = extreme_indices(value)
            range_add(first, last - 1, delta)

    for value in occurrences:
        add_prime_interval(value, 1)

    distinct_prime_count = len(occurrences)
    answers = []
    for index, value in queries:
        old_value = nums[index]
        if old_value != value:
            if is_prime[old_value]:
                add_prime_interval(old_value, -1)
                occurrences[old_value][0].remove(index)
                if not occurrences[old_value][0]:
                    distinct_prime_count -= 1
                add_prime_interval(old_value, 1)

            if is_prime[value]:
                if value not in occurrences:
                    occurrences[value] = [set(), [], []]
                add_prime_interval(value, -1)
                active, minimum_heap, maximum_heap = occurrences[value]
                if not active:
                    distinct_prime_count += 1
                active.add(index)
                heappush(minimum_heap, index)
                heappush(maximum_heap, -index)
                add_prime_interval(value, 1)

            nums[index] = value

        answers.append(distinct_prime_count + maximum_overlap[1])

    return answers
