import heapq


def solve(grid: list[list[int]], limits: list[int], k: int) -> int:
    heap = []

    for row_index, row in enumerate(grid):
        row.sort(reverse=True)
        if limits[row_index]:
            heapq.heappush(heap, (-row[0], row_index, 0))

    total = 0
    for _ in range(k):
        negative, row_index, column_index = heapq.heappop(heap)
        total -= negative
        column_index += 1

        if column_index < limits[row_index]:
            heapq.heappush(
                heap,
                (-grid[row_index][column_index], row_index, column_index),
            )

    return total
