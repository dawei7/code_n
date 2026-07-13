import heapq


def solve(lists: list[list[int]]) -> list[int]:
    heap: list[tuple[int, int, int]] = []
    for list_index, values in enumerate(lists):
        if values:
            heapq.heappush(heap, (values[0], list_index, 0))

    result: list[int] = []
    while heap:
        value, list_index, value_index = heapq.heappop(heap)
        result.append(value)
        value_index += 1
        if value_index < len(lists[list_index]):
            heapq.heappush(
                heap,
                (lists[list_index][value_index], list_index, value_index),
            )
    return result
