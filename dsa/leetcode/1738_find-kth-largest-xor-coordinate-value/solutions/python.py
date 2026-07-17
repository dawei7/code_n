import heapq


def solve(matrix: list[list[int]], k: int) -> int:
    columns = len(matrix[0])
    previous = [0] * (columns + 1)
    largest: list[int] = []

    for row in matrix:
        current = [0] * (columns + 1)
        for column, value in enumerate(row, start=1):
            prefix = (
                value
                ^ previous[column]
                ^ current[column - 1]
                ^ previous[column - 1]
            )
            current[column] = prefix
            if len(largest) < k:
                heapq.heappush(largest, prefix)
            elif prefix > largest[0]:
                heapq.heapreplace(largest, prefix)
        previous = current

    return largest[0]
